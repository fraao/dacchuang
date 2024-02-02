import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



from snownlp import SnowNLP

from snownlp import sentiment

import matplotlib.pyplot as plt

from pyecharts import Map

# 读取csv文件
df = pd.read_csv('weibo_user3.csv',encoding="UTF-8")


#获绘制不同情感值的柱形图
bar= df['score'].value_counts()
labels =list(bar.index)
print(bar)
zipp=zip(labels,bar.values)
sentiment_score=dict(zipp)
print(sentiment_score)

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# x=bar.values
sns.barplot(x=list(sentiment_score.keys()),y=list(sentiment_score.values()))
plt.xlabel('情感值')
plt.ylabel('频数')
plt.title('不同情感值下的频数柱形图')

for x,y in zip(sentiment_score.keys(),sentiment_score.values()):
    plt.text(x*10,y+1,'%s'%y,ha='center',va='baseline',fontsize=12)
plt.show()