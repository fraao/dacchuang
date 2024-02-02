# -*- coding: utf-8 -*-
# @Author  : Liyufei
# @Time    : 2023/2/9 10:28
# @File    : 浏览器模拟搜索.py
# @Software: PyCharm
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

headers = {
    'cookie': 'MKT_CKID=1675507100586.ubspf.zn51; GUID=09031033316224110859; _RSG=2EaTFOI2aN5fxwfyUDAtZ9; '
              '_RDG=283aa4bcf3fbb329a7088bc860a54060ce; _RGUID=55e40926-0f76-4382-98f7-28d7bca7aee9; '
              '_bfaStatusPVSend=1; MKT_Pagesource=PC; nfes_isSupportWebP=1; nfes_isSupportWebP=1; ibulanguage=CN; '
              'ibulocale=zh_cn; cookiePricesDisplayed=CNY; StartCity_Pkg=PkgStartCity=53; '
              'MKT_OrderClick=ASID=5376167068&AID=5376&CSID=167068&OUID=&CT=1675853368560&CURL=https%3A%2F%2Fhotels'
              '.ctrip.com%2F%3Fsid%3D167068%26allianceid%3D5376%26qh_keywordid%3D3567088741%26qh_creative'
              '%3D6988114878%26qh_planid%3D1824762770%26qh_unitid%3D1019297454%26qh_device%3Dpc%26qhclickid'
              '%3D2529269fd62eef52%26keywordid%3D3567088741&VAL={}; MKT_CKID_LMT=1675853368624; '
              'Session=smartlinkcode=U1535&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; '
              'Union=AllianceID=1315&SID=1535&OUID=&createtime=1675860560&Expires=1676465359582; '
              'cticket=936CD65EA865284B8DFC4CE6DA7F086A7A47C6926E2E99126A93A9075A98491F; '
              'AHeadUserInfo=VipGrade=5&VipGradeName=%B0%D7%D2%F8%B9%F3%B1%F6&UserName=&NoReadMessageCount=0; '
              'DUID=u=4B4737687F8777006A20173EF865DC77&v=0; IsNonUser=F; UUID=77CDB71F2293404DA85A6F7AD1D3ED5B; '
              'IsPersonalizedLogin=F; intl_ht1=h4=103_1303880; Hm_lvt_e4211314613fcf074540918eb10eeecb=1675669796,'
              '1675762547,1675853386,1675919071; '
              'ASP.NET_SessionSvc=MTAuNjEuMjIuMjUwfDkwOTB8amlucWlhb3xkZWZhdWx0fDE2Mzg0MzIzMDI2NjI; _RF1=39.155.7.189; '
              '_bfi=p1%3D290570%26p2%3D290570%26v1%3D189%26v2%3D188; '
              'Hm_lpvt_e4211314613fcf074540918eb10eeecb=1675928021; '
              '_bfa=1.1675507100422.23movx.1.1675918996531.1675926055287.6.190.1; _bfs=1.26; '
              '_ubtstatus=%7B%22vid%22%3A%221675507100422.23movx%22%2C%22sid%22%3A6%2C%22pvid%22%3A190%2C%22pid%22'
              '%3A290570%7D; _jzqco=%7C%7C%7C%7C1675853369108%7C1.870967532.1675507100598.1675928014671.1675928022700'
              '.1675928014671.1675928022700.undefined.0.0.155.155; '
              '__zpspc=9.6.1675926056.1675928022.22%233%7Ccn.bing.com%7C%7C%7C%7C%23; _bfaStatus=send; '
              '_pd=%7B%22_o%22%3A30%2C%22s%22%3A903%2C%22_s%22%3A36%7D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  + 'Chrome/62.0.3202.94 Safari/537.36'}
if __name__ == '__main__':
    # 模拟浏览器去搜索
    # the_name = input("请输入你想搜索的城市：")
    url = 'https://you.ctrip.com/sight/xian7/1444.html'
    res = requests.get(url, headers=headers)
    html = res.text
    for i in range(0, 5):
        driver = webdriver.Edge(r'.\edgedriver_win64\msedgedriver.exe')  # Edge浏览器驱动
        driver.get(url)  # 网址
        soup = BeautifulSoup(html, 'html.parser')
        # comments = soup.find_all("div", class_="commentTime")
        # print(comments)
        commentDetail = comments = soup.find_all("div", class_="commentDetail")
        print(commentDetail)
        driver.find_element_by_partial_link_text("下一页").click()
        sleep(2)
    # driver.find_element_by_id('_allSearchKeyword').send_keys(the_name)  # 按照输入的书名搜索
    # driver.find_element_by_id('search_button_global').click()
    # driver.find_element_by_partial_link_text(the_name).click()
    # driver.switch_to.window(driver.window_handles[-1])  # 切换到最后一个页面
    # url = driver.current_url  # 获取最佳匹配的url
    # print(url)
    # driver.quit()
