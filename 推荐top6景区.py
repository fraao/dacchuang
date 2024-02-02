# -*- coding: utf-8 -*-
# @Author  : Liyufei
# @Time    : 2023/2/10 20:54
# @File    : 推荐top5景区.py
# @Software: PyCharm
import csv
from time import sleep
import requests
from bs4 import BeautifulSoup
from 常用参数变量 import headers


def search_city_url(city):
    with open(r'.\csv数据\城市列表.csv', 'r', encoding='utf_8_sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['城市'] == city:
                return row['url']


if __name__ == '__main__':

    city = input("请输入要查询的城市名称：")
    url = search_city_url(city)
    if url:
        print(f"{city}的URL为：{url}")
    else:
        print(f"未找到{city}的URL")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.find_all("div", class_="guide-main")
    path = r'.\csv数据\{}top6景区.csv'.format(city)
    xuhao = 1
    with open(path, 'w', newline='', encoding='utf_8_sig') as f:
        file = csv.writer(f)
        file.writerow(['序号', '景点', 'url'])
        for div in divs:
            a_tags = div.find_all("a", class_="guide-main-item")
            for a_tag in a_tags:
                Scenic_href = a_tag["href"]
                Scenic_name = a_tag.find("p", class_="title").text
                print("href:", Scenic_href)
                print("景区:", Scenic_name)
                file.writerow([xuhao, Scenic_name, Scenic_href])
                xuhao += 1
