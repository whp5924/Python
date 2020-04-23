#!/usr/bin/env python
# -*- encoding: UTF-8 -*- 
"""
-----------------------------------------------
#@File        : 微信发信息.py
#@ide         : PyCharm
#@E-mail      : jxwhp@163.com
#@Author      : jxwhp
#@Modify time : 2020-04-22:11:11 
-----------------------------------------------
"""
from wxpy import *
#encoding:utf-8
#QQ496631085 小和   此代码是固定给某个好友发消息
from threading import Timer
from wxpy import *
import requests

bot = Bot(console_qr=-1)#连接微信,会出现一个登陆微信的二维码
def get_news():
    '''获取金山词霸每日一句'''
    url = 'http://open.iciba.com/dsapi'
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content,note

def send_news():
    try:
        contents = get_news()

        my_friend =bot.friends().search(u'霜叶红于二月花')[0]#这里是搜索你微信好友里面的的昵称
        my_friend.send(contents[0])#给好友发送消息
        my_friend.send(contents[1])
        my_friend.send(u'^_^')

        # t = Timer(86400,send_news)#这里是一天发送一次，86400s = 24h
        # t.start()
        # friends=bot.friends()
        # print(friends)
        # for x in friends:
        #     print(x)

    except:
        my_friend = bot.friends().search('霜叶红于二月花')[0]#这里是你的微信昵称
        my_friend.send(u'今天消息发送失败了')


send_news()