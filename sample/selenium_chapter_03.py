from  selenium import webdriver
import requests
from selenium import webdriver
import re
import json
session=requests.session()
url1='https://wkretype.bdimg.com/retype/text/7eb0e17e81c758f5f61f67ff?md5sum=d040419b19c23732a8ba707db18b844a&sign=12f85e6f6a&callback=cb&pn=1&rn=4&type=txt&rsign=p_4-r_0-s_06fbb&_=1585629416072'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

def fetch_url(url):
    #print(session.get(url).content.decode("gbk"))
    # text=session.get(url3,headers=headers).content.decode(encoding='utf-8')
    # print(text)
    return session.get(url,headers=headers).content.decode("gbk")


def  get_doc(url):
#https://wenku.baidu.com/view/7eb0e17e81c758f5f61f67ff.html?from=search
    return re.findall('view/(.*?).html',url)[0]

def parse_type(content):

    return re.findall(r"docType'.*?:.*?'(.*?)'.*?",content)[0]

def parse_title(content):
    return re.findall("title'.*?:.*?'(.*?)'",content)[0]

def parse_md5sum(doc_id):
    content_url='https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id={}'.format(doc_id)
    content1=fetch_url(content_url)
    return content1

def save_file(filename,text):
    with open(filename,'w',encoding='utf-8') as f:
        f.write(text)
        print('保存完毕')
def main():
    url=input("请输入你的url地址")
    content=fetch_url(url)
    doc_id=get_doc(url)
    doc_type=parse_type(content)
    doc_title=parse_title(content)
    content_txt = parse_md5sum(doc_id)
    md5 = re.findall(r"\"md5sum\":\"(.*?)\"", content_txt)[0]
    rn = re.findall('"totalPageNum":"(.*?)"', content_txt)[0]
    sign = re.findall('"rsign":"(.*?)"', content_txt)[0]

    for i in range(1,2):
        text_url = 'https://wkretype.bdimg.com/retype/text/' +doc_id +'?' +md5 + '&pn=' + str(i) +"&rn=" + rn + '&rsign=' + sign +'&_=1585633820783'
        print(text_url)
        content_1=json.loads(fetch_url(text_url))
        print(content_1)
        text=''
        for item in content_1:
            for item1 in item['parags']:
                text+=item1['c']
                print(text)
                save_file('./'+doc_title + ".txt" ,text)



   # if doc_type=='txt':
    #text_url='https://wkretype.bdimg.com/retype/text/'+ doc_id + '?' + md5 +

# https://wkretype.bdimg.com/retype/text/7eb0e17e81c758f5f61f67ff?md5sum=d040419b19c23732a8ba707db18b844a&sign=12f85e6f6a&callback=cb&pn=1&rn=4&type=txt&rsign=p_4-r_0-s_06fbb&_=1585633820783
if __name__=="__main__":
    main()
