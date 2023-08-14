def hcf_calculation(x,y):
        if (x>y):
            smaller=y
        smaller=x
        for i in range (1,smaller+1):
            if ((smaller%i==0)and (smaller%i==0)):
                 hcf=i
                 
           
        return hcf
input1=int (input("Enter 1st: "))
input2=int (input("Enter 2nd: "))
print(f"The lcm of {input1} and {input2} is "+str(hcf_calculation(input1,input2)))

