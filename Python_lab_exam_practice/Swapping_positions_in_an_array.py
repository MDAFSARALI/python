import array
no_of_array=int (input("Please enter the no of variables in array: "))
array=[]
for i in range(1,no_of_array+1):
    value=int (input("Please enter the values of array: "))
    array.append(value)
print ("The original array is : "+str(array))
pos1=int (input("Please enter the position 1st starting from zero : "))
pos2=int (input("Please enter the position 2st: "))
array[pos1],array[pos2]=array[pos2],array[pos1]
print ("The array after swapping is : "+str(array))
