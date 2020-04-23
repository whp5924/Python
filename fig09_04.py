#
# Fig.9.5 fig09_04.py
# 继承类、基类之间互相调用，必须实例变量 (self.******)命名
# class father():
#     def __init__(self):
#         self.name="laila....."
#     def fun1(self):
#         method = eval('self.' + 'ss' + '_db')
#         print(method)
#     def fun2(self):
#         tt=self.ss_dbb
#         print(tt)
# class son(father):
#     def __init__(self):
#         father.__init__(self)
#         self.ss_db="123456"
#         self.ss_dbb="1234567abcdef"
#     def getname(self):
#         print(self.name)
#         return self.name
#
#
#
# if __name__ == "__main__":
#     son = son()
#     son.fun1()
#     son.fun2()
#     son.getname()


class Employee:
    def __init__(self,first=0,last=0):
        self.first=first
        self.last=last
    def __str__(self):
        return "%s %s" % (self.first,self.last)
class HourlyWorker(Employee):
     def __init__(self,first,last,initHours,initWage):

         Employee.__init__(self,first,last)     #初始化实例变量
         self.Hours=float(initHours)
         self.Wage=float(initWage)
     def getpay(self):
         return self.Hours * self.Wage

     def __str__(self):
         return "%s is an hourly worker with pay of $%0.2f " % (Employee.__str__(self),self.getpay())


# # 实例化小时工
hourly=HourlyWorker("刘","某某",40,10)
# 调用字符串的几种方法
# 隐式调用
print("隐式调用的几种方法: " , end="")
print(hourly)
# 显示调用 绑定方法
print("显示绑定调用对象:  ",hourly.__str__())
# 显示调用 非绑定方法
print("显示非绑定调用对象:",HourlyWorker.__str__(hourly))


