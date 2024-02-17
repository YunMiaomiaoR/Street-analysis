# 教程https://blog.csdn.net/cxz_0030115/article/details/132041322?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-132041322-blog-127271682.235%5Ev38%5Epc_relevant_anti_vip_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-132041322-blog-127271682.235%5Ev38%5Epc_relevant_anti_vip_base&utm_relevant_index=6
# -*- coding: utf-8 -*-
import requests
import json
import xlwt
import math
#######https://blog.csdn.net/cxz_0030115/article/details/132041322?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-132041322-blog-127271682.235%5Ev38%5Epc_relevant_anti_vip_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-132041322-blog-127271682.235%5Ev38%5Epc_relevant_anti_vip_base&utm_relevant_index=6
# 改：TODO
amap_web_key = 'd353a4965ffa8e19ed7a100557b0a9d4'  # 高德地图官网申请的Web API KEY
filename = r'Mass transit.xslx'   # 爬取到的数据写入的EXCEL路径

# 改：多边形边界集合：
polygon_list = ['126.610882,45.78144|126.624529,45.766923']

# 改：POI分类集合, 多个类型用竖线 | 分割；
type_list = '150500|150700'  # 

#=========================下面不用改=====================================

poi_search_url = "http://restapi.amap.com/v3/place/polygon"  # URL
offset = 25  # 分页请求数据时的单页大小
def gcj02_to_wgs84(lon, lat):
    a = 6378245.0
    ee = 0.00669342162296594323
    pi = 3.14159265358979324

    def transform_lon(x, y):
        ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * \
              y * y + (0.1 * x * x * x) + \
              (0.2 * x * x * y) + (0.1 * x * y * y) + \
              (0.1 * y * y * y) + (0.1 * x * x * x * x) + \
              (0.2 * x * x * x * y) + (0.2 * x * x * y * y) + \
              (0.1 * x * y * y * y)
        return ret

    def transform_lat(x, y):
        ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * \
              y + 0.1 * x * y + 0.2 * \
              x * x + (0.1 * x * x * x) + \
              (0.1 * x * y * y) + (0.1 * x * x * y)
        return ret

    def transform(x, y):
        d_lat = transform_lat(x - 105.0, y - 35.0)
        d_lon = transform_lon(x - 105.0, y - 35.0)
        rad_lat = y / 180.0 * pi
        magic = math.sin(rad_lat)
        magic = 1 - ee * magic * magic
        sqrt_magic = math.sqrt(magic)
        d_lat = (d_lat * 180.0) / ((a * (1 - ee)) / (magic * sqrt_magic) * pi)
        d_lon = (d_lon * 180.0) / (a / sqrt_magic * math.cos(rad_lat) * pi)
        mg_lat = y + d_lat
        mg_lon = x + d_lon
        return [x * 2 - mg_lon, y * 2 - mg_lat]

    return transform(lon, lat)


# 根据矩形坐标获取poi数据
def getpois(polygon, type_list):
    i = 1
    current_polygon_poi_list = []
    while True:  # 使用while循环不断分页获取数据
        result = getpoi_page(polygon, i, type_list)
        result = json.loads(result)  # 将字符串转换为json

        if result['status'] != '1':  # 接口返回的状态不是1代表异常
            print('======爬取错误，返回数据：' + result)
            break
        pois = result['pois']
        if len(pois) < offset:  # 返回的数据不足分页页大小，代表数据爬取完
            current_polygon_poi_list.extend(pois)
            break
        current_polygon_poi_list.extend(pois)
        i += 1
    print('===========当前polygon：', polygon, ',爬取到的数据数量：', str(len(current_polygon_poi_list)))

    return current_polygon_poi_list


# 单页获取pois
def getpoi_page(polygon, page, type_list):
    print(polygon)
    req_url = poi_search_url + "?key=" + amap_web_key + '&extensions=all&polygon=' + polygon + '&offset=' + str(
        offset) + '&types=' + type_list + '&page=' + str(page) + '&output=json'
    data = ''
    with requests.get(req_url) as response:
        data = response.text
        print(data)
    return data


# 数据写入excel
def write_to_excel(poilist, filename):
    # 一个Workbook对象，这就相当于创建了一个Excel文件
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('0', cell_overwrite_ok=True)
    # 第一行(列标题)

    sheet.write(0, 0, 'id')
    sheet.write(0, 1, 'name')
    sheet.write(0, 2, 'lon')
    sheet.write(0, 3, 'lat')
    sheet.write(0, 4, 'address')
    sheet.write(0, 5, 'pname')
    sheet.write(0, 6, 'cityname')
    sheet.write(0, 7, 'adname')
    sheet.write(0, 8, 'type')
    for i in range(len(poilist)):
        sheet.write(i + 1, 0, poilist[i]['id'])
        sheet.write(i + 1, 1, poilist[i]['name'])
        lon = float(str(poilist[i]['location']).split(",")[0])
        lat = float(str(poilist[i]['location']).split(",")[1])

        # 将高德坐标转换为WGS 84坐标
        lon, lat = gcj02_to_wgs84(lon, lat)

        sheet.write(i + 1, 2, lon)
        sheet.write(i + 1, 3, lat)
        sheet.write(i + 1, 4, poilist[i].get('address'))
        sheet.write(i + 1, 5, poilist[i].get('pname'))
        sheet.write(i + 1, 6, poilist[i].get('cityname'))
        sheet.write(i + 1, 7, poilist[i].get('adname'))
        sheet.write(i + 1, 8, poilist[i]['type'])

    book.save(filename)


print('开始爬取...')
all_poi_list = []  # 爬取到的所有数据

for polygon in polygon_list:
    polygon_poi_list = getpois(polygon, type_list)
    all_poi_list.extend(polygon_poi_list)

print('爬取完成，总的数量：', len(all_poi_list))

write_to_excel(all_poi_list, filename)

print('写入成功')
