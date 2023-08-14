
def bubble_sort(list):
    for i in range (0,len(list)-1):
        for j in range (i):
            if (list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
            return list
list=[2,5,3,8,9]
print("After bubble sort: ")
print(bubble_sort(list))      
