#
# Fig 9.8 fig09_08_02.py
import math
from fig09_08 import Point

class Circle(Point):
    def __init__(self,x=0,y=0,radiusValue=0):
        Point.__init__(self,x,y)
        self.radius=radiusValue

    def area(self):
        return math.pi * self.radius ** 2
    def __str__(self):
        return "坐标中心=(%s) 半径=%0.2f" % (Point.__str__(self),self.radius)



def main():
    circle=Circle(37,43,2.5)
    print("x的坐标值:",circle.x)
    print("y的坐标值:",circle.y)
    print("半径值:",circle.radius)
    print(circle)
    print("面积:",round(circle.area(),2))
    circle.x=2
    circle.y=2
    circle.radius=4.25
    print(circle)
    print("新面积:",round(circle.area(),2))
    print("新的坐标点:",Point.__str__(circle))    #可以调用基类的实例变量 将Circle类的对象作为Point类的一个对象输出
                                                  # 派生类对象用作基类对象

if __name__=="__main__":
    main()

