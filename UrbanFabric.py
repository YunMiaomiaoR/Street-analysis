# 导入库
import osmnx as ox
from IPython.display import Image
# %matplotlib inline

# 可选，储存图片路径
img_folder = "images"
extension = "png"
size = 480 #图片长宽大小

# 定义函数
def make_plot(place,point,
              network_type="drive",
              dpi=80,dist=1000,default_width=4,
              street_widths=2): # dists 填入米
    tags = {"building": True}
    fp = f"./{img_folder}/{place}.{extension}" # 图片的地址保存
    gdf = ox.geometries_from_point(point, tags, dist=dist)
    fig, ax = ox.plot_figure_ground(
        point=point,
        dist=dist,
        network_type=network_type,
        default_width=default_width,
        street_widths=street_widths,
        save=False,
        show=False,
        close=True,
    )
    fig, ax = ox.plot_footprints(
        gdf, ax=ax, filepath=fp, dpi=dpi, save=True, show=False, close=True
    )
    return Image(fp, height=size, width=size)
  
 #执行函数
place = "Central Street"
point = (45.77368274116403, 126.61884688369749) # 填入wgs1984坐标  上海31.238850562378246, 121.48578354186554
make_plot(place, point,network_type="all", default_width=2, street_widths={"primary": 6})
