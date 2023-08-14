# n=4
# product=1
# for i in range (n):
#     product=product*(i+1)
# print (product)
print ("FACTORIAL USING FOR LOOP\n")
n=5
def factorial_iter(n):
    product=1
    for i in range (n):
        product=product*(i+1)
        
    return product


print(factorial_iter(5))

print ("FACTORIAL USING RECURSION\n")
# n!=1*2*3*---*n
# n!=1*2*3*---(n-1)*n
# n!=(n-1)!*n
def fact_recursive(k):
    if k==1 or k==0:
        return 1
    return k*fact_recursive(k-1)
# print(fact_recursive(5))
f=fact_recursive(6)
print (f)