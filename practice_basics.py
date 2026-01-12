class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
class Dev(Employee):
    pass

dev_1 = Dev("Jeman","Doe",50000)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

class Dev2(Employee):
    raise_amt = 1.05

dev_2 = Dev2("Jack","Jill",50000)
print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('--->',emp.fullname())