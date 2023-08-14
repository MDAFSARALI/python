'''a=[3,6,7,8,9,2,4,23,75,23,123,67]
b=[]
c=[]
for item in a :
    if item%2==0:
        b.append(item) # Here we are storing the even number item from the list in list b...
    if item%2!=0:#odd number 
        c.append(item)
print (b)
print(c)'''
# Another method (SHORT-CUT):
'''a=[3,6,7,8,9,2,4,23,75,23,123,67]
b=[i for i in a if i%2==0]
print(b)'''
# For set :
t=[1,4,2,4,1,2,3]
s={i for i in t } # This is set so for unique value:
print(s)