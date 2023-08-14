class Programmer:
    company="Microsoft"
    def __init__(self,name,product,salary):
        self.name=name
        self.product=product
        self.salary=salary
    def getInfo(self):
        print (f"The name of the {self.company} programer is {self.name} and product is {self.product} and his selary is {self.salary}")
Afsar=Programmer("Afsar","skype",500)
harry=Programmer("Harry","Edge",300)
Afzal=Programmer("AFZAL","Github","1000") # "1000" is also working !!!!
Afzal.getInfo()
Afsar.getInfo()
harry.getInfo()


