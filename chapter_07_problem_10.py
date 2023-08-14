# Q):Reverse multiplication table.
a=int (input("Enter the number whose table you want to print \n"))
for i in range (-10,0):
    print({a},'X',{-1*i},'=',(a*i)*-1)
    print (str(a)+"X"+str(-i)+"="+str(-i*a))

#     # Other method 
# b=int (input("Enter the number whose table you want to print \n"))
# for j in range (1,11):
#         print (b,'X',(11-j),'=',b*(11-j))
    
