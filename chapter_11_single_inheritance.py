class Employee:
    company="Google"
    def showDetails(self):
        print("This is an Employee")
class programmer(Employee):
    language="python"
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