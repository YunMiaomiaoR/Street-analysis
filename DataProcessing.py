import jieba
import pandas as pd
txt = open("Comment.csv", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
words

# 将词和对应出现的次数统计出来
wordsDict = {} #新建字典用于储存词及词频
for word in words:
    if len(word) == 1: #单个的字符不作为词放入字典
        continue
    else:
        wordsDict.setdefault(word, 0) #设置词的初始出现次数为0
        wordsDict[word] +=1 #对于重复出现的词，每出现一次，次数增加1
        
wordsDict_seq = sorted(wordsDict.items(),key=lambda x:x[1], reverse=True) #按字典的值降序排序
wordsDict_seq[:15] 

# 把意义不大的词删除
stopWords = ["这里", "可以", "地方", "一条", "还有", "就是", "一个", "一定", "我们", "一下", "还是","一样", "之一", "位于", "100", "1900"]
for word in stopWords:
    if word in wordsDict:
        del wordsDict[word] #删除对应的词
        
wordsDict_seq = sorted(wordsDict.items(),key=lambda x:x[1], reverse=True) #按字典的值降序排序
wordsDict_seq[:15] 

# 将数据转换成DataFrame，并增加列名“词”和“次数”，然后导出为Excel文件。
df = pd.DataFrame(wordsDict_seq,columns=['词','次数'])
df.to_excel("词频.xlsx",index = False) #存为Excel时去掉index索引列
df.head(10)