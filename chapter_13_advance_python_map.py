''' # This is the method---01:
def square(num):
    return num *num
l=[1,2,4]
l2=[]
for item in l:
    l2.append(square(item))
print(l2)'''
# Method 02:
def square(num):
    return num *num
l=[1,2,4]
print (list (map(square,l))) # Here we converted the upper operation in shortcut method // We must have to convert into the list because we need it into the list
