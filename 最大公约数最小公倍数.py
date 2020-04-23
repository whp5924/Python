#
"""
    几个整数中公有的约数，叫做这几个数的公约数；其中最大的一个，叫做这几个数的最大公约数。例如：12、16的公约数
有1、2、4，其中最大的一个是4，4是12与16的最大公约数，一般记为（12，16）=4。12、15、18的最大公约数是3，记为
（12，15，18）=3。
    几个自然数公有的倍数，叫做这几个数的公倍数，其中最小的一个自然数，叫做这几个数的最小公倍数。例如：4的倍数
有4、8、12、16，……，6的倍数有6、12、18、24，……，4和6的公倍数有12、24，……，其中最小的是12，一般记为[4，6]=
12。12、15、18的最小公倍数是180。

在解有关最大公约数、最小公倍数的问题时，常用到以下结论：
　　（1）如果两个自然数是互质数，那么它们的最大公约数是1，最小公倍数是这两个数的乘积。
　　      例如8和9，它们是互质数，所以（8，9）=1，[8，9]=72。
　　（2）如果两个自然数中，较大数是较小数的倍数，那么较小数就是这两个数的最大公约数，较大数就是这两个数的最小公倍数。
　　      例如18与3，18÷3=6，所以（18，3）=3，[18，3]=18。
　　（3）两个整数分别除以它们的最大公约数，所得的商是互质数。
　　      例如8和14分别除以它们的最大公约数2，所得的商分别为4和7，那么4和7是互质数。
　　（4）两个自然数的最大公约数与它们的最小公倍数的乘积等于这两个数的乘积。
　　      例如12和16，（12，16）=4，[12，16]=48，有4×48=12×16，即（12，16）× [12，16]=12×16。
    （5）GCD(a,b) is the smallest positive linear combination of a and b. a与b的最大公约数是最小的a与b的正线性组合,即对于方程xa+yb=c来说,若x,a,y,b都为整数,那么c的最小正根为gcd(a,b).
"""
# count5=0
# # 在python中怎样让一个递归函数返回此函数的递归次数
# # 1. 全局变量法 但必须首赋值
# def fib0(n):
#     global count5
#     count5+=1
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib0(n-1)+fib0(n-2)
# # 2. 给函数设置一个属性 但必须首赋值
# def fib01(n):
#     fib01.count01 += 1 # 添加fib的计数器属性
#
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib01(n-1) + fib01(n-2)



# a,b=0,1
# while a<5:
#     print(a)
#     a,b=b,a+b



count=0
count1=0
def hcf(x, y):
    """"该函数返回两个数的最大公约数"""

    # 获取最小值
    x1=[]
    y1=[]
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if x % i == 0:
            x1 += [i]

        if y % i == 0:
            y1 += [i]

        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    print("第一个数的公约数有: %s" % x1)
    print("第二个数的公约数有: %s" % y1)
    return hcf

# "欧几里德算法求最大公约数"
# "辗转相除法"
def gcd1(n1,n2):
    """greatest common divisor function """
    global count
    count+=1

    if (n1 % n2 == 0):
        return n2
    return gcd1(n2, n1 % n2)

# 更相减损法
"""
    《九章算术》是中国古代的数学专著，其中的“更相减损术”可以用来求两个数的最大公约数，即“可半者半之，不可半者，
    副置分母、子之数，以少减多，更相减损，求其等也。以等数约之。”

    翻译成现代语言如下：
        第一步：任意给定两个正整数；判断它们是否都是偶数。若是，则用2约简；若不是则执行第二步。
        第二步：以较大的数减较小的数，接着把所得的差与较小的数比较，并以大数减小数。继续这个操作，直到所得的减数和差相等为止。
        则第一步中约掉的若干个2与第二步中等数的乘积就是所求的最大公约数。
        其中所说的“等数”，就是最大公约数。求“等数”的办法是“更相减损”法。所以更相减损法也叫等值算法。
"""

def gcd21(n1,n2):
    global count1
    count1+=1
    if n1%2 == 0 and n2%2==0:
        return gcd21(n1/2,n2/2)
    else:
        return n1,n2
def gcd2(x1,x2):
    if x1>x2:
        if (x1 - x2) == 0:
            return x2
        else:
            return gcd2(x2,x1-x2)
    else:
        if x2-x1 == 0 :
            return x1
        else:
            return gcd2(x1,x2-x1)


def test():
    number1=int(input("请输入第一个数:"))
    number2=int(input("请输入第二个数:"))

    print("\n普通算法求最大公约数: %d" % hcf(number1,number2))
    print("\n阿几里德算法求最大公约数: %d" % gcd1(number1,number2))
    a1,b1=gcd21(number1,number2)
    gcd=gcd2(a1,b1)
    print("\n更相减损算法求最大公约数:" ,int(gcd2(a1,b1) * (2**(count1-1))))
print(dir(__name__))
if __name__=="__mail__":
    test()
