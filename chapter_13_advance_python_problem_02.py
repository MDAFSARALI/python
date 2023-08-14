name=input("Please Enter your name: ")
marks=input("Please Enter your marks: ")
phone=input("Please Enter your phone number: ")
# templet="The name of the student is {},his marks are {} and phone number is {}".format(name,marks,phone)
templet="The name of the student is {},his marks are {} and phone number is {}"
output=templet.format(name,marks,phone)
print (output)