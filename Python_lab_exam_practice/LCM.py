def lcm_calculation(x,y):
        if (x>y):
            greater=x 
        greater=y
        while(True):
            if ((greater%x==0)and (greater%y==0)):
                 lcm=greater
                 break
            greater+=1
        return lcm
input1=int (input("Enter 1st: "))
input2=int (input("Enter 2nd: "))
print(f"The lcm of {input1} and {input2} is "+str(lcm_calculation(input1,input2)))

