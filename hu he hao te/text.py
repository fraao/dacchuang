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
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

Cookie = {
    'Cookie': 'SCF=ArfHZrR50j2dIBHthBCgbug0SIY3DMTR8lWwBE7L5h_AxWvZZNwPEgNuIV-dRfzB4P0p2UdMSSWWKKlO6EOxbxw.; _T_WM=15249726511; XSRF-TOKEN=5547b4; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174%26uicode%3D20000174; SUB=_2A25ytxhLDeRhGedO6lQW8CnLyT2IHXVuW7gDrDV6PUJbktANLW3HkW1NIq8YtjQqBefMW7ytgVZzz8UnUJyBy7FM; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWNV63Cm-IRnecWd5QD-d1Q5NHD95Qpeh2cS05NS0zpWs4Dqcj_i--fiKnfiKn4i--Xi-z4iKyFi--fi-ihiKnEi--ci-8hi-2pi--fiKnfiKn0; SSOLoginState=1605593115'}

# 评论翻页的关键字段

max_id = ""

# 设置循环

while True:

    # 评论第一页max_id为空值

    if max_id == "":

        url = "https://m.weibo.cn/comments/hotflow?id=4758466071888646&mid=4758466071888646&max_id_type=0"

    else:

        # 显示max_id

        print(max_id)

        # 评论后一页url中的max_id为前一页传递来的参数

        url = "https://m.weibo.cn/comments/hotflow?id=4758466071888646&mid=4758466071888646&max_id=" + str(
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

        data2.to_csv('weibo_comment.csv', header=False, index=False, mode='a+')

    # 休眠3秒，防止被系统认为是爬虫

    time.sleep(3)