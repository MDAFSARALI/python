import random
def game(comp,you):
    if comp=='s':
        if you=='w':
            print ("You Lose!")
        elif you=='s':
            print ("Game Draw!")
        else:
            print("You won!")
    if comp=='w':
        if you=='w':
            print ("Game Draw!")
        elif you=='s':
            print ("You won!")
        else:
            print("You Lose!")

    if comp=='g':
        if you=='w':
            print ("You Won!")
        elif you=='g':
            print ("Game Draw!")
        else:
            print("You Lose!")
    print (f"Computer choose: {comp}")
    print (f"You choose: {you}")
print ("Computer turns:Snake(s), water(w) or Gun(g)\n")
randomNo=random.randint(1,3)
if randomNo==1:
    comp='s'
elif randomNo==2:
    comp='w'
elif randomNo==3:
    comp='g'
you=input("your turn:Snake(s) Water(w) or gun(g)?\n")
game(comp,you)