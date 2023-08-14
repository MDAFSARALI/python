class Train:
    @staticmethod
    def greet():
        print ("*********         Hello Welcome to Indian Railway<---->Enjoy the jurnoy!!!         ********")
    def __init__(self,name,fare,seat):
        self.name=name
        self.seat=seat
        self.fare=fare
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats avialble in the train are {self.seat}")
        # print(f"The fare of the train is Rs {self.fare}")
    def fairInfo(self):
        print(f"The fare of the train is {self.fare}")
    def bookTicket(self):
        if (self.seat>0):
            print (f"Your ticket has been booked! and your seat number is {self.seat}")
            self.seat=self.seat-1
        else:
            print ("Sorry ! This train is full.Kindly try in tatkal")
    def cancel(self,ticNo):
        self.seat=self.seat+1
        self.ticNo=ticNo
        print (f"The seat of ticket number available is {self.ticNo}")
intercity=Train("Intercity Express:14015",90,300)
intercity.greet()
intercity.getStatus()
intercity.fairInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancel(300)
intercity.getStatus()


# Either use line 13 and 14 (simultaneously or use line 12)
'''If we write:
intercity=Train("Intercity Express:14015",90,3)
intercity.greet()
intercity.getStatus()
intercity.fairInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
then output for 5 seat booking is :
 then the 3 seat first full hoga uske bad 2 ke liye sorry seat nahi hai aisa bolega
'''