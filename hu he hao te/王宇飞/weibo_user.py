#-*- codeing = utf-8 -*-
#@Time : 2022/4/16 16:28
#Auther : 王小二
#@file : weibo_user.py
#@Software : PyCharm Community Edition
import urllib.request

import re

import pandas as pd

import numpy as np

import csv

import requests

import time

# 设置头部和cookie，反爬，伪装

header = {'Content-Type': 'text/html; charset=utf-8',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

Cookie = {
    'Cookie': 'XSRF-TOKEN=894db0; WEIBOCN_FROM=1110006030; MLOGIN=0; loginScene=102003; M_WEIBOCN_PARAMS=oid%3D4756412444445838%26luicode%3D20000061%26lfid%3D4756412444445838; SUB=_2A25PXkGJDeRhGeFL6VAZ8SjJzjuIHXVsoW_BrDV6PUJbkdANLXfzkW1NQkSBe50rAK_qy6ykib_UC-FbCScDdFkz'}

weibo_comment_df = pd.read_csv('weibo_comment3.csv', header=None, usecols=[1],encoding="utf_8_sig")

weibo_comments = weibo_comment_df.values.tolist()

print(len(weibo_comments))

for i in range(len(weibo_comments)):

    # print(type(weibo_comment[0]))

    url_base_1 = "http://weibo.cn/"

    url_base_2 = "/info"

    url = url_base_1 + str(weibo_comments[i][0]) + url_base_2

    print(i)

    print(url)

    try:

        html = requests.get(url, headers=header, cookies=Cookie)

        nickname = re.findall(r'<div class="c">昵称:(.*?)<br/>', html.text)

        #print(nickname)

        sex = re.findall(r'<br/>性别:(.*?)<br/>', html.text)

        #print(sex)

        location = re.findall(r'<br/>地区:(.*?)<br/>', html.text)
        location = sum(map(str.split, location), [])
        print(location)
        print(type(location[0]))

        if(len(location)==2):

            data1 = [(nickname[0], sex[0], location[0],location[1])]
        else:
            data1 = [(nickname[0], sex[0], location[0],'无')]

        data2 = pd.DataFrame(data1)

        data2.to_csv('weibo_user3.csv', header=False, index=False, mode='a+',encoding="utf_8_sig")

    except:

        print("something is wrong")

        data1 = [('wawa', '男', '呼和浩特')]

        data2 = pd.DataFrame(data1)

        data2.to_csv('weibo_user3.csv', header=False, index=False, mode='a+',encoding="utf_8_sig")

    time.sleep(1)



