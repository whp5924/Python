# 向函数传递列表

from io import StringIO
from io import BytesIO
# 字符串内存中读取

f = StringIO('Hello world \n 来了、\n真的吗')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

g = BytesIO()
g.write('中文'.encode('UTF-8'))
g.write('hello world'.encode('utf-8'))
print(g.getvalue())