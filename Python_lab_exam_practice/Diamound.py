height=int (input("Please enter the height of the diamound: "))
for i in range (height):
    print (" "*(height-i),"*"*(2*i+1))
for j in range (height-2,-1,-1):
    print (" "*(height-j),"*"*(2*j+1))