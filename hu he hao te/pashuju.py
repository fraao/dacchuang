# -*- codeing = utf-8 -*-（防止中文乱码）
# @Time : 2021/1/22 14:33（时间）
# @Auther : IGfraAo（用户名字）
# @File : 1.py（当前文件名）
# @Software: （软件名称）
import jieba
import bs4   #网页解析，获取数据
import re    #正则表达式，进行文字匹配
import urllib.request,urllib.error   #制定url，获取网页数据
import xlwt  #进行excel操作
import sqlite3 #进行sqlite数据库操作
from bs4 import BeautifulSoup
import pandas as pd

def main():
    baseurl = "https://www.mafengwo.cn/poi/6326821.html"
    #1.爬取网页
    getdata(baseurl)
    #2.频度分析
    #count()

#创建正则表达式对象，表示模板
findlink = re.compile(r'<a href="(.*?)">') #影片超链接的规则
findimgsrc = re.compile(r'<img.*src="(.*?)"',re.S) #影片图片的规则，re.S让换行符包含在字符中
findtitle = re.compile(r'<span class="title">(.*)</span>') #影片片名的规则
findrating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>') #影片评分的规则
findjudge = re.compile(r'<span>(\d*)人评价</span>') #评价人数的规则
findinq = re.compile(r'<span class="inq">(.*)</span>') #概况的规则
findbd = re.compile(r'<dd class="item-short">(.*?)<dd class="item-prac">',re.S) #影片相关内容的规则


#爬取网页
def getdata(baseurl):
    for i in range(1,445):#调用获取页面信息的函数10次
        url = baseurl + str(i) + str(".html")
        html= askURl(url)    #保存获取到的网页源码


        # 2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="iteminner"): #查找符合要求的字符串形成列表
            data = []  #保存一部电影的所有信息
            item=str(item)

            link = re.findall(findbd,item)[0]  #re库用来通过正则表达式查找指定的字符串
            link = link.replace("......</dd>","")
            link = link.replace("\n", "") #清除换行符
            link = link.replace("\u3000","")
            link = link.replace("，", "")
            link = link.replace("。", "")
            link = link.replace("！", "")
            link = link.replace("+", "")
            link = link.replace("‘", "")
            link = link.replace("：", "")
            link = link.replace("“", "")
            link = link.replace("？", "")
            link = link.replace("·", "")
            link = link.replace("-", "")
            link = link.replace("~", "")
            link = link.replace("《", "")
            link = link.replace("》", "")
            link = link.replace("、", "")
            link = link.replace("…", "")
            link = link.replace("[", "")
            link = link.replace("]", "")
            link = link.replace("🔺", "")
            link = link.replace("｜", "")
            link = link.replace("------", "")
            link = link.replace("★", "")
            link = link.replace(".....", "")
            link = link.replace("=", "")
            f = open("武汉旅游评价.txt", 'a', encoding='utf-8')  # 储存地址
            f.write(str(link))
        print(i)  # 获取影片超链接



#得到一个指定一个URL的网页内容
def askURl(url):
    #用户代理表示告诉豆瓣服务器，我们是什么类型的浏览器（本质是告诉浏览器，我们可以接受什么水平的文件内容）
    #模拟浏览器头部信息，向豆瓣服务器发送消息
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"}
    request =urllib.request.Request(url,headers=head)
    html =""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr((e,"reason")):
            print(e.reason)
    print(html)
    return html

def count():

    content =open("武汉旅游评价.txt",'r',encoding='utf-8').read()
    seg_list = jieba.cut(content)  # jieba分词，默认是精确模式
    liststr = "/".join(seg_list)
    count_dict = {}
    for ite in liststr.split('/'):
        if ite in count_dict:
            count_dict[ite] += 1
        else:
            count_dict[ite] = 1  # Counter({‘Dog’: 3, 42: 2, ‘Cat’: 2, ‘Mouse’: 1}
    q = open(r'分词频数.txt','w',encoding='utf-8')  # 储存地址
    q.write(str(count_dict))
    p = pd.DataFrame.from_dict(dict(count_dict), orient='index')#保存词频数据到csv
    p.to_csv('最终词频表.csv', encoding='utf-8')

if __name__ =="__main__":#当程序执行时
#     调用函数
     main()