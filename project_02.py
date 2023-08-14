import random
randNumber=random.randint(1,100)
print (randNumber)
count=0
userNumber=None
while(userNumber!=randNumber):
    userNumber=int(input("Enter a number under 100\n"))
    count=count+1
    if randNumber>userNumber:
        print ("Higher Number please!!")
    elif randNumber<userNumber:
        print ("Lower number please!")
    else:
        print("Greet Yoy have guessed it right !!!")

print (f"Total number of time you need for guessing the number is {count}")
with open ("hiscore.txt","r") as f:
    hiscore=int(f.read())
    if (count<hiscore):
        print ("You have just broken the high score! \n ****_____CONGRATULATION_____****!!")
        with open ("hiscore.txt","w") as f:
            f.write(str (count))
   
'''BY HARRY:
import random
randNumber=random.randint(1,100)
print (randNumber)
userGuess=None
guesses=0
while(userGuess!=randNumber):
    userNumber=int(input("Enter a number under 100\n"))
    guesses+=1
    if (userGuess==randNumber):
        print ("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong ! Enter a smaller number")
        else:
            print("You guessed it wrong ! Enter a Larger number") 
print (f"You guessed the number in {guesses} guesses")
    with open ("hiscore.txt","r") as f:
    hiscore=int(f.read())
    if (guesses<hiscore):
        print ("You have just broken the high score! \n ****_____CONGRATULATION_____****!!")
        with open ("hiscore.txt","w") as f:
            f.write(str (guesses))
   '''