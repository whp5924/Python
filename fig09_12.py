#
# Fig 09.12 fing09_12.py
#
# 静态方法演示
#

class Employee:
     #创建类对象的数量  类变量
    numberofEmployees=0
    maxEmployees=5      #最大员工数        类变量
    @staticmethod
    def isCrowded():
        
        return Employee.numberofEmployees>Employee.maxEmployees

    # print(Employee.isCrowded())
    #iscrowded=isCrowded()
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def __del__(self):
        Employee.numberofEmployees-=1
    def __str__(self):
        return "%s %s" % (self.first,self.last)
def main():
    answers=["No","Yes"]
    employeeList=[]
    print("Employee is crowded ?")
    print(answers[Employee.isCrowded()])
    print("Create 11 Object of class Employee.....")
    for i in range(7):
        Employee.numberofEmployees+=1
        employeeList.append(Employee("John ","Doe " + str(i)))
        print("第%s位" % i,employeeList[i])
        print("Employee is Crowded?")
        print(answers[employeeList[i].isCrowded()])

    print("Remove one employee.")
    del employeeList[0]
    print("Employee are crowded ?",answers[Employee.isCrowded()])
    del employeeList[0]
    print("Employee are crowded ?", answers[Employee.isCrowded()])

if __name__=="__main__":
    main()



