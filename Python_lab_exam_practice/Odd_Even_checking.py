def odd_even_checking(n):
    if (n%2==0):
        print (f"The entered number {n} is even.")
    else:
        print(f"The entered number {n} is odd.")
number=eval (input("Please enter a number : "))
odd_even_checking(number)