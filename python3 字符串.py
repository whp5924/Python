#
# 字符串是python中常用的数据类型： 使用''或""来创建字符串
# 字符串转义字符
str0="""
\   续行符
\\  反斜杠符号
\'  单引号
\"  双引号
\a  响铃
\b  退格
\000    空
\n  换行
\v  纵向制表符
\t  横向制表符
\r  回车
\f  换页
\x23 十六进制数 \yy yy代表的字符
"""
# 字符串运算符
str01="""
+   字符串连接
*   重复输出字符串
[]  通过索引获取字符串中的字符
[:] 截取字符中的一部分，遵循左闭右开原则
in  成员运算符: 如果字符串中包含给定的字符串，返回Ture
not in  成员运算符:  如果字符串中不包含给定的字符串，返回Ture
r/R 原始字符串:所有的字符串都是直接按照字面的意思来使用,没有转义特殊或不能打印的字符
%   格式化字符串
"""
# 格式化字符串
str02="""
%c  格式化字符或ASCII码
%s  格式化字符串
%d  格式化整数
%u  格式化无符号整型
%o  格式化无符号八进制数
%x  格式化无符号十六进制数
%X  格式化无符号十六进制数 大写
%f  格式化浮点数,可指定小数点后的精度
%e  用科学计数法格式化浮点数
%p  用十六进制数格式化变量的地址
"""
str03="""
*   定义宽度或者小数点精度
-   左对齐
+   在正数前面加'+'
<sp>    在正数前面加空格
#   在八进制数前面显示'0',在十六进制数前面显'0x'
0   显示数字前面填充'0'而不是空格
%   %%输出一个单一的'%'
(var0   映射变量
m.n     m是显示的最小总宽度，n是小数点后的位数
55
"""
# 字符串的""""""三引号
str04="""
允许一个字符串多行，字符串中可以包含换行符、制表符以及其它特殊字符。
输出字符串是所见即所得。
"""
str000="""
f-string
语法:
    f'string {}' {内} 替换变量
    
 
string.format
语法:
   通过{}或:来实现的
例："""
# 1. format 可以按受不限个参数,位置可以不按顺序
#   a. 不设置指定位置，按顺序
# print('string{},{},{},{}'.format("I","ii","III","iiii"))
# #   b. 设置指定位置
# print('string{0}{1}'.format("I","ii"))
# print("string{1},{0}".format('I',"ii"))
# print("string{0},{1},{0}".format("I","ii"))

# 2. format 可以设置参数
#    a. 直接传参
#print("网站名:{name},网站地址:{url}".format(name="xxIxx",url="www.163.com"))
#    b. 通过字典传参
# dict={"name":"xxIxx","url":"www.163.com"}
# print("网站名:{name}:网站地址:{url}".format(**dict))
# *** *args和**kwargs  都代表1个或多个参数
# *args  传入tuple元组类型的无名参
# def test(*args):
#     print(args)
#     for i in args:
#         print(i)
# test(1,2,3,4)
# ** kwargs  传入dict类型的参数
# def test(**kwargs):
#     print(kwargs)
#     key=kwargs.keys()
#     value=kwargs.values()
#     print(key)
#     print(value)
# test(a=1,b=2,c=3,d=4,e=5)
#    c. 通过列表索引传递参数 0[]其中的'0'是必须的
# list=['xxIxx','www.163.com','我的','你的']
# print("网站名:{0[0]},网址地址:{0[3]}".format(list))

st='''
# string.format()
# 如: "string {0}...{n}".format('2','22')
print("{0},{1}{0},{0}".format("2","45"))
'''
#   另外一种格式化输出
#---------------------------------------
#   字符串内建函数  可以理解为字符的方法
str1="""
1.  capitalize()    返回原始字符串首字母大写,其它字母小写.
                    首字符如果是非字母，后续的首字母不会转换成大写，其余字符会转成小写.  
    语法：
        str.capitalize()
    无参
    返回值:返回一个首字母大写的字符串

2.  center(width,[fillchar])  返回一个指定宽度width的居中字符串
    语法：
        str.center(width[,fillchar])
    参数：
        width   居中的字符串
    可选参数:
        fillchar    填充的字符串
    返回值:返回一个指定宽度width居中的字符串,如果width小于字符串宽度直接返回字符串，否则使用fillchar去填充.
    a) 若width小于字符串的长度，直接输出字符串，不会截断
       str='I am a student'
       print(str.center(4,'*')
       <<< I am a student
    b) fillchar 默认是空格
       str='I am a student'
       print(str.center(40)
       <<<                    I am a student
    c) fillchar 只能是单个字符
       str='I am a student'
       print(str.center(40,"*=")
       会有TypeError: The fill character must be exactly one character long 提示错误
3. count() 返回子字符串在原始字符串中出现的次数
    语法：
        str.count(str[,beg[,end]])
    参数：
        str 单字符或字符串
    可选参数:
        beg 字符串开始搜索的位置,默认为第一个字符，第一个字符的索引值为0
        end 字符串结束搜索的位置，字符串第一个字符索引值为0,结束字符默认为最后一个字符
    返回值:返回该字符串str在字符串string中出现的次数
4. encode(encoding,errors)  返回指定编码encoding格式编码字符串
    语法:
        str.encode(encoding='UTF-8',errors='strict')
    参数:
        encoding    指定的编码格式
    可选参数:       
        errors      设置不同的错误的处理方案 默认为strict 引起一个UnicodeError错误. 
    返回值: 返回指定的字符串
        
5. endswith(suffix[,beg,[end]]  用于判断字符串是否以指定后缀结束, 如果是 返回 True
    语法:
        str.endswith(suffix[,beg[,end]])
    参数: suffix 指定的后缀
    可选参数:
          beg   字符串中的开始位置
          end   字符串结束位置  原则上以左闭右开 不包含end的值
    返回值: True或Flase
6. expandtabs(tabsize=8) #expandtabs()方法把字符串中的tab符号(\t)转为空格
    语法：
        str.expandtabs(tabsize=8)
    在 Python3 中规定制表符\t前面有多少字符，再计算补多少个空格,一般字符+空格为 4 的整数倍
---------------------------------------
str = "this is\tstring example....wow!!!"
 
print ("原始字符串: " + str)
print ("替换 \\t 符号: " +  str.expandtabs())
print ("使用16个空格替换 \\t 符号: " +  str.expandtabs(16))
--输出-------------------------------------
原始字符串: this is	string example....wow!!!
替换 \t 符号: this is string example....wow!!!
使用16个空格替换 \t 符号: this is string example....wow!!!

str11 = "this is\tstri\tng example....wow!!!"
str22 = "athis is\tstring example....wow!!!"
str33 = "athis is    string example....wow!!!"  # is 和 string 中间输入 4 个空格
print(str11)
print("a"+str11)
print(str22)
print(str33)
-输出-------------------------------------------------------------
this is	stri	ng example....wow!!!       # \t 前有 7 个字符，补充 1 个空格
athis is	stri	ng example....wow!!!   # \t 前有 8 个字符，补充 4 个空格
athis is	string example....wow!!!
athis is    string example....wow!!!       # 4 个空格的效果，做对比

    参数:tabsize=8 默认参数是8,但转换空格是4的倍数

7. find(str[,beg[,edn]])    find()方法是检测字符串string中是否包含子字符串str.
                            如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
                            如果指定范围内包含子字符串str，返回的是子字符串str在字符串string中的起始位置。
                            如果不包含索引值，返回-1。
    find()语语：
        string.find(str,beg=0,end=len(string))
    参数:
        str 指定检索的子字符串
        beg 开始检索的位置    # 遵循左闭右开原则
        end 结束检索的位置 默认为字符串string的长度
    返回值:
        如果检索成立，则返回检索成立的位置，否则返回-1
8. index(str[,beg[,end]])   index()方法是检索字符串string中是否包含子字符串str.  
                            如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
                            该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
    语法:
        string.index(str[,beg[,end]])
    参数:
        str 指定检索的子字符串
        beg 开始检索的位置   # 遵循左闭右开原则
        end 结束检索的位置
    返回值:
        如果检索成立，则返回检索成立的位置，否则抛出异常.
9. isalnum()   isalnum()方法检测字符串是否由字母和数字组成. 其中字符也包括文字。
    语法:
        str.isalnum()
    参数：
        无
    返回值:
        如果字符串string中有一个字符,并且所有字符由数字或字母组成，则返回True,否则返回Flase.
10. isalpha()   isalpha()方法检测字符串是否由字母和文字组成.
    语法:
        str.isalpha()
    参数:
        无参
    返回值:
        如果字符串string中有一个字符，并且所有字符由字母或文字组成，则返回True,否则返回False
11. isdigit()    isdigit()方法检测字符串是否由数字组成.
    语法:
        str.isdigit()
    参数:
        无参
    返回值:
        如果字符串string只包含数字，则返回True,否则返回False
12. islower()    islower()方法检测字符串string是否由小写字母组成.
    语法:
        str.islower()
    参数:
        无参
    返回值:
        如果字符串string中包含至少一个区分大小写的字符，并且所有这些区分大小写的字符都是小写,则返回True,否则返回False
13. isnumeric()  isnumerice(）检测字符串是否由数字组成.
                 数字可以是: Unicode数字、全角数字、罗马数字、汉字数字
                 如:
                    ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳
                    ⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂
                    ⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖
                    ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ
                    ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹ
                    ❶❷❸❹❺❻❼❽❾❿
                    ㈠㈡㈢㈣㈤㈥㈦㈧㈨㈩                      # 中文数字
                    ¹²³                                     # 上标数字
                    ₁₂₃                                    # 下标数字
                    ½⅓⅔¼¾                               #  几分之几
                      
    语法:
        str.isnumeric()
    参数:
        无参
    返回值:
        如果字符串string中只包含各类数字,返回True,否则返回False
14. isspace()    isspace()方法检测字符串stirng中只包含空白字符
    语法：
        str.isspace()
    参数:
        无
    返回值:
        如果字符串string中只包含空格,则返回True,否则返回False
    
    *** 注意，空白符包括: 空格、制表符\t、\n、\v、\r、\f等,但空串''不算空白符
            
15. istitle() istitle()方法检测字符串string中所有的单词拼写首字母是否为大写,且其它字母为小写.
    语法:
        str.istitle()
    参数:
        无
    返回值:
        如果字符串string中所有单词拼写首字母为大写,且其它字母为小写，则返回True,否则返回False

16. isupper()   isupper()方法检测字符string中所有字母是否为大写.
    语法:
        str.isupper()
    参数:
        无
    返回值:
        如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写,则返回True,否则返回False
    **注意,字符串中包含至少一个大写字符,很关键.
    ** string='A.....' string.isupper() 返回True

17. jion(seq)  jion(seq)的方法用于将序列seq中的元素以指定的字符串（含空串)连接成一个新的字符串string
    序列包含: 
        字符串、集合{}、元组、列表(列表中的各元素必须是字符串)、字典(字典中的键dict.keys或字典的值
        字典中的值dict.value,但值必须为字符串)
    语法:
        str.jion(seq)
    参数:
        列表序列 sequence
    返回值:
        将序列中的元素以指定的字符串连接成一个新的字符串
 
18. len() len()内置函数,用于返回对象的长度和元素个数
    语法:
        len(object)
    参数:
        object: 序列==字符串(string)、列表(list)或range、元组(tuple)
                集合==集合(set)、字典(dict)、冻结的集合(frozenset)  
    返回值:
        返回对象的长度
    
    ** 注意：len()不是字符串的方法.

19.ljust()  ljust（)方法返回一个字符串string, 左对齐，并使用指定字符填充至指定的宽度,如果指定宽度小于原字符串的宽度,
            则返回原字符串.
    语法:
        str.ljust(width[,fillchar]) 默认为空格
    参数:
        width   指定的宽度
        fillchar    指定的填充字符串
    返回值:
        返回一个新字符串,左对齐，并使用指定字符填充至指定宽度,如果指定宽度小于原字符串的宽度,则返回原字符串
         
20. lower()  lower()方法转换字符串中所有大写字符为小写。
    语法:
        str.lower()
    参数:
        无参
    返回值: 返回转换字符串中所有大写字符为小写字符
    
21. lstrip() 方法用于截掉字符串左侧空格或截掉从左侧开始以指定字符与原字符一一比对，一旦字符串字符不属于子串，则停止，并且返回字符串
    语法:
        str.lstrip(空格或str)
    参数:
        1. 参数为空，则返回截掉字符串的左侧的全部空格
        2. 参数为字符串 从字符串左侧开始，截掉字符串中的字符是属于指定字符串的字符，一旦字符串字符不属于子串字符，则停止，并且返回截掉后的字符串
    返回值: 返回截掉后的新字符串
    
    注意：截取的主体为原字符串，你指定字符集为提取对象，从左侧开始一个一个比对。 
          从左到右移除字符串的指定字符, 无字符集参数或None则从左侧移去空格，直到遇到非空格符停止，返回新字符串
          从左到右移除字符串的指定字符，有字符集参数时，从新原字符串左侧开始，一个一个字符与指定字符集比对，直到遇到不属于字符集字符停止，返回新字         符串         
 22. str.maketrans()  接受一个或两个参数
    语法：
        str.maketrans(str1,str2)  返回一个字典(字典的key和vale均用Unicode编码) 
    参数：
        1. str.maketrans(dict1) dict1为字典
           dict1={'a':"1",'b':'2','c':'3','d':'4'}
           str_st01=str.maketrans(dict1)
           st01="ab--cd"
           st02=st01.translate(str_st01)
        2. str.maketrans(str1,str2) str1、str2均为字符串，将str1和str2的各元素按次序关系构造字典,并用key和value值均用Unicode进行编码
            st1='abcdef'
            str2='123456'
            st0='a che gcba'
            str00=str.maketrans(st1,str2)
            s=st0.translate(str00)
        3. 三参数: 三个参数x,y,z 其中第三个参数必须是字符串,其字符映射后是None,即删除该字符。
                   如果z中的字符与x中的字符重复，则重复的字符在最终结果中会被删除。也就是说无论是否重复，只要有第三个参数，最终结果中有含
                   第三个参数字符的都将被删除。
                   删除后再按映射生成新的字符串。
            x = 'abcdefs'
            y = '1234567'
            z='ot'
            st='just do it'
            trantab = str.maketrans(x,y,z)
            print(st.translate(trantab))
            =========================
            x = 'abcdifs'
            y = '1234567'
            z='stj'
            s_t='just do it'
            # trantab = str.maketrans(x,y,z)
            # print(s_t.translate(trantab))
            for i in z:
                s_t=s_t.replace(i,'')
            print(s_t)
            x=str.maketrans(x,y)
            print(x)
            y=s_t.translate(x)
            print(y)

23. max()  max()返回字符串中最大的字母
    语法:
        max(str)
    参数：
        无参
    返回值：返回字符串中最大的字母
    
    # 大写字母在Unicode字符表中在小写字母的前面
                
24. min()  min()返回字符串中的最小字母
    语法：
        min(str)
    参数：
        无参
    返回值：
        min(str) 返回字符串中最小的字母

25. replace() replace(）方法把原字符串用新字符串替换，如果有第三个参数，则替换次数不能超过第三个参数的值
    语法:
        str.replace(oldstr,newstr[,x])
    参数：
        两个参数：用新字符串替换旧字符串
        三个参数: 用新字符串替换旧字符串，最替换的次数不能超过第三个参数的值
                   
26. rfind() 方法返回子字符串在字符串中出现的最高位置,如果没有则返回-1
    语法:
        str.rfind(str1[,beg[,end]])
    参数:
        1. str.rfind(str)   从字符串最左侧开始索引查找，返回最后一次出现的位置，如果没有找到返回-1
        2. str.rfind(str,beg)   从字符串指定位置beg开始索引查找，返回最后一次出现的位置，如果没有找到返回-1
        3. str.rfind(str,beg,end)   从字符串指定位置beg开始到end结束进行索引查找，返回最后一次出现的位置，如果没有找到返回-1
        beg end 为索引区间
    返回值：
        如果按索引找到，则返回最后一次出现的位置，反之返回-1

27. rindex() 方法返回子字符串在字符串出现的最高位，没有找到返回异常
    语法：
        str.rindex(str1[,beg[,end]])
    参数:
        1. str.rindex(str1) 从字符串最左侧开始索引查找str1, 返回最后一次出现的位置，如果没有找到返回异常
        2. str.rindex(str1,beg) 从字符串中按指定位置开始索引查找，返回最后一次出现的位置，如没有找到返回异常
        3. str.rindex(str1,beg,end) 从字符串中按指定区间开始索引查找，返回最后一次出现的位置，如没有找到返回异常

28. rjust() 方法用于返回一个新字符串，右对齐并按指定字符指定宽度进行填充，如果指定宽度小于原字符串，直接返回原字符串
    语法:
        str.rjust(width[,fillchar]
    参数:
        1. str.rjust(width)   以指定宽度右对齐并以空格填充并返回新字符,如宽度小于原字符，则直接返回原字符
        2. str.rjust(width,fillchar)  以指定宽度右对齐并以指定字符填充并返回新字符，如宽度小于原字符串，则直接返回原字符串

29. rstrip() 用于从右侧开始截掉字符串空格或以指定字符集子串的字符与原字符串一一比对，如果被包含则被截掉，
             直到字符不包含于原字符串停止，并且返回新字符串
             用于从右侧开始截掉空格字符串或指定字符,以指定字符集子字符与原字符串从右侧开始一一比对，被包含则截掉
    语法: 
        str.rstrip(str1)
    参数:
        1. str.rstrip()   从右侧开始截掉右侧空格字符串
        2. str.rstrip(str2) 从右侧开始截掉以指定字符集的字符
     
30. split()  用于字符串切片转列表,通过指定的字符对字符串进行切片，如果第二个参数有指定值，则切成n+1子字符串
             指定字符则自动从原字符删除
    语法:
        str.split(str1)
    参数:
        1. str.split()  以空格为分割符，对字符串进行切片,组成一个新的列表list
        2. str.split(' ',num) 以空格为分割符，对原字符串进行切片，切片数不超过num+1,组成一个新的列表
        3. str.split(str2)  以str2为分割符对字符串进行切片，组成一个新的列表   
        4. str.split(str2,num) 以str2为分割符对原字符串进行切片，切片数不超过num+1，组成一个新的列表
    返回值:
        返回一个以空格或指定字符为分割符的列表
    
31. splitlines() 方法返回以各行作为元素的列表 (\r \r\n \n)
    语法:
        str.splitlines(keepends) 默认为False
    参数:
        1. str.splitlines() 不保留换行符以每行作为列表元素 参数默认为False
        2. str.splitlines(True) 保留换行符以每行作为列表元素
    返回值:
        以依照行('\r',\r\n','\n')为分割符，以每行作为列表的元素

32. startwith() 用于检查字符串中是否以子串substr开头,是返回True,否则返回False
    语法:
        str.startwith(substr[,beg[,end]])
    参数:
        1. str.startwith(substr)   用于检查字符串是否以子串substr开头,是返回True,否则返回False
        2. str.startwith(substr,beg) 用于检查字符串是否以子串substr开头,并且从beg开头进行索引一一比对，是返回True,否则返回False
        3. str.startwith(substr,beg,end) 用于检查字符串是否以子串substr开头,并且从beg开头到end结束进行索引一一比对，是返回True,否则返回False
    返回值:
        用于检查字符串是否以子串substr开头，是返回True,否则False

33. strip() 方法用于截掉字符串头尾指定的字符(默认空格)或者字符序列
    语法:
        str.strip(substr)
    参数:
        1. str.strip()  用于截掉字符串头尾所有空格,并返回新字符串
                    ****默认清除字符串两边的空格. /n /r /t ' '
        2. str.strip(substr) 用于截掉字符串头尾并且是以字符序列一一比对索引,但并不局限单个字符,返回一个新的字符串
                             只要头尾包含指定的字符序列,都要删除
                    *********这个参数可以理解一个要删除的字符的列表，是否会删除的前提是从字符串最开头和最结尾是不是包含要删除的字符，
                             如果有就会继续处理，没有的话是不会删除中间的字符的
    
34. swapcase() 方法用于对字符串大小写字母进行转换
    语法:
        str.swapcasw()
    参数:
        无参
    返回值：
        对字符串的大小写字母进行转换

35. title()  方法用于返回'标题化'字符串，也就是说字符串所有单词的首字母为大写,其它字母为小写
    语法:
        str.title()
    参数:
        无
    返回值: 返回字符串所有单词首字母为大写,其它字母为小写

36. translate() 方法根据参数table给出的表转换字符串的字符,如有要过滤的字符,放在第三个参数里
    语法:
        str.translate(table[,deletechars)
        bytes.translate(table[,deletechars])
        bytesarry.translate(table[,deletechars])
    参数:
        1. str.translate(table) 
        2. str.translate(table,deletechars)
    返回值:
        根据参数给出的映射表转换字符串中的字符,并返回新字符串

37. upper() 将字符串的小写字母转换成大写字母
    语法:
        str.upper()
    参数:
        无参
    返回值:
        将字符串中的小写字母转换成大写字母

38. zfill() 返回指定宽度的字符串,右对齐,前面填0
    语法:
        str.zfill(width)
    参数:
        str.zfill(width)  
    返回值：
        返回指定宽度的字符串,右对齐,前面填0

39. isdecimal() 用于判断一个字符串是否只包含十进制字符 是返回True,否则返回False
    语法:
        str.isdecimal()
    参数:
        无参
    返回值:
        用于判断一个字符串是否只包含十进制字答,是返回True,否则返回False

    
        



    
 """
# !/usr/bin/python3
str11='\tThis is a test string. \t\t'
print("original string: %s" % str11)
print("Using strip: %s" % str11)

print('Using lstrip: %s' % str11)

