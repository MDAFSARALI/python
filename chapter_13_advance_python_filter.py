# Filter syntax error in the notes:correct one::::list (filter(function,list))
def greeter_than_5(num):
    if num>5:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8,9,89,98]
print (list(filter(greeter_than_5,l))) # This line prints the content of list which is greater than 5
# [6, 7, 8, 9, 89, 98]--------->>> OUTPUT
g10=lambda num:num>10 # we can also use the lambda function.
print (list(filter(g10,l)))