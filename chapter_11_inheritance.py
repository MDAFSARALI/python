# Inheritance also works on DRY principle(do not repeat yourself).
# Inheritance is a way of creating a newclass from anexisting class.
# By use of inheritance we can over-Write the previous details.this can be understand by line number 20.
'''This is a single level inheritance:'''
class Employee:
    company="Google"
    def showDetails(self):
        print("This is an Employee")
class programmer(Employee):
    language="python"
    #company="YouTube"// Here the updation of the comapny occures.
    def getLanguage(self):
        print (f"The Employee knows the language of {self.language}")
    def showDetails(self):
        print("This is a programmer")
e=Employee()
e.showDetails()
p=programmer()
p.showDetails()
# print (p.company)
print(p.company)
# p.getLanguage()