def temp(cel):
    return ((cel*(9/5))+32)
c=int (input("Enter the temperature in celcius\n"))
x=temp(c)
print ("Farhanheight to celcius is " + str(x))