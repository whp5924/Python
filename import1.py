#import
# import 模块名1 [as 别名字】,模块名2 [as 别名2],......会导入指定的模块所有成员(包括变量、函数、类) 当使用时 用模块名作前缀.成员名
# from 模块名1 import 成员名1 [as 别名1],成员名2 [as 别名2],..... 导入的是模块中指定的成员,不是全体成员。当使用时，不用加前缀，直接使用成员名
# 直接直接
# *****module
# recursive call 或recursion step递归 return
import math,random
global summ11
def recursive1(number):

     sum1=1
     if number<=1:
        return sum11
     else:
        for counter in range(2,number+1):
            sum1=sum1*counter
            sum11=sum1
            print('%d! %d' % (counter,sum11))
#            return sum11
# for counter in range(2,6):
#     sum1=sum1*counter
#print(recursive1(5))
recursive1(5)

