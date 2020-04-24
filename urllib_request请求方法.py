# 实例  key=lambda  变量：变量[维数]
import urllib.request
from http import cookiejar
import gzip
from io import StringIO
from io import BytesIO
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br'
}
url = 'http://www.sina.com'
#url = "http://www.163.com"
#url = 'http://www.zhihu.com/'

request = urllib.request.Request(url)
request.add_header("user-agent",headers['user-agent'])
request.add_header('accept-encoding','gzip, deflate, br')
response = urllib.request.urlopen(request)
print(response.info())
if response.info().get('Content-Encoding') == 'gzip':
    buf = BytesIO(response.read())
    f = gzip.GzipFile(fileobj=buf)
    html = f.read().decode()
    print(html)

# if response.info().get('Content-Encoding') == 'gzip':
#     buf = BytesIO(response.read())
#     f = gzip.GzipFile(fileobj=buf,mode='rb')
#     data = f.read()
#     print(data.decode())


