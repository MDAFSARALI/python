a=int (input("Enter the number of rows\n"))
for i in range (a):
    print(" "*(a-i-1),end="") # Here the end="" is used for new line 
    print ("*"*(2*i+1),end="")
    print (" ")
    # print (" "*(a-i-1))
        