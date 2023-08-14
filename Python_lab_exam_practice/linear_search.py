def linear_search(list,key):
    for item in range (1,len(list)):
        if (list[item]==key):
            return(item+1)
        return -1
    
a=[1,23,25,90,55]
print(linear_search(a,23))