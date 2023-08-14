height=int (input("Please enter the height of diamound: "))
for i in range (height):
    print (" "*(height-i),"*"*(2*i+1))
for i in range ((height-2),-1,-1):
    print (" "*(height-i),"*"*(2*i+1))