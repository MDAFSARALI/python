myDictionary={
    "fast":"In a Quick manner",
    "afsar":"A Beginners coder",
    "marks":[1,5,12],
    "anotherdict":{'Afsar':'player'},
     1:2
}                          # DICTIONARY METHODS #
#Method 1st for printing the keys of myDictionary in the list form.
print (myDictionary.keys())
# Method 2nd for printing the type of mydicttionary
print(type(myDictionary.keys()))
#Method 3rd for converting dict_key into list.
print(list(myDictionary.keys()))
#Method 4th for printing the value of mydict.
print (list(myDictionary.values()))
print ((myDictionary.values()))
#Method 5th for printing  the (key,value) for all contents .
print ((myDictionary.items())) #......>it returns tuple 
#Method 6th for update or add more 
print(myDictionary)
updateDict={
    "Faishal":"A government employee",
    "Afzal":"A young boy",
    "Kausar":"Head of the family",
    "marks":[12,25,39] # Updated the already present values.
}
myDictionary.update(updateDict)
print (myDictionary)
print (myDictionary["afsar"])
# use of get // Please compare the two lines line=29 and line =31
print (myDictionary.get("afsar")) 
# THE DIFFERENCE BETWEEN LINE 29 and 31 can be seen by this 
 #print (myDictionary["afsar2"])    # THIS LINE THROWS THE ERROR afsar=afsar2
print (myDictionary.get("afsar2")) # THIS LINE  DOES NOT THROWS THE ERROR afsar=afsar2 it will return None
