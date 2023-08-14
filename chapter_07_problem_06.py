a=int(input("Enter the number whose factorial do you need\n")) 
fact=1
for i in range (1,a+1):
    fact=fact*i
print (fact)
print (f"The factorial of the number {a} enterd by user is {fact}")