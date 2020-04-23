# Fig:8.3:TimeAccess.py
# Class Time with customized attrbute access
class Time:
    "Class Time with customized attrbute access"
    def __init__(self,hour=0,minute=0,second=0):
        "Time constructor initialized each data member to zero"
        # each statement invokes __str__
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __setattr__(self,name,value):
        "客户将值指派给对象的:"
        if name=="hour":
            if 0<=value<=24:
                self.__dict__["__"+name]=value  # 插入字典 self.__dict__["__"+name]
            else:
                raise ValueError("Invilad hour value:%d" % value)
        elif name=="minute" or name=="second":
            if 0<=value<=60:
                self.__dict__["__"+name]=value
            else:
                raise ValueError("Invilad %s value:%d" % (name,value))
        else:
            self.__dict__[name]=value
    def __getattr__(self,name):
        "从对象名称获取对象属性值"
        if name=="hour":
            return self.__hour
        elif name=="minute":
            return self.__minute
        elif name=="second":
            return self.__second
        else:
            raise AttributeError("输入属性错误:",name)

    def gethour(self):
        return self.__hour
    def getminute(self):
        return self.__minute
    def getsecond(self):
        return self.__second
    def settime(self,hour1,minute1,second1):
        self.sethour(hour1)
        self.setminute(minute1)
        self.setsecond(second1)
    def sethour(self,hour1):
        if 0<=hour1<=24:
            self.__hour=hour1
        else:
            raise ValueError("Invalid hour value: %d" % hour1)
    def setminute(self,minute1):
        if 0<=minute1<=60:
            self.__minute = minute1
        else:
            raise ValueError("Invalid minute value: %d" % minute1)
    def setsecond(self,second1):
        if 0<=second1<=60:
            self.__second=second1
        else:
            raise ValueError("Invalid second value: %d" % second1)


    def __str__(self):
        "魔法方法，返回格式化字符串"
        return "%2d:%2d:%2d" % (self.__hour,self.__minute,self.__second)

#if __name__=="__main__":
time1=Time(11,45,34)
print(time1)
print(time1.hour,time1.minute,time1.second)
time1.setsecond(20)
time1.setminute(60)
time1.hour=23
print(time1.__dict__)
print(time1)
print(time1.__dict__["__hour"])











