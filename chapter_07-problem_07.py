# Write a python program to remove a given word from a string and strip it at the same time 
# strip is a function generally use for remove the spaces.
# this ="      Harry is a good teacher        "
# print(this) # this will print (      Harry is a good teacher        )
# print(this.strip()) # this wiil print (Harry is a good teacher)
def remove_and_split(string,word):
    newstr=string.replace(word,"")
    af_split=string.strip()
    new=newstr.strip()
    again=newstr.split()
    x=string.split()
    print(newstr)
    print(af_split)
    print(new)
    print(again)
    print(x)
this ="      Harry is a good teacher        "
remove_and_split(this,"Harry")    

