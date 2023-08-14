letter='''Dear <|NAME|>,
Greeting from abc coding house!
I am happy to tell you about your selection ,hope you have a great day ahead!!
you are selected!
            Thanks and regards !!!
            Bill:
date:<|DATE|>'''
name=input("Enter your name please!\n")
date=input("Enter the date\n")
letter =letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print (letter)