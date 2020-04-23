class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Course:
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
    def tell_info(self):
        print('<%s %s %s>' %(self.name,self.period,self.price))

class Teacher(People):
    def __init__(self,name,age,sex,job_title):
        People.__init__(self,name,age,sex)
        self.job_title=job_title
        self.course=[]
        self.students=[]


class Student(People):
    def __init__(self,name,age,sex):
        People.__init__(self,name,age,sex)
        self.course=[]


eg=Teacher('eg',18,'male','霸道金牌讲师')
s1=Student('牛二',18,'female')

python=Course('python','3mons',3000.0)
linux=Course('python','3mons',3000.0)

#为老师eg和学生s1添加课程
eg.course.append(python)
eg.course.append(linux)
s1.course.append(python)

#为老师eg添加学生s1
eg.students.append(s1)
print(eg.__dict__)

#使用
# for obj in eg.course:
#     obj.tell_info()