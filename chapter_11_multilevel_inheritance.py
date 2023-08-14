class Person:
    country="India"
    def takeBreadth(self):
        print ("I am breadthing...")
class Employee(Person):
    company="Honda"
    def getSalary(self):
        print (f"Salary is {self.Salary}")
    def takeBreadth(self):
        print ("I am Employee so I am luckyly breadthing...")
class programmer(Employee):
    company="Fiber"

    def getSalary(self):
        print ("No salary to programmers")
    def takeBreadth(self):
        print ("I am programmer so I am breadthing + +...")

p=Person()
e=Employee()
pr=programmer()
p.takeBreadth()
# print (p.company) //Since person ka company nahi hai isi liye ERROR de raha.
e.takeBreadth()
print (pr.company)
print (e.company)
print (pr.country)
# pr.takeBreadth()# since programmer inheritance the property of the Employee so I am Employee so I am luckyly breadthing... so this will be printed.
pr.takeBreadth()
''' Agar class ke pas unka apna def hai to woh usko follow karenge warna phir apna sabse nearest parent ke property ko follow karenge jisko woh log inherit kiye hai. 
'''