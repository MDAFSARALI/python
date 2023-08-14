'''First------->01
try:
    a=int (input("Enter a number:"))
    c=1/a
    print (c)
except Exception as e:
    print ("Exception occured!!")
    print (e)
print ("Thanks for using this code!!")'''

# Second exception:----->02
try:
    a=int (input("Enter a number:"))
    c=1/a
    print (c)
except ValueError as e:
    print ("Pleaase enter a valid value !!!")
    # print (e)

except ZeroDivisionError as e:
    print ("Make sure you are not dividing by 0 !!")
    # print (e)
    
except TypeError as e :
    print ("Another type of error is occured!!")
print ("Thanks for using this code!!")
