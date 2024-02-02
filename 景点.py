# -*- coding: utf-8 -*-
# @Author  : Liyufei
# @Time    : 2023/2/9 16:21
# @File    : 景点.py
# @Software: PyCharm
import time

import requests
import json
import csv

postUrl = "https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList"

# 将景点poiId和名称添加到此处
urls = [['75682', '兵马俑']]

for id in urls:
    print("正在爬取景点：", id[1])
    # 通过返回值判断总评论数，每页9条，计算出总页数，对大于200页的数据只爬取200页
    data_pre = {
        "arg": {
            "channelType": 2,
            "collapseType": 0,
            "commentTagId": 0,
            "pageIndex": 1,
            "pageSize": 10,
            "poiId": id[0],
            "sourceType": 1,
            "sortType": 3,
            "starType": 0
        },
        "head": {
            "cid": "09031033316224110859",
            "ctok": "",
            "cver": "1.0",
            "lang": "01",
            "sid": "8888",
            "syscode": "09",
            "auth": "",
            "xsid": "",
            "extension": []
        }
    }

    html = requests.post(postUrl, data=json.dumps(data_pre)).text
    html = json.loads(html)

    # 确定总页数总页数
    total_page = int(html['result']['totalCount']) / 9
    # 遍历查询评论
    if total_page > 200:
        print("总页数大于200, 请输入你要爬取的页数：")
    else:
        print("总页数:", total_page, "请输入你要爬取的页数：")
    your_page = int(input())
    # 创建写入csv文件
    path = r'C:\Users\ASUS\Desktop\景区.csv'
    xuhao = 1
    with open(path, 'w', newline='', encoding='utf_8_sig') as f:
        file = csv.writer(f)
        file.writerow(['序号', '景区名称', '评论', '省份', "时间"])
        for page in range(1, your_page + 1):
            print("爬取第{}页".format(page))
            time.sleep(2.5)
            data = {
                "arg": {
                    "channelType": 2,
                    "collapseType": 0,
                    "commentTagId": 0,
                    "pageIndex": page,
                    "pageSize": 10,
                    "poiId": id[0],
                    "sourceType": 1,
                    "sortType": 3,
                    "starType": 0
                },
                "head": {
                    "cid": "09031027214030973865",
                    "ctok": "",
                    "cver": "1.0",
                    "lang": "01",
                    "sid": "8888",
                    "syscode": "09",
                    "auth": "",
                    "xsid": "",
                    "extension": []
                }
            }
            html = requests.post(postUrl, data=json.dumps(data)).text
            html = json.loads(html)
            # 获取评论
            for j in range(1, 10):
                result = html['result']['items'][j]['content']
                location = html['result']['items'][j]['ipLocatedName']
                datetime = html['result']['items'][j]['publishTypeTag']
                datetime = datetime[:10]
                file.writerow([xuhao, id[1], result, location, datetime])
                xuhao += 1
    print(id[1], "爬取完成")
