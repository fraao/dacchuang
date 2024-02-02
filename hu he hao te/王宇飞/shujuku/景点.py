import csv
import os
import subprocess
import time
from time import sleep
import requests
from bs4 import BeautifulSoup
  
import 常用参数变量
from 常用参数变量 import headers, file_path
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent


def search_city_url(city, city_list):
    for row in city_list:
        if row['城市'] == city:
            return row['url']


proxy = 常用参数变量.get_random_proxy()


def get_scenic_info(div):
    a_tags = div.find_all("a", class_="guide-main-item")
    scenic_list = []
    # 获取该城市top6景点的名称和url
    for a_tag in a_tags:
        Scenic_href = a_tag["href"]
        Scenic_name = a_tag.find("p", class_="title").text
        scenic_list.append([Scenic_name, Scenic_href])
    return scenic_list

city = input("请输入要查询的城市名称：")
if __name__ == '__main__':
    start_time = time.time()
    city_list = []
    with open(r'.\csv数据\城市列表.csv', 'r', encoding='utf_8_sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            city_list.append(row)
    url = search_city_url(city, city_list)
    if url:
        print(f"{city}的URL为：{url}")
    else:
        print(f"未找到{city}的URL")
        exit(0)
    response = requests.get(url, headers=headers)
    # response = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.find_all("div", class_="guide-main")
    top6_file_path = file_path.format(city)
    # 将获取到的信息存入csv
    with open(top6_file_path, 'w', newline='', encoding='utf_8_sig') as f:
        file = csv.writer(f)
        file.writerow(['序号', '景点', 'url'])
        with ThreadPoolExecutor() as executor:
            scenic_list = sum(executor.map(get_scenic_info, divs), [])
            xuhao = 1
            for scenic in scenic_list:
                print("景区：{}，url：{}".format(scenic[0], scenic[1]))
                file.writerow([xuhao, scenic[0], scenic[1]])
                xuhao += 1
    print(f"{city}的景区信息已写入{top6_file_path}")
    end_time = time.time()
    print('程序耗时：', end_time - start_time, '秒')
    subprocess.run(["python", "景点poiId.py", str(city), str(url), str(top6_file_path)])