import array
size=int (input("Please eneter the size of the array: "))
array=[]
print ("Please enter the array value : ")
for i in range (1,size+1):
    val=int (input("Please enter the value: "))
    array.append(val)
print ("The original array is : "+str(array))
postion=int (input("Please eneter the position of the array : "))
array.pop(postion)
print ("After removing the element the array is :"+str(array))

