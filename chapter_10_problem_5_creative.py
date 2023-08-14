class Train:
    @staticmethod
    def greet():
        print ("*********           Hello Welcome to Indian Railway<---->Enjoy the jurnoy!!!         ********")
    def __init__(self,name,fare,seat):
        self.name=name
        self.seat=seat
        self.fare=fare
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats avialble in the train are {self.seat}")
        print(f"The fare of the train is Rs {self.fare}")
    def fairInfo(self):
        print(f"The fare of the train is {self.fare}")
    def bookTicket(self):
        if (self.seat<=3):
            print (f"Your ticket has been booked! and your seat number is {self.seat}")
            self.seat=self.seat+1
        else:
            print ("Sorry ! This train is full.Kindly try in tatkal")
intercity=Train("Intercity Express:14015",90,1)
intercity.greet()
intercity.getStatus()
intercity.fairInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()