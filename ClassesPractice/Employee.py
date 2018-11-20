class Employee:
    empcount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def displayCount():
        print("Employee Count : ",Employee.empcount)

    def displayEmployee(self):
        print("Name : ",self.name," Salary : ",self.salary)

emp1 = Employee("Shubham",60000)

emp2 = Employee("Raksesh",50000)

emp3 = Employee("Radha",90000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

Employee.displayCount()