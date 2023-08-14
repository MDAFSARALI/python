a=int (input("Enter your makrs please!"))
if (a>=90 and a<100):
    print ("your grade is excalent")
elif(a>=80 and a<90):
    print ("your grade is A")
elif(a>=70 and a<80):
    print ("your grade is B")
elif(a>=60 and a<70):
    print ("your grade is C")
elif(a>=50 and a<60):
    print ("your grade is D")
elif(a<50):
    print ("your grade is F")
                #Harry method#
marks=int (input("Enter your makrs please!"))
if marks>=90:
    grade="Ex"
elif marks>=80:
    grade="A"
elif marks>=70:
    grade="B"
elif marks>=60:
    grade="C"
elif marks>=50:
    grade="D"
elif marks<50:
    grade="F"
print ( "Your grade is" +" "+grade)