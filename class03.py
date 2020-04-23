#
class person:

    def __init__(self, name, age, height, weight, money):  # 构造函数;
        # 定义属性
        self.name = name
        self.age = age
        self.__height = height
        self.weight = weight
        self.__money = money
    def say(self):
        print("hello! my name is %s,\ni am %d years old,\nI am height is %d,\nI am weight is %d " % (self.name,self.age,self.__height,self.weight))

#不被外部直接访问；相当于_Person__money
#通过内部的方法，去修改私有属性
#通过自定义的方法实现对私有属性的赋值与取值
    def setMoney(self,money):#对私有属性的赋值
#数据过滤
        if money < 0:
            monry = 0
        else:
            self.__money = money
    def getMoney(self):#对私有属性的取值
        return self.__money
    def get_height(self):
        return self.__height
    def set_height(self,height):
        self.__height=height




