#

# 冰雪奇缘2
# 0. 框架
# https://youku.cdn7-okzy.com/20200208/17059_b76b7053/1000k/hls/6e4b9af7f7e000000.ts
# https://youku.cdn7-okzy.com/20200208/17059_b76b7053/1000k/hls/6e4b9af7f7e001542.ts
import requests
from  multiprocessing import Pool

def V_steam(i):
    # 1. url
    url = 'https://youku.cdn7-okzy.com/20200208/17059_b76b7053/1000k/hls/6e4b9af7f7e00%04d.ts' % i
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    print(url)

    # 2. 请求 解析

    r = requests.get(url ,headers=headers).content



    # 3. 删选数据



     # 4. 保存

    with open("./pic/mpeg/{}".format(url[-8:]) , "wb") as f:
           f.write(r)

if __name__=="__main__":
    pool=Pool(10)
    for i in range(4):
        pool.apply_async(V_steam,(i,))
    pool.close()
    pool.join()
