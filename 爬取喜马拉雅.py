#
import  requests
import re
import json
#https://www.ximalaya.com/revision/category/detailCategoryPageInfo?category=youshengshu&subcategory=wenxue
#https://www.ximalaya.com/revision/category/detailCategoryPageInfo?category=youshengshu&subcategory=shenghuo
#-----------
#https://www.ximalaya.com/revision/category/detailCategoryPageInfo?category=youshengshu&subcategory=wenxue








#------------------------------------------------------------------

url = 'https://www.ximalaya.com/revision/category/detailCategoryPageInfo?category=youshengshu'
#https://www.ximalaya.com/revision/play/v1/audio?id=270708211&ptype=1

headers={
    'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
#---------------------------------------
def req_uest(url,headers):
    r = requests.get(url,headers=headers)
    return r
def url_list(url,headers):
    r = req_uest(url,headers)
    result = json.loads(r)
    return result


if __name__ == '__main__' :
    result = url_list(url,headers)
    contend_list=result['data']['subcategories']
    for contend in contend_list[:1]:
        #print(contend['displayValue'])
        youshengshu_name = contend['displayValue']
        youshengshu_code = contend['code']
        print(youshengshu_code)
        #有声书分类的全部url_youshengshu\
        url_youshengshu = url + '&subcategory=' + youshengshu_code
        print(url_youshengshu)
        result_1 = url_list(url_youshengshu,headers)
        #print(result_1)
        contend_list_1 = result_1['data']['metadata']
        for i in contend_list_1[:1]:
            #print(i['metaValues'])
            for j in i['metaValues']:
                print(j['displayName'])

