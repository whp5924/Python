#
# 面向对象
# 1. 面向过程编程：核心是”过程“,过程指的是解决问题的步聚。即先干什么后干什么，基于此思想的编程就好比编写一条流水线，
#    是一种机械式的思维方式
#    优缺：复杂的问题流程化，进而简单化。 缺点： 可扩展性差

# 2. 面向对象编程（OOP): 核心是对象,对象是变量和函数的结合体，编程过程就是要创造一个又一个具体对象。程序的执行就象由
#    对象直接交互完成。
#    优点：可护展性优良。缺点：编程的复杂性高于面向过程编程。

# 7. 类
# 7.1 类的定义
# 1. 类：就是一些对象的抽象。可以把类理解成某种概念。对象才是一个具体存在的实体。
# 2. 在现实生活中，先有对象，后才能类，对象是具体存在的，类只是一种抽象。
# 3. 在编程世界中，先定义类，再调用类来产生对象
# 4. 语法：
#         class 类名：
#              执行语句
#              0~多个类的变量
#              0~多个类的方法
#        类名只要是一个合法的标识符即可，但这仅仅满足的是 Python 的语法要求：如果从程序的可读性方面来看，
#    Python 的类名必须是由一个或多个有意义的单词连缀而成的，每个单词首字母大写，其他字母全部小写，
#    单词与单词之间不要使用任何分隔符。
#        Python 的类定义有点像函数定义，都是以冒号（:）作为类体的开始，以统一缩进的部分作为类体的。
#    区别只是函数定义使用 def 关键字，而类定义则使用 class 关键字
#        Python 的类定义由类头（指 class 关键字和类名部分）和统一缩进的类体构成，在类体中最主要的两个成员
#    就是类变量和方法。如果不为类定义任何类变量和方法，那么这个类就相当于一个空类，如果空类不需要其他可执行语句，
#    则可使用 pass 语句作为占位符。例如，如下类定义是允许的：
class Empty:
    pass
#     类中各成员之间的定义顺序没有任何影响，各成员之间可以相互调用
#        Python 类所包含的最重要的两个成员就是变量和方法，其中类变量属于类本身，用于定义该类本身所包含的状态数据：
#    而实例变量则属于该类的对象，用于定义对象所包含的状态数据：方法则用于定义该类的对象的行为或功能实现
#        Python 是一门动态语言，因此它的类所包含的类变量可以动态增加或删除（程序在类体中为新变量赋值就是增加类变量）
#    程序也可在任何地方为已有的类增加变量；程序可通过 del 语句删除己有类的类变量
#        Python 对象的实例变量也可以动态增加或删除（只要对新实例变量赋值就是增加实例变量），因此程序可以在任何地方
#    为己有的对象增加实例变量；程序可通过 del 语句删除已有对象的实例变量。
#        在类中定义的方法默认是实例方法，定义实例的方法与定义函数的方法基本相同，只是实例方法的第一个参数会被
#    绑定到方法的调用者（该类的实例），因此实例方法至少应该定义一个参数，该参数通常会被命名为 self。
#        注意：实例方法的第一个参数并不一定要叫 self，其实完全可以叫任意参数名，只是约定俗成地把该参数命名为 self，
#    这样具有最好的可读性
#        在实例方法中有一个特别的方法：__init__，这个方法被称为构造方法(也叫构造函数)。构造方法用于构造该类的对象，
#    Python 通过调用构造方法返回该类的对象
#        Python 中很多这种以双下划线开头、双下划线结尾的方法，都具有特殊的意义.
#
# 5. 调用类：1. 首先会产生一个空对象stu1
#            2、会自动触发类内部的__init__函数
#            3、然后将空对象stu1连同调用类时括号内的参数组成（stu1,"马冬梅",18,'female'）,将这四个参数一起传给__init__函数
# 例：
class OldboyStudent:
    school = "Oldboy"  # 用变量表示特征

    def __init__(self, name, age, sex):  # self=stu1     name= "马冬梅"   age=18     sex="female"
        self.name = name  # stu1.name = "马冬梅"
        self.age = age  # stu1.age = 18
        self.sex = sex  # stu1.sex = "female"

    def learn(self):  # 用函数表示技能
        print('is learning...', self)

def choose(self):
    print('choose course...')

stu1=OldboyStudent("马冬梅",18,'female')  # OldboyStudent.__init__(stu1,"马冬梅",18,'female')
stu2=OldboyStudent("甜蜜蜜",21,'male')    # OldboyStudent.__init__(stu2,"甜蜜蜜",21,'male')
stu3=OldboyStudent("原石开",22,'male')
print(stu1.name,stu1.age,stu1.sex)
print(stu2.name,stu2.age,stu2.sex)
print(stu3.name,stu3.age,stu3.sex)

#  调用类---》产生类的对象，该对象也可以称为类的一个实例，调用类的过程也称为类的实例化.

# 5. 命名空间


class OldboyStudent:
    school='oldboy'
    name='axaxaxaxxaaxs'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
stu1=OldboyStudent('李三胖',18,'male')   #OldboyStudent.__init__(stu1,'李三胖',18,'male')
print(stu1.name)                         #stu1对象的名称空间和类的名称空间都有name时优先自己的  #李三胖
print(stu1.school)                       #stu1对象的名称空间没有school时，到类的名称空间查找  oldboy
                                         #类的名称空间没有时报错
# 对象属性的查找顺序 : 先找对象自己的名称空间----》类的名称空间

# 6. 绑定方法
#   1.类内部定义的变量是给所有对象共享，所有对象指向的都是同一个内存地址
class OldboyStudent:
    def learn(self):
        print('%s is learning' %self.name)

print(id(stu1.school))          #   32094528
print(id(stu2.school))          #   32094176
#print(id(OldboyStudent.school)) #   32094528
#   2.类内部定义的函数，类可以使用，但类来用的时候就是一个普通函数，普通函数有几个参就传几个参数

print(OldboyStudent.learn)
OldboyStudent.learn(stu1)

#   3.类内部定义的函数，其实是给对象使用的，而且是绑定给对象用，绑定给不同的对象就是不同的绑定方法,
#   内存地址都不一样，但其实指向同一个功能
print(stu1.age)
print(stu2.age)

# 7. 创建对象计数器
class Foo:
    n=0
    def __init__(self):
        Foo.n+=1                # 不要写成 self.n+=1
obj1=Foo()
obj2=Foo()
obj3=Foo()
print(obj1.__dict__)        # {}
print(obj2.__dict__)        # {}
print(obj3.__dict__)        # {}

print(obj1.n)               # 3
print(obj2.n)               # 3
print(obj3.n)               # 3