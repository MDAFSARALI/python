'''a=54 # This is the global value of a.
def func1():
    print (a)
func1'''
'''a=54 # Global variable:
def func1():
    a=8 #This is a local variable the value of a does not mean to change 54 to 8
    print (a)
func1()
print(a)'''
a=54
def func1():
    global a # It will change the global variable of a
    # Here the global keyword is used to globalise now assignmnet does not take place so printing of a will produce 54 
    print(f"print statement 01--{a}") # this line will produce :54
    a=8 # Now this will become global variable 
    print(f"print statement 02--{a}") # This line wil produce :8

func1()
print(f"print statement 03--{a}") # this line will produce :8
