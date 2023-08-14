# Using enemurate functio use print the 1st,3rd,5th element of the list
'''list1=["Afsar",12,25,36,12.35,"Harry"]
for index,item in enumerate(list1):
    if (index %2!=0):
        print (index,item)'''
    
# BY HARRY:
list1=["Afsar",12,25,36,12.35,"Harry",25,68.0,90]
for index,item in enumerate(list1):
        if (index==2 or index==4 or index==6):
            print (f"The {index+1}th element is {item}")
