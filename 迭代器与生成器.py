# 迭代器和生成器
# 迭代器是访问集合的一种方式。
# 迭代器是一个可以记住遍历的位置的对象
# 迭代器对象从集合的第一个元素开始访问，直到所有元素被访问完结束
# 迭代器只能往前不能后退
# 迭代器基本方法: iter(),next()
# 字符串、列表、元组对象都可用于创建迭代器
# 例：
import  sys
# list=[11,12,13,14,15,16]
# it=iter(list)  #创建迭代器对象
# print(next(it))
# print(next(it))
# 迭代器可以使用常规的for 语句进行遍历
# for i in it:
#     print("迭代器输出打印:",i)
# 也可以用netx()访问
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()
# 迭代器同样可以作用到类，__iter__(),__next__()
# __iter__ 方法返回一个特殊的迭代器对象，这个迭代器实现__next()方法并通过StopIteration 异常标识迭代的完成
# __next__会返回一个迭代器对象
# 创建一个返回数字的迭代器：初始值为1,逐步递增1
# class MyClass:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# myclass=MyClass()
# x=iter(myclass)
# print(next(x))
# print(next(x))
#------------------------------------------------------------------------------------------------------#
# 生成器







