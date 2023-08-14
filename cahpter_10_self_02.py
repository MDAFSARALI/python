class Employee:
    comapny="Google"
    def getSalary(self):
        print (f"Salary for this employee working in {self.comapny} is {self.salary}")
    
harry=Employee()
harry.salary=500000
harry.getSalary()