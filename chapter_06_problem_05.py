a=["afsar","afzal","faishal","rehan","shakib"]
b=input("Enter the name which you want to search\n")
if (b in a): #In list functio when we have tfind the wether any string/name is present or not we can not use "find" keyword because list does not accept it 
    #For overcome this problem we generally use "in"keyword .....>braces in if statement is not compulsory.
    print("Entered name is present in the list\n")
else:
    print("Entered name is not present in the list\n")
    