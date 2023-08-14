
def bubble_sort(list):
    for i in range (len(list)):
        for j in range (len(list)-i-1):
            if (list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
           
list=[2,5,3,8,9]
print("After bubble sort: ")
bubble_sort(list)

print(list)
