#
#selenuim 学习
"""
browser=browser.find_element_by_css_selector()
方式一：
    后代或平级关系来选择元素
    父元素:
        # 表示通过id属性来定位元素
        . 表示过过class属性够定位元素
    子元素(后代关系)
        # 表示通过id属性来定位元素
            # choose_car option （空格）后面的元素不必是前面元素的直接子元素，（并列子关系)
        . 表示通过class属性来定位元素
            . s_ipt_wr option   (空格)

        # choose_car > option   含键值 > 后面的元素必须是前面元素的直接子关系
        . s_ipt_wr > option

        ul > ol > li > p   可以是很多级的父子关系

    组合型

        # food  > span option  选择id为food的所有span的子元素和所有option的子元素
        . s_ipt_wr > span option

        # food > * 选择id为food的所有子元素

    兄弟节点的选择(平级关系0
        # food + div 选择id为food 紧跟后面的div
        . food ~ div  选择class为food后面的div 或div 们 只在在class 后面,不需要紧跟

方式二:
    *[style]                    选择所有的style属性的元素
    p[spec=len2]                选择所有的spec属性值只等于len2的p元素
    p[spec='len2' 'len3']      选择spec属性值只等于len2 len3的p元系 有空的值一定要加""
    p[spec*='len2']             选择spec属性值包含len2的p元素
    p[spec^='len2']             选择spec属情值以len2开关的p元素
    p[spec$='len2']             选择spec 属性值以len2结尾的p元素
    p[class=specia][name=p1]    选择class属性值为specia并且 name值为p1的p元素
    p:nth-child(1)              选择第一个p元素
    p:nth-last-child(1)         选择倒数第一个p元素 要保证最后一个是p元素


    1.移动到元素element对象的“底端”与当前窗口的“底部”对齐

        driver.execute_script("arguments[0].scrollIntoView(false);",element)

    2.移动到元素element对象的“顶端”与当前窗口的“顶部”对齐

        driver.execute_script("arguments[0].scrollIntoView();",element)

    3.移动到页面底部

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    4.移动到页面顶部

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight，0)")
"""


# 0. 框架
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import parse
from lxml import etree


url='https://wenku.baidu.com/view/f15a777a27284b73f242507f.html'
# 1. 实例

browser = webdriver.Chrome()         # 实例化对象，构建一个浏览器，并请求网页
browser.get(url)
time.sleep(16)                       # 等待页面加载完成，否则有可能找不到目标元素或不能点击的情况

# scroll_add_crowd_button = browser.find_element_by_css_selector('#html-reader-go-more' > div.banner-core-wrap.super-vip > div.doc-banner-text')
# 找元素   复制类选择器
# 找到目标元素上方适应位置的元素
scroll_add_crowd_button = browser.find_element_by_css_selector('div#html-reader-go-more > div.banner-core-wrap.super-vip > div.doc-banner-text')
browser.execute_script("arguments[0].scrollIntoView();",scroll_add_crowd_button)
time.sleep(8)

try:
    browser.find_element_by_css_selector('div.continue-to-read > div.banner-more-btn > span').click()
    time.sleep(5)
except Exception as e:
    print(str(e))
html=''
a=0
while True:
    a+=1
    #print(browser.page_source)
    html=html+browser.page_source

    browser.execute_script("window.scrollBy(0,1080)")
    time.sleep(1)
    #print(type(html))
    if a >27:
        break


soup=BeautifulSoup(html,'html.parser')

data_list=soup.select('div.reader-txt-layer > div.ie-fix > p')

b,c= 0,0
data_all=[]
data_line=[]
for i in data_list:

    data=i.find_all(text=True)[0]  #bs4的函数

    data_line.append(data)


    re_data=re.compile("\d+")   # compile()函数表示将正则表达式的字符串形式编译成一个pattern对象
    if re_data.findall(data):    # 在做正则表达式时,数据类型必须统一
        b += 1
        s = ','.join(data_line).replace('\\n','')
        data_all.append(s)
        data_line = []
        print(s+'_'+str(b))
data_all=set(data_all)
print('共', len(data_all) , '条数据。')
print(data_all)
for j in range(len(data_all)):
    j=str(j)+'. '+str(list(data_all)[j])+'\n'
    with open("./aa.doc",'a+') as f:
        f.write(j)







