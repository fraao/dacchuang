from snownlp import SnowNLP
import pymysql
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password= "1234",
    database= "USIP",
    charset= "utf8"
)
cur = conn.cursor()
try:
    sql = "select result from t_data"
    cur.execute(sql)
    datalist=[]
    ret=cur.fetchall()
    for s in ret:
        datalist.append(s[0])
    contents=''.join(datalist)
except Exception as e:
    print(e)
    conn.rollback()

cur.close()
conn.close()

# print(len(contents))

word = []

score = []


for content in contents:

    # print(content)

    try:
        s = SnowNLP(content[0])
        s1=round(s.sentiments,1)
        score.append(s1)


    except:

     print("something is wrong")

    score.append(0.5)

# print(len(score))

data2 = pd.DataFrame(score)
print(data2)

bar= data2.value_counts()
labels =list(bar.index)
print(bar)
zipp=zip(labels,bar.values)
sentiment_score=dict(zipp)
print(sentiment_score)
# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
z=list(sentiment_score.keys())
z1=[]
for i in z:
    z1.append(i[0])
print(z1)
# sns.barplot(x=list(sentiment_score.keys()),y=list(sentiment_score.values()))
sns.barplot(z1,y=list(sentiment_score.values()))
plt.xlabel('情感值')
plt.ylabel('频数')
plt.title('不同情感值下的频数柱形图')

# for x,y in zip(sentiment_score.keys(),sentiment_score.values()):
for x,y in zip(z1,sentiment_score.values()):
    plt.text(x*10,y+1,'%s'%y,ha='center',va='baseline',fontsize=12)
plt.show()