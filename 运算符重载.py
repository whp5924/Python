#
"""
1. __neg__  对一元否定运算符进行重载
    def __neg__(self):             # -field python解释器会生成如下方法调用 field.__neg__(self)
    return Rational( - self.sign * self.numerator , self.denominator )
2. __add__  对二元运算符加法进行重载
    def __add__(self,other)        # field1 + field2   field1.__add__(field2) 返回新对象
    return self+other
3. __sub__  对二元运算符减法进行重载
    def __sub__(self,other)
    return self + (-other)
4. __mul__  对二元运算符乘法进行重载
    def __mul__(self,other)
    return self * other
5. __truediv__ 对二元运算符除法进行浮点数重载
    def __fruediv__(self,other)
    return self.__div__(other)
6. __div__(self,other) 对二元运算符除法进行重载
    def __div__(self,other)
    return self / other
7. __eq__(self,other)  对二元运算符等于进行重载
    def __eq__(self,other)
    return self - other == 0
8. __lt__(self,other)  对二元运算符小于进行重载
    def __lt__(self,other)
    return self-other < 0
9. __gt__(self,other)  对二元运算符大于进行重载
    def __gt__(self,other)
    return self-other > 0
10. __le__(self,other)  对二元运算符小于等于进行重载
    def __le__(self,other)
    return self < other< or self == other
11. __ge__(self,other)  对二元运算符大于等于进行重载
    def __ge__(sele,other)
    return self > other or self == other
12. __ne__(self,other)  对二元运算符不等于进行重载
    def __ne__(self,other)
    return not (self == other)
13. __abs__(self)   特殊方法，重载绝对值运算符
    def __abs__(self)
    return __abs__(self)
14. __str__(self)  对字符串输入进行重载 返回对字符串的表示
    def __str__(self)
    return 返回对字符串的表示，可以是格式化后的字符串






"""