# Define a Employee class with attributes role,department & salary .this class also showDetails() method
# create an Engineers  class that inherits properties from Employee & has additional attributes name & age:

class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def showDetails(self):
        print("Role :",self.role)
        print("Department :",self.department)
        print("Salary :",self.salary)
        
class Engineers(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        super().__init__("Engineer","IT","75,000")

eng1 = Engineers("Ankit Vishwakarma",21)
eng1.showDetails()
print("Name :",eng1.name)
print("Age :",eng1.age)