import pandas as pd
from icecream import ic

# 读取文件
pd_data = pd.read_excel('E:/GoodGoodStudyDayDayUp/DayDayNoBug/StoreDistribution/全国.xlsx')

prov = pd_data['省份'].tolist()
prov_num = pd_data['数量'].tolist()

name = []
for i in prov:
    if "省" in i:
        name.append(i.replace('省', ''))
    elif '内蒙古自治区' in i:
        name.append(i.replace('自治区', ''))
    else:
        name.append(i[:2])
ic(name)
ic(prov)


# 接下来我们使用pyecharts来可视化我们清洗过后的数据
from pyecharts.charts import Map
from pyecharts import options as opts

map = (
    Map()
    .add("数量分布", [list(z) for z in zip(prov, prov_num)], "china")
    .set_global_opts(
    title_opts=opts.TitleOpts(title="霸王茶姬全国门店分布图"),
    visualmap_opts=opts.VisualMapOpts(max_=600, is_piecewise=True),
    )

  )
map.render('全国.shtml')
ic('全国分布图绘制完毕！')