import xlwt
import json
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'Cookie': '_RSG=XCqQn7JEGUCu4M6He2y5wB; _RDG=28a8d08ce405ae29042ef9109d08feaf1f; _RGUID=c7903931-f16b-4321-be85-f02a11196138; MKT_CKID=1616676686325.e69zq.hj9o; nfes_isSupportWebP=1; GUID=09031170210339221227; UBT_VID=1707110024198.c292w2JTzDe8; _RF1=117.179.96.225; _jzqco=%7C%7C%7C%7C1707110024015%7C1.1132224340.1707110023725.1707110090005.1707110112327.1707110090005.1707110112327.0.0.0.4.4; _bfa=1.1707110024198.c292w2JTzDe8.1.1707110110589.1707110367177.1.4.290510',
    #可以根据需要设置其他请求头
}

#加上得分情况
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('sheet1')
header = ['评论','用户']
for h in range(len(header)):
    sheet.write(0,h,header[h])

# 改pageIndex 爬取不同页面
for index in range(1,2):
    base_url = 'https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList'
    payload = {
        "arg": {
            "channelType": 2,
            "collapseType": 0,
            "commentTagId": 0,
            "pageIndex": 32,
            "pageSize": 10,
            "poiId": 77071,
            "sourceType": 1,
            "sortType": 3,
            "starType": 0
        },
        "head": {
            "cid": "09031170210339221227",
            "ctok": "",
            "cver": "1.0",
            "lang": "01",
            "sid": "8888",
            "syscode": "09",
            "auth": "",
            "xsid": "",
            "extension": []
        }
    }
 
    response = requests.post(base_url, data=json.dumps(payload), headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    
    
    # 解析 JSON 数据
    data = json.loads(soup.text)
    # 获取 "content" 字段的内容
    comments = data.get("result", [])
    items = comments['items']
    
    
    i=(index-1)*10+1
    for item in items:
        comments = item['content']
        name = item['userInfo']['userNick']
        j=0
        sheet.write(i,j,comments)
        sheet.write(i,j+1,name)
        i = i+1
        
 
book.save('C:/Users/Cc/Desktop/评论.xls')    