#

str_urllib_request="""
    1. request=urllib.request.Request(url)
    2. 可改变request.headers
    3. response=urllib.request.urlopen()
    4. html=response.read()
    5. html=html.gzip.decompress(html)
    6. html=html.decode()
    7. 输出
    
    
"""

str_requests="""
    requests属性和方法如下：
        request.encoding()   获取
        request.encoding=""  设置
        request.text         以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码
        request.contend      以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
        request.headers      以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
        request.status_code  响应状态码
        request.raw          返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()   
        request.ok           查看r.ok的布尔值便可以知道是否登陆成功
 
 #*特殊方法*#
        request.json()       Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
        request.raise_for_status()              失败请求(非200响应)抛出异常

"""
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
url="http://www.163.com"

import urllib.request
import requests
import urllib.request
import urllib.parse
from http import cookiejar
import re
from lxml import etree
#url='https://www.biqugela.com/'
#url = 'http://httpbin.org/get'
#http://www.python.org/
def re_quest_get(url):
    with urllib.request.urlopen(url) as resposne:
        #print(type(resposne))
        html = resposne.read().decode()
        #print(type(html))
        #print(html)
def re_quest_Request_post(url,headers):
    dict = {
        'user':'jxwhp',
        "password" : '111134'
    }

    data = text_parse_b(dict)
    print(url)
    #request = urllib.request.Request(url,data = data,headers=headers,method='POST')  #得到一个请求对象
    #request = urllib.request.Request(url,data)
    request = urllib.request.Request(url,data=data,headers=headers)
    #request.add_header('headers',headers)
    #request.add_header('method','POST')
    response1 = urllib.request.urlopen(request)

    html = response1.read()
    # 如果网页源代码里有中文乱码,判断html是不是字节流，是字节流转码时加unicode-escape  html = html.decode('unicode-escape')
    #          判断html不是是字符串，是字符串转码时加unicode-escape  html = html.encode('latin-1').decode('unicode-escape')

    html = html.decode('unicode-escape')

    #print(html)
def text_parse_b(dict):

    data = bytes(urllib.parse.urlencode(dict),encoding='UTF-8')

    return data
def get_cookie_urllib(url,headers):
    cookie = cookiejar.CookieJar()
    cookie_handle = urllib.request.HTTPCookieProcessor(cookie)
    cookie_opener = urllib.request.build_opener(cookie_handle)
    response = cookie_opener.open(url)
    #print(response.read().decode())
    #print(cookie)
    #for cookie in cookies:

    # urllib.request.install_opener(cookie_opener)
    # request = urllib.request.Request(url,headers=headers)
    # response = urllib.request.urlopen(request)
    #print(response.read().decode('unicode-escape'))
    for item in cookie:
        print(item.name, ':', item.value)

def get_cookie_request(url,headers):
    response = requests.get(url,headers)
    cookies = response.cookies
    #print(cookies)
    for cookie in cookies:
        print(cookie.name + ':' + cookie.value)

        print('****'*10)
def url_cookie_opener(url):
    cookie = cookiejar.CookieJar()
    handle = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handle)
    response = opener.open(url)
    #print(response.read())
    #print(cookie)
    for i in cookie:
        print(i.name, ':' , i.value)

#笔趣网实例
def func_opener(url,headers):
    # cookies = cookiejar.CookieJar()   #取cookies 值
    # handler = urllib.request.HTTPCookieProcessor(cookies) #通过cookies 取handler
    handler = urllib.request.HTTPHandler()
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)

    html = response.read().decode()


    return html

def title_re(html):
    res = re.compile(r'<li><a href="/(.*?)">(.*?)</a></li>')
    res1 = re.findall(res,html)
    return res1
def title_xpath(html):
    dom = etree.HTML(html)
    content = dom.xpath("//*[@id='wrapper']//*[@class='nav']//a/text()")
    href = dom.xpath("//*[@id='wrapper']//*[@class='nav']//a/@href")
    #print(content,href)
    return content,href

def classify_xpath(html):
    dom1 = etree.HTML(html)
    content_1 =dom1.xpath("//*[@id='newscontent']//*[@class='l']//span[2]/a/text()")
    href_1 = dom1.xpath("//*[@id='newscontent']//*[@class='l']//span[2]/a/@href")
    return content_1,href_1

def text_xpath(html):
    dom2 = etree.HTML(html)
    content_1_1 = dom2.xpath("//*[@id='list']//dd/a/text()")
    href_1_1 = dom2.xpath("//*[@id='list']//dd/a/@href")

    return content_1_1,href_1_1



def title_url(res1,headers):
    for i in res1[1:2]:
        title_url = url + i[0]
        #print(title_url)
        for j in range(1,2):
            print(j)
            title_url_1 = url + i[0] + '{}'.format(j)+'.html'
            print(title_url_1)
            html = func_opener(title_url_1,headers)
            print(html)
            dom1 = etree.HTML(html)
            text = dom1.xpath('//*[@id="newscontent"]//*[@class="l"]//span[2]/a/text()')
            href = dom1.xpath('//*[@id="newscontent"]//*[@class="l"]//span[3]/a/@href')

            for i in range(len(href[:1])):
                content_1 = text[i].strip(' \r\n ')
                href_1 = url + href[i].lstrip('/')
                print(content_1)
                print(href_1)
                response_1 = func_opener(href_1,headers)
                print(response_1)
#
# if __name__ == '__main__':     # 此处为下载笔趣网小说实例
#     url = 'https://www.biqugela.com/'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
#     }
#     #get_cookie_request(url,headers)
#     #get_cookie_urllib(url,headers)
#    # re_quest_Request_post(url,headers)
#     #url_cookie_opener(url)
#     html = func_opener(url,headers)
#     content,href = title_xpath(html)
#     for i in href[1:2]:         # 总值：12 此处做切片  [:12] 测试取值[1:2]
#
#         href_1 = url + i.lstrip('/')
#         #print(href_1)
#         html_1 = func_opener(href_1,headers)
#         content_1 , href_2 =classify_xpath(html_1)
#
#         for j in range(len(content_1[1:3])):  # 共30篇，此处做切片[:30] 测试取值[:1]  此处选第一篇
#             content_name = content_1[j].strip(' \r\n ')
#             print(content_name)
#
#             url_href_2 = url + href_2[j].lstrip('/')
#
#             html_2 = func_opener(url_href_2,headers)
#
#             content_1_1,href_1_1 = text_xpath(html_2)
#
#             href_1_1 = href_1_1[12:]  # 此处选章节
#             content_1_1 = content_1_1[12:]
#             print(len(href_1_1),len(content_1_1))
#             for k in range(len(href_1_1)):
#                 url_href_1_1 = url + href_1_1[k].lstrip('/')
#                 content_1_1_name = content_1_1[k].strip(' ')
#                 print(content_1_1_name)
#                 print(url_href_1_1)
#                 html_3 = func_opener(url_href_1_1,headers)
#                 dom4 = etree.HTML(html_3)
#                 text =dom4.xpath("//*[@id='content']//p/text()")
#                 with open('./pic/{}'.format(content_name),'a+',encoding='UTF-8') as fi:
#                     fi.write(content_1_1_name)
#                 for t in text:
#                     txt = t.strip(' \n\r ')
#                     print(t.strip(' \n\r '))
#                     with open('./pic/{}'.format(content_name),'a+',encoding='UTF-8') as f:
#                         f.write(txt)   #  #  #
#
#


