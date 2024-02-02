from telnetlib import EC

import requests
import json
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains

#创建一个浏览器对象
from selenium.webdriver.support.wait import WebDriverWait

option=webdriver.EdgeOptions()
option.add_experimental_option("detach",True)
option.add_argument("--disable-blink-features=AutomationControlled")#防止反爬
chrome=webdriver.Edge(options=option)
#with open('./stealth.min.js') as f:
#    js = f.read()

#chrome.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#    "source": js
#})
#打开网页
f=open("D:/pythonProject/hu he hao te/景点网址1.txt","r")
for line in f:
    chrome.maximize_window()
    chrome.get(line)
    #翻页
    for i in range(0,6):
            #拖动滚动条
            t = random.randint(1, 3)
            time.sleep(t)
            js1="window.scrollTo(0,100000)"
            chrome.execute_script(js1)
            #取数据
            items=chrome.find_elements(By.XPATH,"/html/body/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]//ul")
            for item in items:
                print(item.text)
                f = open("景点评论1.txt", 'a', encoding='utf-8')  # 储存地址
                f.write(str(item.text) + '\n')
            t1 = random.randint(1,3)
            time.sleep(t1)
            try:
                #自动翻页
                search_btn2 = chrome.find_element(By.LINK_TEXT, '后一页')
                chrome.execute_script("arguments[0].scrollIntoView(false);",search_btn2)#屏幕定位到按钮
                search_btn2.click()
            except:break

