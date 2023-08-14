no_of_dollar=int (input("PLease enter the no of dollar sign: "))
for i in range(no_of_dollar):
    for j in range (no_of_dollar):
        if i==0 or i==no_of_dollar-1 or j==0 or j==no_of_dollar-1:
            print ("$",end=" ")
        else: 
            print (" ",end=" ")
    print("\n")