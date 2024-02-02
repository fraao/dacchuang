import requests
from bs4 import BeautifulSoup

# 设置网页的url
url = 'https://you.ctrip.com/sight/xian7/1444.html'
data = {
    "arg": {
        "channelType": 2,
        "collapseType": 0,
        "commentTagId": 0,
        "pageIndex": 0,
        "pageSize": 10,
        "poiId": 75682,
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
pages = 10
# 获取网页的源代码
res = requests.get(url)
html = res.text

# 使用BeautifulSoup解析网页
soup = BeautifulSoup(html, 'html.parser')
for page in range(1, pages):
    print("爬取第{}页".format(page))
    # 获取评论内容和评论时间

    comments = soup.find_all("div", class_="commentTime")
    print(comments)
    # times = soup.find_all("span", class_="time")
    #
    # # 遍历评论内容和评论时间
    # for comment, time in zip(comments, times):
    #     print("Comment:", comment.text)
    #     print("Time:", time.text)
