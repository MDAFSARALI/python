def bubble_sort(list):
    for i in range (len(list)):
        for j in range (0,len(list)-i-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
            return list
list=[5,23,10,15,13]
print(bubble_sort(list))
