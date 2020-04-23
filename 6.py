#!/usr/bin/env python
# -*- encoding: UTF-8 -*- 
"""
-----------------------------------------------
#@File        : 6.py
#@ide         : PyCharm
#@E-mail      : jxwhp@163.com
#@Author      : jxwhp
#@Version     : Administrator  
#@Modify time : 2020-04-18:15:07 
-----------------------------------------------
"""
import requests
from lxml import etree

url = 'https://club.autohome.com.cn/bbs/thread/665330b6c7146767/80787515-1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

response = requests.get(url,headers=headers)
print(response)
res_html = response.text
print(res_html)
dom = etree.HTML(res_html)