def selectionsort(array,size):
    for index in range (size):
        min_index=index
        for j in range ((index+1),size):
            if array[j]<array[min_index]:
                min_index=j
                (array[index],array[min_index])=(array[min_index],array[index])
array=[-2,45,0,11,-9,88,-97,-202,747]
size=len(array)
selectionsort(array,size)
print(array)
