number=int (input("Please enter the number: "))
sum=0
for i in range(1,number):
    if (number%i==0):
        sum+=i
if (sum==number):
    print ("yes.perfect")
else: 
    print ("No perfect")