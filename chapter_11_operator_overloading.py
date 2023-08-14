class Number:
    def __init__(self,num):
        self.num=num
    # def __add__(self,num2)://--------------------01 <<<<<<<<< Here we have overloaded the add method: >>>>>>>>>>>
    #     print ("Let's add") //--------------------01
    #     return self.num+num2.num //--------------------01
    def __mul__(self,num2):
        print ("Let's Multiply:")
        return self.num*num2.num
n1=Number(4)
n2=Number(6)
# sum=n1+n2 //------------------------------01
mul=n1*n2
# print (sum)   //--------------------------01
print(mul)