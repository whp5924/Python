# Fig 8.10: RationalNumber.py
# Definition of class Rational
# 引用类的属性进行数值运行时，注意类定义方法

def gcd (x,y):
    """Computers qreatest common divisor of two values"""
    while y:
        z=x
        x=y
        y=z%y
    # while x:
    #     z=y
    #     y=x
    #     x=z%x
    # print("最大公约数:",y)
    return x
class Rational():                                  # 有理数约分类
    """Representation of rational number"""
    def __init__(self,top=1,bottom=1):
        """Initializes Rational instance"""
        # do not allow 0 denominator
        if bottom == 0:
            raise ZeroDivisionError("Cannot have 0 denominator")
        self.numerator = abs(top)  #分子绝对值
        self.denominator = abs(bottom) #分子绝对值
        self.sign = int((top * bottom) / (self.numerator*self.denominator))
        self.simplify()
        # print(self.sign)

    # 有理数约分
    def simplify(self):
        """Simplifices a Rational number"""
        common=gcd(self.numerator, self.denominator)   # 接收最大公约数
        self.numerator /= common
        self.denominator /= common
        # print("分子:", self.numerator,end="")
        # print("分母:", self.denominator ,"\n")



    def __neg__(self):                                        # 对一元否定运算符进行重载
        """OVERLOADED ADDITION OPERATOR"""
        return Rational( - self.sign * self.numerator , self.denominator )
    def __sub__(self,other):                                  # 对二元减法运算符进行重载(先进行一元否定动算符重载，再进行二元加法运算符重载
        """Overloaded subtraction operator"""
        return self + (-other)
    def __add__(self,other):                                   # 对二元加法运行符进行重载
        return Rational(self.sign*self.numerator*other.denominator + other.sign*other.numerator*self.denominator,
                        self.denominator*other.denominator)


    def __mul__(self,other):
        """Overloaded multiplication operator"""
        return Rational(self.numerator * other.numerator, self.sign * self.denominator * other.sign * other.denominator)
    #
    def __div__(self,other):
        return Rational (self.numerator * other.denominator,self.sign * self.denominator * other.sign * other.numerator)
    #
    def __truediv__(self,other):
        return self.__div__(other)
    #
    def __eq__(self,other):
        return (self-other).numerator == 0
    #
    def __lt__(self,other):
         return (self-other).sign < 0
    #
    def __gt__(self,other):
        return (self-other).sign > 0
    #
    def __le__(self,other):
        return (self<other) or (self==other)
    #
    def __ge__(self,other):
        return (self > other) or (self == other)
    #
    # def __ne__(self,other):
    #     return  not (self==other)
    # #
    def __abs__(self):                                  # 自定义绝对值特殊方法
        return Rational(self.numerator,self.denominator)
    #
    def __str__(self):

        if self.sign == -1:
            signString ="-"
        else:
            signString=""
        if self.numerator ==0:
            return "0"
        elif self.denominator ==1:
            return  "%s%d" % (signString,self.numerator)
        else:
            return "%s%d/%d" % (signString, self.numerator,self.denominator)
    #
    # def __int__(self):
    #     return self.sign * divmon(self.numerator,self.denominator)
    # #
    # def __float__(self):
    #     return self.sign * float(self.numerator) / self.denominator
    #
    # def __coerce__(self,other):
    #     if type(other)==type(1):
    #         return (self,Rational(other))
    #     else:
    #         return None


# # from RationalNumber import Rational
rational1=Rational(35,70)
rational2=Rational(15,70)
rational3=Rational(-20,60)
print("rational1:" , rational1)
print("rational2:" , rational2)
print("rational3:" , rational3)
# x1 = rationa11 + rationa12 / rational3
# print(rationa11,"/","(",rational3,")","=",x1)
print(rational3-abs(rational3))

# print("2222222", rational1 == rational2 )
