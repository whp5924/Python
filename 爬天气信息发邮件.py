#!/usr/bin/env python
# -*- encoding: UTF-8 -*- 
"""
#@File        : 爬天气信息发邮件.py       
#@ide         : PyCharm
#@E-mail      : jxwhp@163.com
#@Modify time : 2020-04-22:17:56 
-------------------------------------------------
"""
import requests
import json

def crawl_msg():


    url = 'https://free-api.heweather.net/s6/weather/now?location=zhongshan&key=fe119fda4d46475795ebabaf6a43700a'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    print(url)
    response = requests.get(url,headers).text
    #print(response)
    dict = json.loads(response)['HeWeather6'][0]
    print(len(dict))
    # print(dict)
    add = dict['basic']
    wether = dict['now']
    print(add)
    print(wether)
    stat = ''
    stat += "省份：{}\n".format(add['admin_area'])
    stat += "城市：{}\n".format(add['parent_city'])
    stat += "温度：{}\n".format(wether['fl'])
    stat += "风向：{}\n".format(wether['wind_dir'])
    return stat

if __name__=="__main__":
    crawl_msg()
    send_wether()