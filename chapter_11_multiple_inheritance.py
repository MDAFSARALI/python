class Employee:
    company="Visa"
    eCode=120
class Freelancer:
    company="Fiber"
    level=0
    def upGradeLevel(self):
        self.level=self.level+1
class programmer(Employee, Freelancer): # Priority to the methods of employee rather than Freelancer
    name="Rohit"
#  Creating the object of the programmer.
p=programmer()
p.upGradeLevel()
print (p.level)
# p.upGradeLevel()
# print (p.level)
# p.upGradeLevel()
# print (p.level)
# p.upGradeLevel()
# print (p.level)
print (p.company) # p.company print karne par visa print hua q ki programmer ke andar pehle Employees ka details dala gaya hai isi liye agar usme 
# pehle freelancer,Employee dalde to p.company print karne par fiber print hoga//



