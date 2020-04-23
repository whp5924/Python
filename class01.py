# 在类中定义了私有变量，类的实例不能直接访问，但是又想使用或修改私有变量的值，这时候就需要用到get/set方法
class student:
    age=10
    def __inint__(self):
        pass
    def get_student(self):
        return self.age
    def set_student(self,age):
        if isinstance(age,int) and 0<age<100:
           self.age=age
        else:
            input('请输入正确的年龄：')
            self.age=age

stu=student()
print(stu.get_student())
stu.set_student(110)
print(stu.get_student())





