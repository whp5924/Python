#

import requests
import chardet
from io import BytesIO
import gzip
# 直接登陆到163邮箱
def func_requests(url,headers):

    s = requests.Session()
    r = s.get(url,allow_redirects=True)
    data = {'name':'jxwhp@163.com','password':'jxwhp6335924'}
    r = s.post(url,data=data,allow_redirects=True,headers=headers)
    print(r.text)
def func_request(url,headers):
    html = requests.get(url,headers)
    print(html.text)

def func_proxy(url,headers):
    proxy = {
        'http' : "14.118.162.246:4256"
    }
    response = requests.get(url,headers,proxies=proxy)
    print(response.text)
if __name__ == '__main__':
    url = 'http://www.163.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
    }
    func_proxy(url,headers)