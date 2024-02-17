import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置字体
myfont = FontProperties(fname='C:/Windows/Fonts/simhei.ttf', size=12)

# 初始化数据
words = []
counts = []

# 读取数据并分割为单词和计数
with open('Parking lot Type.txt', encoding='utf-8') as f:
    for line in f:
        parts = line.strip('\n').split(': ')
        if len(parts) == 2:  # 确保分割得到了两个部分
            words.append(parts[0])
            counts.append(int(parts[1]))

# 按计数降序排序数据
sorted_data = sorted(zip(counts, words), reverse=True)
counts_sorted, words_sorted = zip(*sorted_data)

# 设定显示的条目数
N = 14

fig, ax = plt.subplots()

# 设置颜色
colors = ['#FA8072'] * N

# 绘制前N条数据
rects = ax.barh(words_sorted[:N], counts_sorted[:N], align='center', color=colors)

# 设置y轴标签
ax.set_yticklabels(words_sorted[:N], fontproperties=myfont)

# 反转y轴，从而使得数值最大的条目在上面
ax.invert_yaxis()

# 设置标题和x轴标签
ax.set_title('停车场类别', fontproperties=myfont, fontsize=17)
ax.set_xlabel(u"数量", fontproperties=myfont)

# 显示图表
plt.show()
