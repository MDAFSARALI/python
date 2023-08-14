class Employee:
    company="Bharat Gas"
    salary=5600
    salaryBonus=300
    # totalSalary=6100 #// Changing it to the function so that we can chnge the bonus in future.
        # This is the getter method:
    @property
    def totalSalary(self):
         return self.salary+self.salaryBonus
    '''totalSalary=salary+salaryBonus------->Isko isliye use nahi kar rahe q ki agr total salary hm denge to selary le lega magr bonus khud se jo value mene diya usme se salary ko ghata kar use lena hai thats why we are not using this '''
    @totalSalary.setter
    def totalSalary (self,val):
        self.salaryBonus=val-self.salary

e=Employee()
print (e.totalSalary) # totalSalary ke bad open closing paranthesis bracket lagane ki jaroorat nahai hai q ki woh total salary generate kar ke dega.
e.totalSalary=5800
print(e.salary) # jab hm ne 5800 diya to 5600 slary
print(e.salaryBonus) # and 200 bonus ke tor pe program ne use liya.