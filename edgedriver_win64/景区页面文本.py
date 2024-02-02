# -*- coding: utf-8 -*-
# @Author  : Liyufei
# @Time    : 2023/2/10 22:32
# @File    : 景区页面文本.py
# @Software: PyCharm
import csv
from time import sleep
import requests
from bs4 import BeautifulSoup
from 常用参数变量 import headers

url = 'https://you.ctrip.com/sight/xian7/1444.html'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
the_text=soup.find("div", class_="detailModuleRef")
print(the_text)

