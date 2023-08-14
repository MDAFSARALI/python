import array
size_of_array=int (input("Please enter the size: "))
array=[]
for i in range (1,size_of_array+1):
    val=int(input ("Please enter the value : "))
    array.append(val)

print ("The original array is : "+str(array))
no=int (input("Please enter the no  :"))
index=int (input("Please enter the index: "))
array.insert(index,no)
print (f"The array after appending the {no} at index {index} is : "+str(array))