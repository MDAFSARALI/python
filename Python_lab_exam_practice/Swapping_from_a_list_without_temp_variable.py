list1=[1,2,3,4,5]
pos1=int (input("Enter the position no 1: "))
pos2=int (input("Enter the position no 2: "))
list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
print ("The list after swapping : "+str(list1))