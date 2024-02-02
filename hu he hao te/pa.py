import requests
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
#创建一个浏览器对象
option=webdriver.EdgeOptions()
option.add_experimental_option("detach",True)
chrome=webdriver.Edge(options=option)
#打开网页首页
chrome.get("http://www.mafengwo.cn/gonglve/")
#网页搜索框
search_ele=chrome.find_element(By.ID,'_j_head_search_input')
#向搜索框中输入我们想查的城市
search_ele.send_keys(u'呼和浩特')
#按下搜索按钮
search_btn=chrome.find_element(By.CLASS_NAME,'icon-search')
search_btn.click()
#打开景点网站
search_btn1=chrome.find_element(By.LINK_TEXT,'查看更多相关旅行地>>').click()
#切换操作网站（切换为景点网站并关闭搜索网站）
chrome.close()
n=chrome.window_handles
chrome.switch_to.window(n[0])
#翻页
for i in range(1,20):

    #拖动滚动条
    time.sleep(1)
    #js="var q=document.documentElement.scrollTop=10000"
    #chrome.execute_script(js)
    #取数据
    items=chrome.find_elements(By.XPATH,"/html/body/div[2]/div[4]/div/div[1]/ul//a")
    for item in items:
        result=item.get_attribute("href")
        print(result)
        #f = open("景点网址1.txt", 'a', encoding='utf-8')  # 储存地址
        #f.write(str(result) + '\n')

    if chrome.find_element(By.LINK_TEXT,'后一页'):
        search_btn2=chrome.find_element(By.LINK_TEXT,'后一页')
        search_btn2.click()