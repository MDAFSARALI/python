n=3
for i in range(n):
    print("* "*(n-i))
print("Hello new line ")
def star(k):
    for i in range(k):
        print("* "*(k-i))
x=int (input("Enter the no of rows\n"))
star(x)