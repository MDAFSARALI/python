class Calculator:
    @staticmethod
    def greet():
        print ("*********Hello Welcome to the best calculator of the World !!!********")
    def __init__(self,num) :
        self.number=num
    def square(self):
            print (f"The value of {self.number} square is {self.number**2}")
    def cube(self):
        print (f"The value of {self.number} cube is {self.number**3}")
    def squareRoot(self):
        print (f"The value of {self.number} squareRoot is {self.number**0.5}")
a=Calculator(3)
a.greet()
a.square()
a.cube()
a.squareRoot()
