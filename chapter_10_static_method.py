class Employee:
    comapny="Google"
    def getSalary(self,signature):
        print (f"Salary for this employee working in {self.comapny} is {self.salary}\n{signature}")
    @staticmethod # This is used here because we dont want to write the self in line 6.(@staticmethod is decorator)//
    def greet():
    # #  Either use line 5 and 6 (stah me) ya phir only line 8.
    # def greet(self):
        print ("Good Morning,sir")
    @staticmethod
    def time():
        print("Time is 9 am in the morning!")
harry=Employee()
harry.salary=100000
harry.getSalary("Thanks!")
harry.greet()
harry.time()