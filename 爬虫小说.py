# --*-- UTF-8 --*--
import urllib.request
import re
from multiprocessing import Pool
import gzip
headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_be0e39a35cd0d6e9cc62c031fb378d90=1585093724; ChapterOrder=asc; look_9063=1; look_182=1; autoplaycookie=0; look_184_182=1; Readed=182-183,182-,182-184,9063-; look_183_182=1; Hm_lpvt_be0e39a35cd0d6e9cc62c031fb378d90=1585098604',
    'Host': 'www.xs4.cc',
    'Pragma': 'no-cache',
    'Referer': 'https://www.xs4.cc/changshengjie/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


# 2.定义一个函数


def getNovlContent(url):
# 获取主页面源代码
    request=urllib.request.Request(url)
    request.headers=headers
    respone=urllib.request.urlopen(request)
    print(respone)
    html=gzip.decompress(respone.read())


#解码

    html=html.decode("gb2312")

# #获取章节超链接
    req=r'<a href="(.*?)" title="(.*?)">'
    req=re.compile(req)
    urls = req.findall(html)[42:729]  #42:729
#
# #遍历每章（章节网址和名字）建立内存池
#
    for i in urls:

        novel_url = i[0]
        novel_name_file = i[1][:4]
        novel_name=i[1]
        chapter = urllib.request.urlopen(novel_url).read()
        chapter_html = chapter.decode("gbk")

# #获取小说内容
        reg ='<div id="content">(.*/?)/></div>'
        reg=re.compile(reg)
# #多行匹配

        chapter_content = reg.findall(chapter_html)

        # # #删掉多余的字符串（替换）
        chapter_content = chapter_content[0].replace(" ","")
        chapter_content=chapter_content.replace("<br><br>","\n")
        chapter_content = chapter_content.replace("br><br>", "\n")
        chapter_content = chapter_content.replace("<br", "\n")
        print(chapter_content)
# # #下载小说
#         print("正在下载：%s"%novel_name)
#         f = open('./pic/{}.txt'.format(novel_name_file),"w",encoding='UTF-8')
#         f.write(novel_name+'\n\n')
#         f.write(chapter_content+'\n')
#         f.close()
# #调用函数

getNovlContent("https://www.xs4.cc/changshengjie/")

    # for i in range(4):
    #     pool = Pool(10)
    #     pool.apply_async(V_steam,(i,))
    # pool.close()
    # pool.join()