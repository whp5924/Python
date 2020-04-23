#
# Fig 9.8 fig09_08_02.py
import math
from fig09_08 import Point
from fig09_08_02 import Circle

class Cyliner(Circle):
    def __init__(self,x,y,radius,heigh): # 初始化圆柱体的四个参数
        Circle.__init__(self,x,y,radius)
        self.heigh=float(heigh)
    def area(self):                      # 计算圆柱体的表面积

        return 2* Circle.area(self) + 2 * math.pi * self.radius * self.heigh

    def volume(self):
        # return math.pi * self.radius ** 2 * self.heigh
        return Circle.area(self) * self.heigh
    def __str__(self):
        return "底面圆参数:%s,圆柱体的高%0.2f" % (Circle.__str__(self),self.heigh)


def main():
    cyliner=Cyliner(12,23,2.5,5.7)
    print("x的坐标:",cyliner.x)
    print("y的坐标:", cyliner.y)
    print("圆的半径:",cyliner.radius)
    print("圆柱体的高:", cyliner.heigh)
    print("参数:",cyliner)
    print("圆的底面积:",Circle.area(cyliner))
    print("圆柱体的体积:",cyliner.volume())
    # 重新实例化
    cyliner.heigh=10
    cyliner.radius=4.25
    cyliner.x,cyliner.y=2,2
    print("重新打印圆柱体的参数:",cyliner)
    print("圆柱体的底面积:",cyliner.area())
    print("圆柱体的体积:",cyliner.volume())
    print("点类定义字符串:",Point.__str__(cyliner))
    print("圆类定义字符串:",Circle.__str__(cyliner))
    print("圆柱体定义字符串:",Cyliner.__str__(cyliner))

if __name__=="__main__":
    main()
