#
# Fig 09.09 fig09_09.py

# 基类：雇员
# 子类：Boss 老板 每周领固定的薪水
# 子类: Commission Worker 代理人 每周领取少量的固定薪水，另外销售提成
# 子类: PieceWorker  计件工 按生产的件数领取薪水
# 子类: HourlyWorker  小时工 按每小时计酬，每周超过40小时，每小时按1.5美元计

class Employee:
    def __init__(self,first,last):
        if self.__class__== Employee:
            raise NotImplementedError("Cannot create object of class Employee")
        else:
            self.first=first
            self.last=last
    def __str__(self):
        return "  %8s %6s" % (self.first,self.last)

    def _checkPositive(self,value):
        if value<0:
            raise ValueError("Attribute value (%s) must be positive " % value)
        else:
            return value
    def earnings(self):
        raise NotImplementedError("Cannot call abstract meth")
class Boss(Employee):
    def __init__(self,first,last,salary):
        Employee.__init__(self,first,last)
        self.weeklySalary=self._checkPositive(float(salary))
    def earnings(self):
        return self.weeklySalary
    def __str__(self):
        return "%17s%12s  " % ("Boss",Employee.__str__(self))
class CommissionWorker(Employee):
    def __init__(self,first,last,salary,commission,quantity):
        Employee.__init__(self,first,last)
        self.salary=self._checkPositive(float(salary))
        self.commission=self._checkPositive(float(commission))
        self.quantity=self._checkPositive(float(quantity))

    def earnings(self):
        return self.salary + self.commission * self.quantity

    def __str__(self):
        return "%17s%12s  " % ("Commission Worker", Employee.__str__(self))

class PieceWorker(Employee):
    def __init__(self,first,last,wage,quantity):
        Employee.__init__(self,first,last)
        self.wage=self._checkPositive(wage)
        self.quantity=self._checkPositive(quantity)
    def earnings(self):
        return self.wage *self.quantity

    def __str__(self):
        return "%17s%12s  " % ("Piece Worker",Employee.__str__(self))
class HourlyWorker(Employee):
    def __init__(self,first,last,wage,hours):
        Employee.__init__(self,first,last)
        self.wage=self._checkPositive(wage)
        self.hours=self._checkPositive(hours)
    def earnings(self):
        if self.hours<=40:
            return self.wage * self.hours
        else:
            return self.wage * self.hours + (self.hours-40) * self.wage * 1.5
    def __str__(self):
        return "%17s%12s  " % ("HourlyWork",Employee.__str__(self))


#
employees=[Boss("John","Smith",800),CommissionWorker("Sue","Jones",200,3.0,150),PieceWorker("Bob","Lewis",2.5,200),
           HourlyWorker("Karen","Price",13.75,40)]

for employee in employees:
    print("%11s earnings %0.2f" % (employee,employee.earnings()))