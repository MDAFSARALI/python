lower=int (input("Enter lower limit :"))
upper=int (input("Enter upper limit :"))
for num in range (lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while(temp>0):
        digit=temp%10
        sum+=digit**order
        temp//=10
    if(sum==num):
        print(num)
