def perfect_check(n):
    sum=0
    for i in range (1,n):
        if (n%i==0):
            sum=sum+i
    return sum

number=int (input("Please enter a number: "))
if(number==perfect_check(number)):
        print ("Yes entered number is perfect :")
else:
        print ("No entered number is not perfect :")
