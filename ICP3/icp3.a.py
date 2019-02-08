class Employee():
    empCount = 0 #initialization of the data member
    empSal = [];
    def __init__(self,name,family,salary,department): #default constructor
        self.empname = name
        self.empfamily = family
        self.empsalary = salary
        self.empdepartment = department
        Employee.empCount +=1  #counts the number of employees
        Employee.empSal.append(salary)  #appends salaray attribute

    def avg_salary(self):
        print('the average salary is')
        sumSal = 0;
        for sal in Employee.empSal:
            sumSal = sumSal+ int(sal);
        return sumSal/len(Employee.empSal)

class FulltimeEmployee(Employee):
    def __init__(self,name,family,salary,department):
        Employee.__init__(self,name,family,salary,department)


emp1 = FulltimeEmployee('bhargavi',' chennupati','7000','CS');
emp2 = FulltimeEmployee('ramya','sai','5000','MECH');
emp3 = FulltimeEmployee('lakshmi','kavuri','4000','CS');
print(FulltimeEmployee.empCount)  #inherits characteristics from parent class
print(FulltimeEmployee.empSal)
avgSal = FulltimeEmployee.avg_salary(Employee);
print(avgSal)