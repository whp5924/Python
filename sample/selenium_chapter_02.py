#

# 0. 框架
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from lxml import etree


# 1. 确立url和headers
url='https://wenku.baidu.com/view/2af6de34a7e9856a561252d380eb6294dd88228d.html#'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
# 2. 构建浏览器 并实例化
browser=webdriver.Chrome()
browser.get(url)    #请求网页
time.sleep(5)      #等待网页加载完数据

# 查找目标元素上方适应位置的元素
#scroll_add_down=browser.find_element_by_css_selector("div.try-end-fold-page > div.fold-page-text")
#WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"吧_百度贴吧")]')))
scroll_add_down=browser.find_element_by_class_name('read-all')
browser.execute_script('arguments[0].scrollIntoView();',scroll_add_down)

try:
    #browser.find_element_by_css_selector('div.try-end-fold-page > div.fold-page-text span').click()
    browser.find_element_by_class_name('read-all').click()
    time.sleep(5)
except Exception as e:
    print('没有找到')
html=''
a=0
# while True:
#         #print(browser.page_source)
#     html=html+browser.page_source
#
#     browser.execute_script("window.scrollBy(0,1080)")
#     time.sleep(3)
#     #print(type(html))
#     if a >8:
#         break



