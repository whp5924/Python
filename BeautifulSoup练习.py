#
#BeatifulSoup适合的解析器
#   1. python 标准库        BeatifulSoup(markup,"html.parse")
#   2. lxml HTML解析器      BeatifulSoup(markup,"lxml")
#   3. lxml XML解析器       BeatifulSoup(markup,["lxml-xml"])
#                           BeatifulSoup(markup,"xml")
#   4. html5lib             BeatifulSoup(markup,"html5lib")
# BeatifulSoup四个对象
#   1. Tag 网页源代码的节点及内容
#   2. navigableString 标签的内容
#   3. BeatifulSoup 主要是实例对象
#   4. comment 注释
# 遍历文档树
#   1. 直接子节点
#       Tag.children    直接通过下标名称访问子节点
#       Tag.contents        以列表的形式返回所有子节点
#       Tag.children        生成器,可用于循环访问 for child in Tag.children

#       . contents
#           可以将Tag的子节点以列表的方式输出
#               .contents  向后遍历树
#               .parent    向前遍历树
#       . children
#           返回的不是列表,但是可以是列表生成器
#           可以通过for循环遍历孩子  for child in soup.body.children
#   2. 所有子孙节点
#       .descendants 可以对所有Tag的子孙节点进行递归循环 for descendants in Tag.descendants
#   3. 节点内容
#       .string Tag.string
#           如果标签里没有标签,可以使用Tag.string
#           如果标签里只有一个唯一的标签，可以使用Tag.string
#   4.  多个内容
#       .strings
#           如果标签里有多个标签,可以用遍历的形式访问   for string in Tag.strings
#       .stripped_strings
#           如果输出的字符串中有多个空行、空格等,可以使用Tag.stripped_strings遍历去掉多余的空格、空行
#   5. 父节点
#       .parent  父节点
#           Tag.parent  父节点
#           Tag.parents 父到根的所有节点
#   6. 全部父节点
#       .parents  全部父节点
#   7. 兄弟节点
#       .next_sibling
#       .previous_sibling
#       .next_siblings
#       .previous_siblings
#   8. 全部兄弟节点
#       .next_siblings
#       .previous_siblings
#       全部兄弟节点可以通过迭代形式输出  for sibling in soup.a.next_siblings:
#   9. 前后节点
#       .next_element
#       .previous_element
#   10. 所有的前后节点
#       .next_elements
#       .previous_elements
#
# 搜索文档树
#   find_all(name,attrs,recursive,text,**kwargs)
# 传name参数
#   1. 传字符串     传入标签的名称
#   2. 传正则表达式
#        re.compile("^字符串")  ^匹配以字符串开头所有节点    传入正则表达式的标签内容
#   3. 传列表
#       [标签名[,标签名[,标签名]]]
#   4. 传True
#       for tag in soup.find_all(True):
#   5. 传方法
#       可以定义一个方法
#       def tag_has_class_no_id()
#           return tag.has_attr("class") and  not tag.has_attr("id")
#       soup.find_all(tag_has_class_no_id)
# 传keyword参数
#   例：soup.find_all(属性='值')                         单属性
#       soup.find_all(属性=re.compile(正则表达式))       属性值为正则表达式
#       soup.find_all(属性='值'...属性='值')             多属性
#       soup.find_all(标签,属性='值')                    标签+属性
#       soup.find_all(属性={'key':'value'}               属性为字典
#
# 传text
#   例: soup.find_all(text=字符串)                        text=字符串
#       soup.find_all(text=[字符串，字符串..字符串])      text=[字符串,字符串,字符串]
#       soup.find_all(text=re.compile(正则表达式)         text=正则表达式

# 传limit参数
#   为提高效果,限制搜索的结果数量
#   例: soup.find_all(标签,limit=数值)

# 传recursive参数
#   find_all()搜索所有的子节点,如果只想搜索直接节点,可以传入参数 recursive=False
#   例: soup.find_all(标签,recursive=False)

# find() 直接返回




from bs4 import BeautifulSoup
from lxml import etree
import html5lib
import re
import lxml
import requests
#定义一个网页源代码

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# </body>
# </html>
#
# """

#<class 'bs4.element.ResultSet'>
#<class 'bs4.element.Tag'>
#url = 'https://www.cnblogs.com'
url = 'https://www.biqugela.com/book_1898/'
url_base = 'https://www.biqugela.com/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
r=requests.get(url).content.decode()
soup=BeautifulSoup(r,'lxml')
title_name = soup.title.text.strip(' \n\r ')
print(title_name)
href = soup.select('div#list dd>a')
#print(len(href)-12)
for i in href[12:]:
    #print(type(i))
    href_1 = i['href'].lstrip('/')
    chapter = i.text.strip(' \n\r ')
    url_chapter = url_base + href_1
    #print(chapter,url_chapter)
    r_chapter = requests.get(url_chapter,headers).content.decode()
    soup_chapter = BeautifulSoup(r_chapter,'lxml')
    #print(type(soup_chapter))
    chapter_text = soup_chapter.select('p.content_detail')
    print(len(chapter_text))
    for j in chapter_text:
        #print(type(j))
        content = j.text.strip(' \n\r ')
        #print(content)
        with open("./pic/{}.txt".format(title_name),"a+",encoding='utf-8') as f:
            f.write(content)
