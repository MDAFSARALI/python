
              ##### Program by harry!!####
text=input("Enter the text\n")
if ("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe this" in text):
    spam=True
elif("click this" in text):
    spam=True
elif("watch this" in text):
    spam=True
elif("discount" in text):
    spam=True
else:
    spam=False
    
if (spam):
    print ("this is a spam ")
else:
    print("This is not a spam")
    
