#-*- codeing = utf-8 -*-
#@Time : 2022/4/15 23:04
#Auther : 王小二
#@file : sentiment_analysis.py
#@Software : PyCharm Community Edition
import pandas as pd

from snownlp import SnowNLP

from snownlp import sentiment

import matplotlib.pyplot as plt



#读取抓取的csv文件，标题在第3列，序号为2

df=pd.read_csv('weibo_comment3.csv',usecols=[3],encoding="utf-8")



#将dataframe转换为list

contents=df.values.tolist()

print(len(contents))

word=[]

score=[]

score1=[]

for content in contents:

	print(content)

	try:

		s=SnowNLP(content[0])

		score.append(round(s.sentiments,1))
		score1.append(s.sentiments)

	except:

		print("something is wrong")

		score.append(0.5)

print(len(score))

data2 = pd.DataFrame(score)

# data2.to_csv('sentiment.csv', header=False, index=False, mode='a+',encoding="utf_8_sig")