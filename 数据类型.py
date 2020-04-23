#
#
'''
    在Python3以后，字符串和bytes类型彻底分开了。字符串是以字符为单位进行处理的，bytes类型是以字节为单位处理的。
    bytes数据类型在所有的操作和使用甚至内置方法上和字符串数据类型基本一样，也是不可变的序列对象。
    bytes对象只负责以二进制字节序列的形式记录所需记录的对象，至于该对象到底表示什么（比如到底是什么字符）
    则由相应的编码格式解码所决定。
    Python3中，bytes通常用于网络数据传输、二进制图片和文件的保存等等。可以通过调用bytes()生成bytes实例，
    其值形式为 b'xxxxx'，其中 r'xxxxx' 为一至多个转义的十六进制字符串,(单个x的形式为："\\0x12"，其中\0x为小写的
    十六进制转义字符，12为二位十六进制数）组成的序列，
    每个十六进制数代表一个字节（八位二进制数，取值范围0-255），对于同一个字符串如果采用不同的编码方式生成bytes对象，
    就会形成不同的值.
    编码：string.encode(encoding='编码类型)   以编码类型解码字符串
    解码: bytes.decode() 或 b'字符串'.decode()   直接以默认的UTF-8编码解码bytes成string


'''
t=frozenset('bookshop')
print(type(t))
print(t)
frozenset({'h', 'o', 's', 'b', 'p', 'k'})
# bytes object
b = b"example"
print(type(b))
print(b)
# str object
s = "example"

# str to bytes
sb = bytes(s, encoding = "utf8")
print(sb)
# bytes to str
bs = str(sb, encoding = "utf8")
print(bs)
# an alternative method
# str to bytes
sb2 = str.encode(s)
print(sb2)

# bytes to str
bs2 = bytes.decode(sb2)
print(bs2)