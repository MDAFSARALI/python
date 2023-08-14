class RailwayForm:
    formType="RailwayForm"
    def printData(self):
        print (f"Name is {self.name}")
        print (f"Train name is {self.train}")
afsarapplication=RailwayForm()
afsarapplication.name="Afsar"
afsarapplication.train="Rajdhani Express"
afsarapplication.printData()