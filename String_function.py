story="once upon a time there was a youtube named as Harry who uploade python course with notes"
#string function
print (len (story)) #in this statement len is used to find the length of story.
print(story .endswith("notes")) #Yaha par story me likha hua line notes se khatam ho raha isi liye true return hua'
print(story .endswith("s"))
#agar story ka line notes se khatam hua magar kuch or agar likhe to woh false return karega 
print(story.endswith("Afsar"))
print(story .count("o"))   #count =how many times any letter has been written in the line #here capital o and small o are different
print(story .count("notes"))
print (story.capitalize())  #this keyword is used for capitalize the first letter of the sentance .
print (story.find("was"))    #It finds whwther it is present or not and if is presend then position of it
print (story.find("wax"))   #it returns -1 it means it is not present in the comment 
print (story.replace("Harry","Codewithharry")) #replaces all the harry with codewithharry