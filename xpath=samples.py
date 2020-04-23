#-*-coding:UTF-8
"""
Xpath使用方法:
    1. xpath常用规则

        nodename            选取此节点的所有子节点
        /               	从当前节点选取直接子节点
        // 	                从当前节点选取子孙节点(模糊子节点查找)
        . 	                选取当前节点
        .. 	                选取当前节点的父节点
        @ 	                选取属性
        * 	                通配符，选择所有元素节点与元素名
        @* 	                选取所有属性
        [@attrib] 	        选取具有给定属性的所有元素
        [@attrib='value'] 	选取给定属性具有给定值的所有元素
        [tag] 	            选取所有具有指定元素的直接子节点
        [tag='text'] 	    选取所有具有指定元素并且文本内容是text节点


    2.  xpath的运算符
        运算符 	描述 	            实例 	                返回值
        or  	或 	        age=19 or age=20 	        如果age等于19或者等于20则返回true反正返回false
        and 	与 	         age>19 and age<21 	        如果age等于20则返回true，否则返回false
        mod 	取余 	        5 mod   2 	1
        | 	取两个节点的集合 //book | //cd 	            返回所有拥有book和cd元素的节点集合
        + 	加                   6+4 	10
        - 	减 	6-4 	            2
        * 	乘                   6*4 	24
        div 除法 	            8 div 4 2
        = 	等于 	            age=19 	true
        != 	不等于 	            age!=19 	true
        < 	小于 	            age<19 	    true
        <= 	小于或等于       	age<=19 	true
        > 	大于 	            age>19 	true
        >=  大于或等于 	        age>=19 	true



2. requests
    1. requests.get()     get请求
        a. 没有请求的参数类型  requests.get(url)
        b. 有请求参数的类型   requests.get(url,params={'key1':'value1','key2':'value2'}) 键值对表示参数
        c. 有请求头           requests.get(url,headers={'key1':'value1'})

    2. requests.post(url)    post请求
        a. 请求正文是application/x-www-form-urlencoded
            requests.post(url,params={'key1':'value1','key2':'value2}',headers={'Content-Type':'application/x-www-form-urlencoded'})
        b. 请求正文是multipart/form-data
            requests.post(url.params={'key1':'value1','key2':'value2'},headers={'Content-Type':'multipart/form-data'})
        c. 请求正文是raw
            I.  传入xml格式文本
                requests.post(url,data='<?xml  ?>',headers={'Content-Type':'text/xml'}
            II. 传入json格式文本
                requests.post(url,data=json.dumps({'key1':'value1','key2':'value2'},headers={'Content-Type':'application/json'})
                或requests.post(url,json={'key1':'value1','key2'"'value2'},headers=['Content-Type':'application/json'})
        d. 请求正文是binary
            requests.post(url,file={'file':'open('test.***','wb')},headers={'Content-Type':'binary'})
    3. r=requests.put(url)     put请求
    4. r=requests.delete()     delete请求
    5. r=requests.head()          head请求
    6. r=requests.options()    options请求

"""
# 测试单个下载




#  ===
# # 0. 框架
import requests
from lxml import etree
#
#
# # 1. url
#
url='http://music.taihe.com/top'
url12='http://music.taihe.com/top/dayhot'
base_url='http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid='
# 2. 请求 requests
text=requests.get(url).text            # 总目录 content/decode(0


dom1=etree.HTML(text)
song_type_ids=dom1.xpath('//a[contains(@href,"/top")]/@href')[1:2]      #提取歌名目录属性/top/dayhot
song_type_names=dom1.xpath('//h2/text()')[0:1]                          #提取歌名目录
print(type(song_type_names))
j=0
for i in song_type_ids:
    url1_1=url.strip('/top')+'/'+i
    song_type_names_1=song_type_names[j]
    text=requests.get(url1_1).content.decode()
    j += 1
# 3. 删选数据
    dom = etree.HTML(text)
    song_names_1=dom.xpath("//a[contains(@href,'/song')]/text()")[2:] #列表类型
    song_ids = dom.xpath('//a[contains(@href,"/song")]/@href')[2:]    #列表类型
    song_names_1.remove('原创音乐榜')                                 #列表删除最后一个元素
    song_ids.remove(r'http://y.taihe.com/top/song?play_top=top&pst=music_top') #列表删除最后一个元素
    print(len(song_names_1))
    print('------------------------------------------------')
    for song_name,song_id in zip(song_names_1,song_ids):   # 返回后是lxml.etree._ElementUnicodeResult
        count_id=song_id.strip('/song/')
        base_url_1=base_url+count_id+'.mp3'
        #print(base_url_1)
        song_new_name=song_name.replace('/','／')
        # print(song_new_name)
        # print(count_id)
        song_url=base_url_1+count_id
        # print(song_new_name)
        mp3=requests.get(song_url).content
        # with open("./pic/%s/%s.mp3" % (song_type_names_1,song_new_name),"wb") as file:
        #     print()
            #print(song_new_name)
            #file.write(mp3)

# 4. 保存

#==============================================================================================

# # 0. 框架
# import requests
# from lxml import etree
#
#
# # 1. url
#
# url='http://music.taihe.com/top/dayhot'
#
#
# # 2. 请求 requests
#
# text=requests.get(url).content.decode()
#
#
# # 3. 删选数据
#
# # //a[contains(@href,'/song')]/text()
# # //a[contains(@href,'/song')]/@href
# dom = etree.HTML(text)
# song_names=dom.xpath("//a[contains(@href,'/song')]/text()")[2:102]
# song_ids=dom.xpath('//a[contains(@href,"/song")]/@href')[2:102]
# print(song_ids)
# # song_ids=dom.xpath('//a[contains(@href,"/song")]/@href)')




# 4. 保存




