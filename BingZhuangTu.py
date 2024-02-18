import pandas as pd
from pyecharts import options as opts  
from pyecharts.charts import Pie  

# 读取Excel文件
df = pd.read_excel('C:/Users/Cc/Desktop/IP统计.xlsx')

# 假设Excel文件中有两列，一列是分类（'Category'），一列是值（'Value'）
data = df[['省份', '数量']].values.tolist()

# 创建饼图
c = (
    Pie()
    .add(
        series_name="",  # 系列名称
        data_pair=data,  # 数据（分类和值的列表）
        radius=["40%", "60%"],  # 饼图的内半径和外半径
        label_opts=opts.LabelOpts(
            position="outside",
            # {a}是系列名，{b}是数据项名称，{c}是数据项值，{d}是百分比
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    .set_global_opts(
        # 设置标题和位置
        title_opts=opts.TitleOpts(title="", pos_top='10%'),
        # 设置图例位置
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="5%", pos_left="1%"),
        )
    .render("pie_rich_label.html")
)

# 注意：确保Excel文件中的列名是'Category'和'Value'，或者修改代码中的列名以匹配你的Excel文件。
