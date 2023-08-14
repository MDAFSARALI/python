# class Employee:
#     company="Camel"
#     salary=100
#     location="Delhi"
#     def changeSalary(self,sal):# It creates an instance attribute.
#         self.salary=sal


# e=Employee()
# print (e.salary)
# print (Employee.salary)
# e.changeSalary(20)
# print (e.salary)
# print (Employee.salary) //This is still 100 class attribute does not changed.#It only created an instance attribute.
# If we want to change the class attribute then -------METHOD 01
'''class Employee:
    company="Camel"
    salary=100
    location="Delhi"
    def changeSalary(self,sal):# It creates an instance attribute.
        self.__class__.salary=sal # Here we have changed the class attribute rather than creating a new instance attribute
    # __class__(This is called as dundered(dunder not under) method)


e=Employee()
print (e.salary)
print (Employee.salary)
e.changeSalary(20)
print (e.salary)
print (Employee.salary)''' # Here we can see that the class attribute has been changed.


# METHOD 02 ----To change the class attribute:
class Employee:
    company="Camel"
    salary=100
    location="Delhi"
    @classmethod # We have to use class decorater.
    def changeSalary(cls,sal):# By cls we can directly excess the class 
     cls.salary=sal

e=Employee()
print (e.salary)
print (Employee.salary)
e.changeSalary(20)
print (e.salary)
print (Employee.salary)