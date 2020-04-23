#
# import urllib.request
# import http.cookiejar
# import urllib2
#
# url = 'http://www.baidu.com'
# # 直接通过url来获取网页数据
# print('第一种')
# response = urllib.request.urlopen(url)
# code = response.getcode()
# html = response.read()
# mystr = html.decode("utf8")
# response.close()
# print(mystr)
#
# # 构建request对象进行网页数据获取
# print('第二种')
# request2 = urllib.request.Request(url)
# request2.add_header('user-agent', 'Mozilla/5.0')
# response2 = urllib.request.urlopen(request2)
# html2 = response2.read()
# mystr2 = html2.decode("utf8")
# response2.close()
# print(mystr2)
#
# # 使用cookies来获取
# print('第三种')
# cj = http.cookiejar.LWPCookieJar()
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# urllib.request.install_opener(opener)
# response3 = urllib.request.urlopen(url)
# print(cj)
# html3 = response3.read()
# mystr3 = html3.decode("utf8")
# response3.close()
# print(mystr3)
#----------------------
# 首先构建Request请求
import urllib.request
import urllib.parse
import urllib
from http import cookiejar

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
}

#url = 'https://www.biqugela.com/'
#url = 'http://www.zhihu.cn/'
data = {
    "1" : "3333",
    "吴海平" : "姓名"
}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}

def data_parse(data):
    data = urllib.parse.urlencode(data)
    data = bytes(data)
    return data


def get_cookie_cookies(url):
    opener = urllib.request.build_opener()
    opener.addheaders.append(('cookies','7fMZQdQvCP705piDUIGpSf9FGIWnJXS2'))  #以元组形式传送
    request = urllib.request.Request(url)
    response = opener.open(request).read().decode()
    print(response)

def get_response_code(url):
    try:
        response = urllib.request.urlopen(url)
        print(response.read().decode())
    except urllib.request.HTTPErrorProcessor as e:
        if hasattr(e,'code'):
            print('==============Error code',e.code)

def get_redicrect(url):
    response = urllib.request.urlopen(url)
    isRedirected = response.geturl() == 'http://www.zhihu.cn/'
    print(response.code)
    print(isRedirected)

def get_cookie(url):
    cookies = cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url).read().decode()
    print(type(cookies))
    for item in cookies:
        print(item.name + '=' + item.value)
    print(response)
def save_cookies(url):
    filename = 'cookie.txt'
    cookies = cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    cookies.save(ignore_discard=True,ignore_expires=True)

def save_cookie_lwp(url):
    filename = 'cookies.txt'
    cookies = cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url).read().decode()
    cookies.save(ignore_discard=True,ignore_expires=True)
    print(response)
# 利用cookie.txe文件访问网页源代码
def get_response_cookies(url):
    cookies = cookiejar.LWPCookieJar()
    cookies.load('cookies.txt',ignore_expires=True,ignore_discard=True)
    handle = urllib.request.HTTPCookieProcessor(cookies)
    opener = urllib.request.build_opener(handle)
    response = opener.open(url).read().decode()
    print(response)
def get_response_cookie(url):
    cookie = cookiejar.MozillaCookieJar()
    cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url).read().decode()
    print(response)
# 构建opener全局对象

def get_response_install_opener(url):
    proxy = urllib.request.ProxyHandler({'http':'14.115.69.115:4256'})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url).read().decode()
    print(response)

def get_response_opener(url):
    proxy = urllib.request.ProxyHandler({'http':'14.115.69.115:4256'})
    opener = urllib.request.build_opener(proxy)
    response = opener.open(url).read().decode()
    print(response)
def get_response(url):
    handler = urllib.request.HTTPHandler(debuglevel=1)
    handlers = urllib.request.HTTPHandler(debuglevel=1)
    opener = urllib.request.build_opener(handler,handlers)
    response = opener.open(url).read().decode()
    #print(response)

if __name__ == "__main__":
    url = 'http://www.baidu.cn/'
    get_response(url)