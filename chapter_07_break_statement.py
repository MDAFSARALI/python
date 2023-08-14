for i in range(10):
    print (i)
    if i==5:
        break
else:
    print ("This is inside else of for")
     # This will be executed on the succesful termination of the loop.otherwise it will not be executed.

     #Use of continue statement ------>
print ("Lets start the continue statements\n")
for i in range(10):
    print (i)
    if i==5:
        continue
else:
    print ("This is inside else of for")


    #######CONTINUE UNSTANDING1!
for i in range(10):
    if i==5:
        continue #This will not be executed for 5 it will continue for 6
    print (i)
    #printing of odd number 
for i in range(10):
    if i%2==0:#printing of odd numbers!
        continue 
    print (i)
    #printing of even numbers
for i in range(10):
    if i%2!=0:#printing of odd numbers!
        continue 
    print (i)


    ''' When we want to say do nothing then we generally use "pass" PASS is a null statement in python'''
i=4
if i>0:
    pass
while i>6:
    pass
print ("Hello Afsar")