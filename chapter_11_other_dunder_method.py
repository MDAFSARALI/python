class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print ("Let's add") 
        return self.num+num2.num 

    def __mul__(self,num2):
        print ("Let's Multiply:")
        return self.num*num2.num

    def __str__(self):
        print ("Let's see the number")
        return f"Decimal number :{self.num}"
        
    def __len__(self):
        print ("The length of the number is:")
        return 1
n=Number(9)
print (n)
print (len(n))