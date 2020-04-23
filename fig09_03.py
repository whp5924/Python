#
# 基类 派生类
import math
class Point:
    def __init__(self,xValue=0,yValue=0):
        self.x=xValue
        self.y=yValue
class Circle(Point):
    def __init__(self,x=0,y=0,radiusValue=0):
        Point.__init__(self,x,y)
        self.radius=float(radiusValue)
    def area(self):
        return math.pi * self.radius ** 2

print(Point.__bases__)
print(Circle.__bases__)
print("类Point是类Circle的子类",issubclass(Point,Circle))
print("类Circle是类Point的子类",issubclass(Circle,Point))
b1=Point(10,30)
a1=Circle(12,34,2.7)
print("对象a1是类Point的一个对象:",isinstance(a1,Point))
print("对象a1是类Circle的一个对象:",isinstance(a1,Circle))
print("对象b1是类Point的一个对象：",isinstance(b1,Point))
print("对象b1是类Circle的一个对象:",isinstance(b1,Circle))
print("圆的面积是:",round(a1.area(),2))