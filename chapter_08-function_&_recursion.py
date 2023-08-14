def percentage_function(marks1):
    return ((marks1[0]+marks1[1]+marks1[2]+marks1[3])/400)*100

marks1=[98,78,56,89]
percentage1=percentage_function(marks1)
print (percentage1)
marks3=[98,78,56,89]
percentage3=percentage_function(marks3)
print(percentage3)
marks2=[98,78,56,89]
percentage2=(sum(marks2)/400)*100 # Sum is the building function (pre_define).
print (percentage2)
# We can also use the function for this purpose.

    
