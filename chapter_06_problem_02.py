English=float (input("Enter the marks of English:  "))
Math=float(input("Enter the marks of Math:   "))
Hindi=float (input("Enter the marks of Hindi:   "))
total=(English+Math+Hindi)/3
if (English>=33 and Math>=33.3 and Hindi>=33 and total>=40 ):
       print("You have passed ")
else:
    print("You have failed")





#This is the method by harry:
English=int (input("Enter the marks of English:  "))
Math=int(input("Enter the marks of Math:   "))
Hindi=int (input("Enter the marks of Hindi:   "))
if (English<33 or Math<33 or Hindi<33):
    print ("You have failed due to less than 33% IN one(more) of the subject")
elif(English+Math+Hindi)/3 <40:
    print("You failed due to total percentage less than 40")
else:
    print("Congratulation ! You have passed!")