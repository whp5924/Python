# Fig 7.17:date.py
# !/usr/bin/pytho3
# Definition of class date
class Date:                       # 定义Date类
    "Class that represents date"  # 文档化字符串
    # class attribute lists number of days in each month
    daysPerMonth=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    def __init__(self,month,day,year): # 构建函数
        "Constructor for class Date"   # 文档化字符串
        if 0<=month<=12:
            self.month=month           # 判断非法月份
        else:
            raise ValueError("Invalid value for month: %d" % month )
        if year>=0:
            self.year=year             # 判断年份
        else:
            raise ValueError("Invalid value for year:%d" % year)

        self.day=self.checkday(day)    #判断日份
        # self.displaydate = "%2d/%2d/%2d" % (self.month, self.day, self.year)
        print("Date constructor:",end="")
        self.display()

    def display(self):
        "Print date information"
        print("%2d:%d:%d" % (self.month,self.day,self.year))

    def __del__(self):    # 自动执行析构函数 回收内存
        "Print message when called"
        print("马上回收内存啦...销毁中！！date object about to be destroyed:",end="")
        self.display()

    def checkday(self,testday):
        "Validates day of the month"
    # validate day , test for leap year
        if 0<testday<=Date.daysPerMonth[self.month]:
            return testday
        elif self.month==2 and testday==29 or (self.year % 400 ==0 or self.year % 4==0 and self.year != 0):
            return testday
        else:
            raise ValueError("Invalid day:%d for month: %" % (testday,self.month) )


