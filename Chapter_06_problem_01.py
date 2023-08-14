a=int (input("Enter the first number\n"))
b=int (input("Enter the second number\n"))
c=int (input("Enter the Third number\n"))
d=int (input("Enter the Forth number\n"))
if (a>d):
    f1=a
else:
    f1=d
if (b>c):
    f2=b
else:
    f2=c
if (f1>f2):
    print (str(f1) + "is greatest")
else:
    print(str(f2) + "is greatest")