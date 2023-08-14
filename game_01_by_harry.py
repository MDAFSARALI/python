#  Snack Water or Gun Rock paper scissors //Rock paper scissors can also be fored bu using the same code.
import random
# If two values are equal then ,Declare a tie!
def game(comp,you):
    if comp==you:
        return None
#Check for all possibilities when computer choose 's'
    elif comp=='s':
        if you=='w':
            return False 
        elif you=='g':
            return True
#Check for all possibilities when computer choose 'w'
    elif comp=='w':
        if you=='g':
            return False 
        elif you=='s':
            return True
#Check for all possibilities when computer choose 'g'
    elif comp=='g':
        if you=='w':
            return False
        elif you=='s':
            return True
print ("Computer turns:Snake(s), water(w) or Gun(g)\n")
randomNo=random.randint(1,3)
if randomNo==1:
    comp='s'
elif randomNo==2:
    comp='w'
elif randomNo==3:
    comp='g'
you=input("your turn:Snake(s) Water(w) or gun(g)?\n")
a=game(comp,you)
print(f"computer choose:{comp}")
print(f"You choose:{you}")
if a==None:
    print("The game is tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")