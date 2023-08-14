def greet(name):
    print(f"Good morning,{name}")
# a=greet("Shahid")
# print(__name__)
if __name__=="__main__":
    n=input("Enter a name:\n")
    greet(n)
    # Agar me is file se isko callkaro to __name__ ka value main ke barabar hoga agar bahar se call karu to alag hoga. 