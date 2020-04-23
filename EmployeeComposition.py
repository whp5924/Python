# Difinition of Employee class with composition rembers
from date import Date
class Employee:
    "Employee class with Date attributes" # 文档化字符串
    def __init__(self,firstName,lastName,birthMonth,birthDay,
                 birthYear,hireMonth,hireDay,hireYear):
        "Constructor for class Employee"
        self.birthDate=Date(birthMonth,birthDay,birthYear)
        self.hireDate=Date(hireMonth,hireDay,hireYear)
        self.firstName=firstName
        self.lastName=lastName
        print("Employee constructor: %s %s" % (self.lastName,self.firstName))
    def __del__(self):
        "Called before Employee destructor"
        print("开始清理内存.......")
        print("Employee object about to be destroyed:%s,%s" % (self.firstName,self.lastName) )
    def display(self):
        "Print Employee infomation"
        print("Hire Date:",end="")
        self.hireDate.display()
        print("Birth date ",end="")
        self.birthDate.display()
