
# 0. 框架
import urllib.request
import urllib.parse
import re
import requests
import gzip
import time
import random

# 1. url

domain='https://www.biqugela.com/book_30324/'
domain1='https://www.biqugela.com/book_30324/25625845.html'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

def getList(url):
    # request=urllib.request.Request(url)
    # request.headers=headers
    # res=urllib.request.urlopen(request)
    # html = gzip.decompress(res.read())
    # html=html.decode('utf-8')
    html=requests.get(url,headers=headers).content.decode()
    reg1=r'<a href="/book_30324/(.*?).html">'
    reg=re.compile(reg1)
    #regg=reg.findall((html))[13:1283]   #13:1283
    return reg.findall(html)

def getNovelContent(url):
    # request=urllib.request.Request(url)
    # request.headers=headers
    # res=urllib.request.urlopen(request)
    # html=gzip.decompress(res.read())
    # html=html.decode("utf-8")
    html=requests.get(url,headers=headers).content.decode()
    reg = '<p.*?class="content_detail">([\^\s\S]*?)</p>'

    #reg = r'<p.*?class="content_detail">([\^\s\S]*?)</p>'  #.不能识别换行,可以加[\s\S] \S匹配任何空白字符，包括空格、制表符、换页符等等
    #reg='<a.*?title="(.*?))">'                                                      # \S 匹配任何非空白字符
    #< p

    # class ="content_detail" >
    #
    # 豪华的萧家别墅，一片灯火通明。
    # < / p >

    reg=re.compile(reg)
    regg=reg.findall(html)
    print(regg)
    return reg.findall(html)

if __name__=="__main__":
    for url in getList(domain)[13:14]:
        main=domain+url+'.html'
        print(main)
        text=getNovelContent(main)
        #print(text)
        # print(text[1:])
        for i in range(len(text)):
            f=open('./pic/上门女婿.txt','a+',encoding='utf-8')
            tt=text[i].replace('\n','').replace(' ','')
            f.write(text[i].replace('\n','').replace(' ','')+'\n')
        print(text[0] + '\t下载完成')
            #time.sleep(random.choice([0.5, 1, 1.5, 2]))

