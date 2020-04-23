# 自定义类
# Fig. 8.1:PhoneNumber.py
# Representation of phone number of USA format: (xxx)-xxx-xxx
class phonenumber:
    "Simple class to represent phone number in USA format:" # 文档化字符串
    def __init__(self,number):
        "Accepts string in form (xxx) xxx-xxxx"             # 文档化字符串
        self.areaCode=number[0:3]
        self.exchange=number[3:6]
        self.line=number[6:]
    def __str__(self):
        "定义'魔法'方法,字符串的信息"
        return "(%s) %s-%s " % (self.areaCode,self.exchange,self.line)
def test():
    newNumber=input("Enter phone number in the form (123) 456-7890:")
    phone=phonenumber(newNumber)
    print("The phone number is :",phone)

#print(dir(__name__))7777777777777777
if __name__=="__main__":
    test()
