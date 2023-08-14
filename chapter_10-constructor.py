class Employee:
    comapny="Google"
    def __init__(self,name,salary,subunit):# It is called as a Constructor because it initializes the object.
        self.name= name
        self.salary=salary
        self.subunit=subunit
        print ("Employee is created")
    def getDetails(self):
        print (f"The salary of the salary is {self.salary}")
        print (f"The subunit of the subunit is {self.subunit}")
        print (f"The name of the Employee is {self.name}")
    def getSalary(self,signature):
        print (f"Salary for this employee working in {self.comapny} is {self.salary}\n{signature}")
    @staticmethod 
    def greet():
        print ("Good Morning,sir")
    @staticmethod
    def time():
        print("Time is 9 am in the morning!")


harry=Employee("Harry",100,"YouTube")
# harry=Employee() # If we do not passes three arguments then this (harry=Employee("Harry",100,"YouTube")) error is throwing
harry.getDetails()
