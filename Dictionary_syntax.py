# Q):Formation of nested dictionary in python? 
# It is unordered in nature.
# It is mutable(means :it can be change )
# It is index.
# It Can not contain duplicate key.
#Multiple keys of same name can not be existed.
myDictionary={
    "Fast":"In a Quick manner",
    "Afsar":"A Beginners coder",
    "marks":[1,5,12],
    "anotherdict":{'Afsar':'player'},
    "Afsar":"A Null Value"  # Here the mutability occured bcz the keY "Afsar" gets updated . 
   
}
print (myDictionary['Fast'])
print (myDictionary['Afsar'])
print (myDictionary['marks'])
print(myDictionary['anotherdict']['Afsar'])