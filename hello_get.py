#!/usr/bin/python
# -*- coding: UTF-8 -*-

# # filename：testpy.py
#
# # CGI处理模块
# import cgi, cgitb
#
# # 创建 FieldStorage 的实例化
# form = cgi.FieldStorage()
#
# # 获取数据
# site_name = form.getvalue('name')
# site_url = form.getvalue('url')
#
# print
# "Content-type:text/html"
# print
# print
# "<html>"
# print
# "<head>"
# print
# "<meta charset=\"utf-8\">"
# print
# "<title>表单提交 CGI 测试实例</title>"
# print
# "</head>"
# print
# "<body>"
# print
# "<h2>%s官网：%s</h2>" % (site_name, site_url)
# print
# "</body>"
# print
# "</html>"
#! c:\python\python.exe

import time
def printHeader(title):
    print("""Content-type: text/html
        <?xml version="1.0" encoding= "UTP-8"?>
        <!DOCTYPE html PUBLIC
          "DTD/xhtml=strict.dtd">
        <html xmlns="http://www.3w.org/2009/xhtml">
        <head><title>%s</title></head>
        <body>""" % title)

printHeader("Current date and time")
print(time.ctime(time.time()))
print("</body></html>")
