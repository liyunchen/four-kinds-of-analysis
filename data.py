# -*- coding: utf-8 -*-


"""
李运辰 2021-3-24

公众号：python爬虫数据分析挖掘
"""


import requests
from lxml import etree
from bs4 import BeautifulSoup
import json
import time
import re
headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
        }

def xpath():
    url="http://www.xbiquge.la/xuanhuanxiaoshuo/"
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    text = res.text

    selector = etree.HTML(text)
    list = selector.xpath('//*[@class="l"]/ul/li')

    for i in list:
        title = i.xpath('.//span/a/text()')
        href = i.xpath('.//span/a/@href')
        print(title)
        print(href)
        print("--------")

    print(len(list))

def bs4():
    url="http://www.xbiquge.la/xuanhuanxiaoshuo/"
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    text = res.text



    # 创建一个BeautifulSoup解析对象
    soup = BeautifulSoup(text,'html.parser')

    ###法一
    # list = soup.find_all(attrs={'class':'s2'})
    # for i in list:
    #     print(i.a.get_text())
    #     print(i.a.get("href"))
    #     print("--------")
    # print(len(list))

    ####法二
    # 获取所有的链接
    all_link = [(link.a['href'], link.a.get_text()) for link in soup.find_all('li')]
    for i in all_link:
       print(i)

def jsondata():
    ip = "123.123.123.123"
    url="https://restapi.amap.com/v3/ip?key=0113a13c88697dcea6a445584d535837&ip="+str(ip)
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'

    text = res.text
    print(text)
    ##text不是json类型的话，则转为json类型
    text = json.loads(text)
    print("省份="+text['province']+",城市="+text['city'])

def redata():
    url="http://www.xbiquge.la/xuanhuanxiaoshuo/"
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    text = res.text

    pattern = re.compile('《.*?》')
    items = re.findall(pattern, text)

    for i in items:
        print(i)


redata()








