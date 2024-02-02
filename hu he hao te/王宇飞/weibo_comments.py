#-*- codeing = utf-8 -*-
#@Time : 2022/4/15 23:14
#Auther : 王小二
#@file : weibo_comments.py
#@Software : PyCharm Community Edition
# encoding=gbk



import requests

import pandas as pd

import json

import time

import re

# 设置头部和cookie，反爬，伪装

header = {'Content-Type': 'application/json; charset=utf-8',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

Cookie = {
    'Cookie': 'XSRF-TOKEN=894db0; WEIBOCN_FROM=1110006030; MLOGIN=0; loginScene=102003; M_WEIBOCN_PARAMS=oid%3D4756412444445838%26luicode%3D20000061%26lfid%3D4756412444445838; SUB=_2A25PXkGJDeRhGeFL6VAZ8SjJzjuIHXVsoW_BrDV6PUJbkdANLXfzkW1NQkSBe50rAK_qy6ykib_UC-FbCScDdFkz'}

# 评论翻页的关键字段

max_id = ""

# 设置循环

while True:

    # 评论第一页max_id为空值

    if max_id == "":

        url = "https://m.weibo.cn/comments/hotflow?id=4756412444445838&mid=4756412444445838&max_id_type=0"

    else:

        # 显示max_id

        print(max_id)

        # 评论后一页url中的max_id为前一页传递来的参数

        url = "https://m.weibo.cn/comments/hotflow?id=4756412444445838&mid=4756412444445838&max_id=" + str(
            max_id) + "&max_id_type=" + str(max_id_type)

    print("请求的url是：" + url)

    # request对象获取

    response = requests.get(url, headers=header, cookies=Cookie)

    # json格式解析

    comment = response.json()

    print("requestion请求状态:" + str(comment['ok']))

    # 如果Ok值为1，表示解析成功

    if comment['ok'] == 0:
        break

    # 获取max_id值

    max_id = comment["data"]["max_id"]

    max_id_type = comment["data"]["max_id_type"]

    print("max_id is:" + str(max_id))

    print("max_id_type is:" + str(comment["data"]["max_id_type"]))

    # 获取评论文本，并过滤符号和英文字符

    for comment_data in comment["data"]["data"]:
        data = comment_data["text"]

        p = re.compile(r'(<span.*>.*</span>)*(<a.*>.*</ a>)?')

        data = re.sub('[^\u4e00-\u9fa5]', '', data)

        data = p.sub(r'', data)

        data1 = [(comment_data['created_at'], comment_data['user']['id'], comment_data['user']['screen_name'], data)]

        data2 = pd.DataFrame(data1)

        data2.to_csv('weibo_comment3.csv', header=False, index=False, mode='a+',encoding="utf_8_sig")
    # 休眠3秒，防止被系统认为是爬虫

    time.sleep(3)





