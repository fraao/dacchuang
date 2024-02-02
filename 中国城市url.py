# -*- coding: utf-8 -*-
# @Author  : Liyufei
# @Time    : 2023/2/7 23:07
# @File    : 一小段.py
# @Software: PyCharm
import csv
from time import sleep
import requests
from bs4 import BeautifulSoup
from 常用参数变量 import headers

# a = "https://you.ctrip.com/countrysightlist/china110000/p1.html"
# response = requests.get(a, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")
# numpage = soup.find(class_="numpage").text
# print(numpage)
path = r'.\csv数据\城市列表.csv'
xuhao = 1
with open(path, 'w', newline='', encoding='utf_8_sig') as f:
    file = csv.writer(f)
    file.writerow(['序号', '城市', 'url'])
    for i in range(1, 215):
        url = "https://you.ctrip.com/countrysightlist/china110000/p{}.html".format(i)
        #print(url)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("div", class_="cityimg"):
            city_a = link.find("a")
            city_href = city_a["href"]
            city_href = 'https://you.ctrip.com' + city_href
            city_name = link.find("span").text
            print("city: ", city_name)
            print("href: ", city_href)
            file.writerow([xuhao, city_name, city_href])
            xuhao += 1
        sleep(1)
