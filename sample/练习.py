#!/usr/bin/env python
# -*- encoding: UTF-8 -*- 
"""
-----------------------------------------------
#@File        : 练习.py
#@ide         : PyCharm
#@E-mail      : jxwhp@163.com
#@Author      : jxwhp
#@Modify time : 2020-04-20:9:08 
-----------------------------------------------
"""
from bs4 import  BeautifulSoup
from lxml import etree
import requests
import bs4
import re

# url = 'http://seputu.com/'
# #url = 'https://www.biqugela.com/sort/1/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
# }
#
# def tag_has_gartet_no_id(tag):
#     return tag.has_attr('target') and not tag.has_attr('id')
#
#
# response = requests.get(url,headers).content.decode()
# #print(response)
# htmlCharset = 'utf-8'
# soup = BeautifulSoup(response,'lxml')
# soup.find_next_sibling()
# soup.f
# iterator = soup.select('body > div.body > div:nth-child(7) > div > div.box > ul > li:nth-child(13) > a')
# a =iterator[0]
# print(type(a))
# print(a)
# li = a.parent
# print(li)
# parent2 =li.find_parents('ul')
# print(type(parent2))
# print(parent2)
import cv2
import email

from email.mime.text import MIMEText

import smtplib

from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header

# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '17833871@qq.com'
password = ''

# 收信方邮箱
to_addr = '17833871@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText('send by python********吴海平', 'plain', 'utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('python test')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()
555555555