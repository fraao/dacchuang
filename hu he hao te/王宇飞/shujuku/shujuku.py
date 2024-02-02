import time
import requests
from lxml import etree
from multiprocessing.dummy import Pool
from requests.exceptions import RequestException
import openpyxl
import re
from fake_useragent import UserAgent
import pymysql
import traceback



def database_connect(do_what: str, sql: str, *args) -> tuple:
    is_success = True
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='1234',
                           database='usip')
    cursor = conn.cursor()
    data = 'ok'
    try:
        if do_what == 'in' or do_what == 'upd' or do_what == 'del':
            cursor.execute(sql, args)
            conn.commit()
        elif do_what == 'out':  # 向数据库读出图片做网页端呈现用
            cursor.execute(sql, args)
            data = cursor.fetchall()
    except Exception as e:
        is_success = False  # 有异常,返回False
        traceback.print_exc()  # 追踪错误信息
        data = 'false'
    finally:
        cursor.close()
        conn.close()
    return is_success, data


def get_one_page(url):
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    # 构造HTML解析器
    info_list = []
    ii_list = html.xpath('//a[@class="journal-item cf"]')
    for ii in ii_list:
        ##提取
        # 客源地
        title = ii.xpath('.//dt[@class="ellipsis"]/text()')[0].strip()
        di_li = ii.xpath('.//span[@class="tips_a"]/text()')[0].strip().split(
            '\n                                        ')
        try:
            day = di_li[0]
            # 出游时间（月份）
            time = di_li[1]
            # 出行同伴（家人、朋友或其他）
            people = di_li[3].replace('，', '')
            # 人均消费
            money = di_li[2].replace('，', '')
        except Exception:
            day = ''
            time = ''
            people = ''
            money = ''
        # print(day,time,people,money)
        # 用户名
        user1 = ii.xpath('.//dd[@class="item-user"]/text()')[0].strip()
        user = re.findall(r"(.+?)发表于", user1)[0].strip()
        fa = user1[user1.rfind('发表于'):].replace('发表于 ', '')
        # print(user)

        url = 'https://you.ctrip.com' + ii.xpath('./@href')[0].strip()
        headers = {
            'cookie': '_ga=GA1.2.50538359.1626942417; MKT_CKID=1626942416972.xsrkp.h14a; _RSG=vt4axMVXju2TUp4mgpTnUB; _RDG=28416d30204f5527dc27cd978da9f4f9ba; _RGUID=2e2d85f5-bb90-4df9-b7b1-773ab013379d; GUID=09031042315856507136; nfes_isSupportWebP=1; nfes_isSupportWebP=1; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; _gid=GA1.2.607075386.1635573932; MKT_Pagesource=PC; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&createtime=1635573932&Expires=1636178732460; MKT_CKID_LMT=1635573932634; _RF1=113.204.171.221; ASP.NET_SessionSvc=MTAuNjAuNDkuOTJ8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTYyMzE0MzgyNjI2MA; _bfa=1.1626942411832.2cm51p.1.1635573925821.1635580203950.4.26; _bfs=1.2; _jzqco=%7C%7C%7C%7C%7C1.429931237.1626942416968.1635580207564.1635580446965.1635580207564.1635580446965.0.0.0.19.19; __zpspc=9.4.1635580207.1635580446.2%232%7Cwww.baidu.com%7C%7C%7C%7C%23; appFloatCnt=7; _bfi=p1%3D290602%26p2%3D0%26v1%3D26%26v2%3D25',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          + 'Chrome/62.0.3202.94 Safari/537.36'}
        hji2 = get_one_page(url)
        hji2 = etree.HTML(hji2)
        quanwen = hji2.xpath('//div[@class="ctd_content"]')
        try:
            quanwen = quanwen[0].xpath('string(.)').strip().replace('\\n', '')
        except Exception:
            quanwen = ''
        pattern = "[\u4e00-\u9fa5]+"
        regex = re.compile(pattern)
        results = ','.join(regex.findall(quanwen))

        cai = hji2.xpath('//div[@class="ctd_content_controls cf"]')
        try:
            result = cai[0].xpath('string(.)').strip().replace('\\n', '').replace('\r\n', '')
        except Exception:
            result = ''
        # print(result)
        if '天数' in result:
            n = re.findall(r"天数：(.+?)天", result[result.rfind('天数'):])[0].strip() + '天'
            # print(n)
        else:
            n = ''
        if '时间' in result:
            m = re.findall(r"时间：(.+?)月", result[result.rfind('时间'):])[0].strip() + '月'
            # print(m)
        else:
            m = ''
        if '人均' in result:
            ren1111 = re.findall(r"人均：(.+?)元", result[result.rfind('人均'):])[0].strip() + '元'
            # print(k)
        else:
            ren1111 = ''
        if '和谁' in result:
            c = result[result.rfind('和谁'):][3:6]
            # print(c)
        else:
            c = ''
        if '玩法' in result:
            try:
                a = re.findall(r"玩法：(.+?)作者去了这些地方", result[result.rfind('玩法'):])[0].strip()
            # print(a)
            except Exception:
                a = ''
        else:
            a = ''
        if '作者去了这些地方' in result:
            b = result[result.rfind('作者去了这些地方'):].replace(
                '                                                                                                     ',
                '、')
            b = b.replace('、、  ', ',')
            b = b.replace('、', '')
            b = b.replace('作者去了这些地方：', '')
            # print(b)
        else:
            b = ''
        print(title, day, time, people, money, results)
        database_connect('in', 'insert into t_data values (null, %s, %s, %s, %s, %s, %s)', title, day, time, people,
                         money, results)


def main(offset):
    # 构造主函数，初始化各个模块，传入入口URL
    base_url = 'https://you.ctrip.com/travels/tianjin154/t2-p{}.html'
    print(offset)
    url = base_url.format(offset)
    html = etree.HTML(get_one_page(url))
    parse_one_page(html)


if __name__ == '__main__':
    wb = openpyxl.Workbook()  # 获取工作簿对象
    sheet = wb.active  # 活动的工作表
    # 添加列名
    global ren1111
    #     sheet.append(['发表于','用户名', '标题', '出游天数','天数','具体时间','出游时间（月份）',\
    #                   '出行同伴','和谁','人均消费','人均','玩法','作者去了这些地方','链接','全文'])
    # 请求头
    headers = {'User-Agent': UserAgent(verify_ssl=False).random}
    # 使用线程池
    print('多线程爬取开始')
    start_time = time.time()
    p = Pool(8)
    p.map(main, [i for i in range(1, 5)])
    # 保存位置
    # 关闭线程池
    end_time = time.time()
    print('多线程爬取结束')
    print('耗时:', end_time - start_time)
    p.close()
    p.join()  # 用来等待进程池中的worker进程执行完毕，防止主进程在worker进程结束前结束。
