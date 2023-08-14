'''Exception Handling in python:'''
# try.py
while(True):
    print ("Press q for quit the game----")
    a=input("Enter a number:")
    if a=='q':
        break
    try:
        print ("Trying to run......")
        a=int (a)
        if a>6:
            print ("You have entered a number greater than 6")
    except Exception as e:
         print (f"Your input resulted in error:{e}")
        # print(e)
# We we does not enter the number if we enter the another elements then it will through the error of (invalid literal for int () with base 10) 
# so for menimize such type of error we uses Exception Handling......
print("Thanks for playing the game !!!")
