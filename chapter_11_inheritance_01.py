# Types of inheritance:
# 1)Single level inheritance.(1 base class,1 inherited class)
# 2)Multiple level inheritance.(2(or more)base class(parent class),1 inherited class)
# 3)Multilevel inheritance.(1 base class,multilevel inherited class)
class Person:
    country="India"

    def __init__(self):
        print ("Initializing person.....\n")     

    def takeBreadth(self):
        print ("I am breadthing...")
class Employee(Person):
    company="Honda"
    def __init__(self):
        super().__init__()
        print ("Initializing Employee.....\n")

    def getSalary(self):
        print (f"Salary is {self.Salary}")

    def takeBreadth(self):
        super().takeBreadth()
        print ("I am Employee so I am luckyly breadthing...")

class programmer(Employee):
    company="Fiber"
    def __init__(self):
        super().__init__() # IF WE COMMENT OUT THIS THEN ONLY INITIALIZING PROGRAMMER WILL BE EXECUTAD.bcz we did not call for super class/
        print ("Initializing Programmer.....\n")

    def takeBreadth(self):
        super().takeBreadth()# It also prints the takeBreadth of the Employee because we have used super.takeBreadth because it inherutance the Employee class so it will print it .
        print ("I am programmer so I am breadthing + +...")

# p=Person()
# p.takeBreadth()

# e=Employee()
# e.takeBreadth()

pr=programmer()
# pr.takeBreadth()

