# Time 实例 如果类定义了属性的访问方法，在实例中按定义的方法，访问属性
# -*- coding:UTF-8 -*-
from Time1 import Time
def printtimevalue(timetoprint):
    print(timetoprint.printMilitary())
    print(timetoprint.printStandard())

time1=Time()
time2=Time(5)
time3=Time(9,34,45)
time4=Time(23,56,34)
printtimevalue(time1)
printtimevalue(time2)
printtimevalue(time3)
printtimevalue(time4)
