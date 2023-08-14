# Set is the collection of none repetative elements.

a={1,2,3,5,25}
print (type(a))
print(a)
#If repetation occure in sets the repeated numbers get cancelled out,
b={1,2,3,4,5,5,5,5}
print (b)
b.add(25)
print (b)
c={}   #Carly braces does not forms empty set it forms empty  dictionary.
print (type(c))
#How to create an empty set? 
# WE can create an empty set by given below syntax.
d=set()
print (type(d))
#For adding items in the empty set then we must have to use (name.add) 
d.add(4)
d.add(4) # This line does not add the 4 two times after printing it will occure only once because set does not contain the same number more than once.
d.add(25)
print (d)
# Adding the list to the empty set
# d.add([12,25,35,65])              // This does not add into d a list can  not be add into the set.
# print (d) 
#  BUT WE CAN DEFINATELY ADD IN FOrmS OF TUPLES
d.add((12,25,35,65)) # Touples sayd set ke end me add ota hota hai.
# We also can not add dictionary into the sets.        
 # b.add({15,1,7,9}) 
d.add(2.5)
print (d) 
print (len(d)) # This method shows how many items are present in the set with the help of len
d.remove(2.5) #This remove the 2.5 from the sets if the number does not present in the set the it will throe a error.
 #d.remove(98) ,,,,,,,,,,,,ERROR
print (d)
print(d.pop())
print (d)
#set.clear ....>It empties the set
#set.union({12,39}).....>Returns a new set with all item from the both sets
#set.intersection({8,11})
# a.clear() // This line set a ko empty kar diya 
# print (a) 
ne=a.union({13.5,35.7})
print(ne)  #// This line prints the union of the a with new elements
xe=a.intersection({2,3})
print (a)
print (xe)