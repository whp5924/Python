#下载一本小说并存放在指定目录(本代码只对新笔趣阁http://www.xbiquge.la的小说有效)
import requests
import urllib.request
import multiprocessing #本代码未使用多线程加速
from bs4 import BeautifulSoup
import re #本代码未使用正则表达式（太难了。）
import os #文件流模块
import time #时间模块
import gzip #压缩解压缩模块
from urllib.error import HTTPError,URLError #错误处理模块
import random #随机数模块


#头字典里的值须修改成自己电脑访问网页时对应的值
# req_header={
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Accept-Encoding':'gzip, deflate',
#     'Accept-Language':'zh-CN,zh;q=0.9',
#     'Connection': 'keep-alive',
#     'Cookie':'_abcde_qweasd=0; __guid=270189431.88115020722726830.1582038501555.4824; _abcde_qweasd=0; bdshare_firstime=1582038502825; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1582038503; monitor_count=3; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1582038564',
#     'Host':'www.xbiquge.la',
#     'Upgrade-Insecure-Requests':'1',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
# }

req_header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '_abcde_qweasd=0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=wf4m8340oQeNagjuNxjMwFlGVNGIY0rgrdWBNG2YkI7&wd=&eqid=a0ce060b0008729c000000065e79b484; _abcde_qweasd=0; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1585034380; bdshare_firstime=1585034379684; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1585034908',
    'Host': 'www.xbiquge.la',
    'Pragma': 'no-cache',
    'Referer': 'http://www.xbiquge.la/7/7931/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

#打开并返回整个网页
def url_open(url):
    '''
    因免费代理不稳定故不使用代理
    proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})
    opener=urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    '''
    request = urllib.request.Request(url,headers=req_header)
    response = urllib.request.urlopen(request)
    content = gzip.decompress(response.read())
    data = content.decode('utf-8')
    print("111:",type(data))
    return data

class novel_catch(object):

    def __init__(self,url):#init两边各有两个_
        self.url = url
        self.chapter_names = []#存放章节名称
        self.chapter_hrefs = []#存放章节链接

    #获取章节名称和章节URL
    def get_catalogue(self):
        response=url_open(self.url)
        soup = BeautifulSoup(response, "html.parser")
        #chapter_hrefs=re.findall('/\d\d/\d\d\d\d\d/\d\d\d\d\d\d\d\.html',soup)
        a=soup.find('div',id='list')
        #print(a)
        for i in a.dl:
            if i.name=='dd':
                self.chapter_names.append(i.string)
                self.chapter_hrefs.append('http://www.xbiquge.la'+i.a['href'])
        self.novel_name=soup.find('div',id='info').h1.string#获取书名
    
    #获取对应章节的内容
    def get_chapter_text(self,url):
        try:
            response=url_open(url)       
            soup = BeautifulSoup(response, "lxml")
            a=soup.find('div',id='content')
            text=''
            for i in a:
                if i.name!='p' and i.name!='br':
                    text+=(i.string+'\n')
        
            return text
        except HTTPError as e:
            print(e.code)
            print("获取章节内容失败,1秒后重试！")
            time.sleep(1)
            self.get_chapter_text(url)
        except URLError as e:
            print(e.reason)
            print("获取章节内容失败,1秒后重试！")
            time.sleep(1)
            self.get_chapter_text(url)
        except Exception as e:
            print(e)
            print("获取章节内容失败,1秒后重试！")
            time.sleep(1)
            self.get_chapter_text(url)
    
    #写入txt文档，path为写入路径，没有将创建，name为章节名，text1为章节具体内容
    def writer(self,name,path,text1):
        with open(path,'a',encoding='utf-8') as f:
            print()
            # f.write(name+'\n')
            # f.write(text1)
            # f.write('\n\n')







#主函数入口    
if __name__ == "__main__":
    novel_1=novel_catch('http://www.xbiquge.la/7/7931/')#修改网址为想要下载小说的目录url

    novel_1.get_catalogue()

    for i in range(len(novel_1.chapter_names)):
        name=novel_1.chapter_names[i]
        text=str(novel_1.get_chapter_text(novel_1.chapter_hrefs[i]))
        novel_1.writer(name,'./novel'+novel_1.novel_name+'.txt',text)#这句中的'F:\学习资料\程序设计\python练习代码\\'需要修改成你自己的路径

        print(name+'\t下载完成',i)
        time.sleep(random.choice([0.5,1,1.5,2]))#下载完一章节后随即停顿

    print('successful')#全本小说下载完
    
  








