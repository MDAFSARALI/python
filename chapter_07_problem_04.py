a=int(input("Enter the number which you want to check\n"))

for i in range (2,a):
    if ((a%i)==0):
        print ("Enterd number is not a prime number")
        i=i+1
        break
else:
    print ("Enterd number is a prime number")


# This problem by codewithharry:

num=int (input("Enter the number\n"))
prime=True
for i in range (2,num):
    if (num%i==0):
        prime =False
        break
if prime:
    print ("Entered number is prime")
else :
    print("Entered number is not a prime")
