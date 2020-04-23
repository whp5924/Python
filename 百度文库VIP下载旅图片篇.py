#

# 0. 框架
import requests
import re
import urllib.request
from lxml import etree
from bs4 import BeautifulSoup


# 1. url
url='https://wenku.baidu.com/view/c7752014f18583d04964594d.html'

u1='https://wenku.baidu.com/browse/getrequest?doc_id=c7752014f18583d04964594d&pn=17&rn=1&type=ppt&callback=bd__cbs__ygx0yo'
u2='https://wenku.baidu.com/browse/getrequest?doc_id=c7752014f18583d04964594d&pn=18&rn=1&type=ppt&callback=bd__cbs__gv7fdb'
u3='https://wenku.baidu.com/browse/getrequest?doc_id=c7752014f18583d04964594d&pn=16&rn=1&type=ppt&callback=bd__cbs__163r5'
u4="https://wenku.baidu.com/browse/getrequest?doc_id=c7752014f18583d04964594d&pn=5&rn=1&type=ppt&callback=bd__cbs__dgxi32"

headers={

}

class Wk():
    def __init__(self):
        #self.base_url='https://wenku.baidu.com/view/c7752014f18583d04964594d.html'
        self.headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
    def getResponse(self,url):
        try:
            # request=urllib.request.Request(url,headers=self.headers)
            # response=urllib.request.urlopen(request,timeout=8)
            request=requests.get(url,headers=self.headers).content.decode()
            print(request)

        except:
            print("请求页面失败......")
        else:
            # return response.read().decode("gb2312")
            return request


if __name__=="__main__":
    wk=Wk()
    # wk.spyder(wk.base_url)
    for page in range(1,25):
        url='https://wenku.baidu.com/browse/getrequest?doc_id=c7752014f18583d04964594d&pn={}&rn=1&type=ppt'.format(page)
    #&rn=1&type=ppt&callback=bd__cbs__ygx0yo
        html = wk.getResponse(url)
        reg = r'"zoom":"(.*?)","page"'
        reg = re.compile(reg)
        text = reg.findall(html)[0]
        text = text.replace("\\", "")
        # print(type(text))
        print(text)
        req = requests.get(text)

        with open("./pic/第{}图.jpg".format(page), "wb") as f:
            f.write(req.content)

#   原始url

# 2. 请求、解析
# requests 框架

