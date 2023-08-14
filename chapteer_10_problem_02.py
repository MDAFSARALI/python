'''class Calculator:
    def __init__(self,number):
        self.number=number
        self.square=number*number
        self.cube=number*number*number
        self.square_root=number**(0.5)
    def getInfo(self):
        print (f"The square of the {self.number} is {self.square}\ncube is {self.cube} and square root is {self.square_root}")
b=eval(input("Enter the number which you want to calculate the square and cube and square root\n"))
num2=Calculator(b)
num1=Calculator(25)
num1.getInfo()
num2.getInfo()'''


#By Harry:
class Calculator:
    def __init__(self,num) :
        self.number=num
    def square(self):
            print (f"The value of {self.number} square is {self.number**2}")
    def cube(self):
        print (f"The value of {self.number} cube is {self.number**3}")
    def squareRoot(self):
        print (f"The value of {self.number} squareRoot is {self.number**0.5}")
a=Calculator(3)
a.square()
a.cube()
a.squareRoot()