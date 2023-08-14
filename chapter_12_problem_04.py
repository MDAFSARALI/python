a=int (input("Enter the value of a: "))
b=int (input("Enter the value of b: "))
try:
    c=a/b
    print (c)
except ZeroDivisionError as e:
        print (f"Please check the value of 'b' ! Make sure you does not entered b=0 !!!--------->{e} is not possible")