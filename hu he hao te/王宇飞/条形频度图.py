import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



from snownlp import SnowNLP

from snownlp import sentiment

import matplotlib.pyplot as plt

from pyecharts import Map

# 读取csv文件
df = pd.read_csv('weibo_user3.csv',encoding="GBK")
grouped = df.groupby('location').describe().reset_index()

use_location = grouped['location'].values.tolist()

print(len(use_location))

print(use_location)

sentiment_average = df.groupby('location')['score'].mean()

sentiment_scores = sentiment_average.values

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#数据可视化
sns.barplot(x=list(sentiment_average.values),y=use_location)
plt.xlabel('情感值')
plt.ylabel('主题')
plt.title('不同主题下的情感得分柱形图')
for x,y in enumerate(list(sentiment_average.values)):
    plt.text(y,x,'%s'%y,va='center')
plt.show()