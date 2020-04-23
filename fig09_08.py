#
# Fig 9.6: fig09_08.py
#
class Point:
    name="*******"
    def __init__(self,xValue,yValue):
        self.x=xValue
        self.y=yValue

    def __str__(self):
        return "%d,%d" % (self.x,self.y)

if __name__=="__main__":

# 给类对象赋值，必须是类名赋值，用类对象赋值，只会实例化新类
    point=Point(75,115)
    print("x的坐标点:",point.x)
    print("y的坐标点:",point.y)
    print(Point.name)
    print("原坐标点值:",point)
    point.x=10   # 实例变量赋新值
    point.y=10
    print("新坐标点值:",point)
