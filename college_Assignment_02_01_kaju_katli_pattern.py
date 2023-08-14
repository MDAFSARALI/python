h=eval(input("Enter the hight of the diamond pattern\n"))
for x in range (h):
    print (" "*(h-x),"*"*(2*x+1))
for x in range (h-2,-1,-1):
        print (" "*(h-x),"*"*(2*x+1))