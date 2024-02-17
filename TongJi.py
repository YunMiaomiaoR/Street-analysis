import csv
from collections import Counter

# 假设表格文件名为'words_table.csv'，并且每行只有一个由分号分隔的单元格
filename = 'ServiceType.csv'

# 创建一个Counter对象来直接统计词频
word_counter = Counter()

# 打开文件并读取内容
with open(filename, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        # 假设每行只有一个单元格
        cells = row[0]
        # 使用分号分割单元格中的词汇
        words = cells.split(';')
        # 更新词频计数器
        word_counter.update(words)

# 打印词频统计结果
for word, freq in word_counter.items():
    print(f"{word}: {freq}")
