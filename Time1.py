# Fig. 章节 7.1: Time1.py
# 面向对象数据 OOP
# class Time:
#     """Time abstract data type (ADT) definittion"""  # 文档化字符串
#     annotations={"1":1,"2":2}
#     def __init__(self): # 构建函数 初始化对象属性 __名称__（语法) 返回值：None 构造函数不返回None
#                         # 就属于严重的运行时错误, 对象引用参数 (self). 将所有方法的第一个参数命名为self
#         """Initializes hour,minute and second to zero""" # 文档化字符串
#         self.hour=0     # 将属性绑定类命名空间 同时将属性初始化
#         self.minute=0
#         self.second=0
#     def printMilitary(self): # 创建类的方法(类的函数) 军事化时间 无参返回
#         """Print object of class Time in military format""" # 文档化字符串
#         militaryTime=""
#         militaryTime+="%.2d:%.2d:%.2d" % (self.hour,self.minute,self.second)
#        # print('%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second))
#         return militaryTime
#
#     def printStandard(self): # 创建类的方法  标准化时间 无参返回
#         """Print object of class Time in strand format"""   #  文档化字符串
#         standardTime="" # 初始化标准时间
#         if self.hour==0 or self.hour==12:
#             standardTime+='12:'
#         else:
#             standardTime+='%d:' %  (self.hour % 12)
#         standardTime+="%.2d %.2d" % (self.minute,self.second)
#         if self.hour<12:
#             standardTime+="AM"
#         else:
#             standardTime+='PM'
#         return standardTime
#         # print(standardTime)
# 控制属性的访问
class Time:
    """Time abstract data type (ADT) definittion"""  # 文档化字符串
    annotations={"1":1,"2":2} # __annotations__ 实例
    def __init__(self,hour=0,minute=0,second=0): # 构建函数 初始化对象属性 __名称__（语法) 返回值：None 构造函数不返回None
                        # 就属于严重的运行时错误, 对象引用参数 (self). 将所有方法的第一个参数命名为self
        """Initializes hour,minute and second to zero""" # 文档化字符串
        # self.__hour=0     # 将属性绑定类命名空间 同时将属性初始化
        # self.__minute=0
        # self.__second=0
        self.settime(hour,minute,second)
    def settime(self,hour,minute,second):
        "Set value of hour,minute,second"
        self.sethour(hour)
        self.setminute(minute)
        self.setsecond(second)
    def sethour(self,hour):
        "Set hour value"
        if 0<= hour <=24:
            self.__hour=hour
        else:
            self.__hour=hour % 24

        # else:
        #     raise ValueError("Invalid hour value: %d" % hour)
    def setminute(self,minute):
        "Set minute value"
        if 0<=minute<=60:
            self.__minute=minute
        else:
            raise ValueError("Invalid minute value: %d" % minute)
    def setsecond(self,second):
        "Set sencod value"
        if 0<=second<=60:
            self.__second=second
        else:
            raise ValueError("Invalid second value: %d" % second)
    def gethour(self):
        "Get hour value"
        return self.__hour
    def getminute(self):
        "Get minute value"
        return self.__minute
    def getsecond(self):
        "Get value second"
        return self.__second

    def printMilitary(self): # 创建类的方法(类的函数) 军事化时间 无参返回
        """Print object of class Time in military format""" # 文档化字符串
        militaryTime="" # 初始化军事时间
        militaryTime+="%.2d:%.2d:%.2d" % (self.__hour,self.__minute,self.__second)
       # print('%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second))
        return militaryTime

    def printStandard(self): # 创建类的方法  标准化时间 无参返回
        """Print object of class Time in strand format"""   #  文档化字符串
        standardTime="" # 初始化标准时间
        if self.__hour==0 or self.__hour==12:
            standardTime+='12:'
        else:
            standardTime+='%02d:' %  (self.__hour % 12)
        standardTime+="%.2d:%.2d" % (self.__minute,self.__second)
        if self.__hour<12:
            standardTime+="AM"
        else:
            standardTime+='PM'
        return standardTime

