'''
t=(1,5,2,8)
print (t)
print(t[0])
print(t[1])
print(t[2])
print(t[3])
#  What is the difference between tuple and list .
# ANS::::In the tuple we can not update the value but int the list we can update it.....
 #t[0]=98       ...............>Here we can clearly see we can not update.
print (t)
a=("Afsar","Shakib")
    #a[0]="Afzal".........>Here we can clearly see we can not update.
print (a)
t1=()
print(t1)
t2=(1)  #This is the wrong way to write the single elemnt in the tuple.
#Right methodto write the single element in the tuple is (1,)
    #t2[0]=45.............>ERROR bcz tuplates can not update.
print (t2)'''

'''a.count(1):a.count[1] will return number of times 1 occures in a 
a.index(x):a.inex will return the index of first occurence of 1 in a.'''

#####Use of count keyword.
a=(1,1,1,1,1,1,2,3,4,5,6)
print (a.count(1))
b=a.count(1)
print (b)#This print the number of count of the number which is entered in the (1)

c=a.index(3) #This index keyword indicates at first time where the 5(five) has arrived.
print (a.index(3)) 
print (c)


