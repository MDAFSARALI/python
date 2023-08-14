a=int (input("Enter the number whose table you want to print \n"))
i=1
while i<=10:
    print(str(a)+"X"+str(i)+"="+str(a*i))
    i=i+1


    # By using for loop
b=int (input("Enter the number whose table you want to print \n"))
for i in range (1,11):
    # print(str(b)+"X"+str(i)+"="+str(b*i))
    # Another method for printing the table is 
    print(f"{b}X{i}={b*i}")