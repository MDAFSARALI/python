'''def readfile(filename):
    with open(filename,"r") as f:
       print ( f.read())

readfile("1.txt")
readfile("2.txt")
readfile("3.txt")'''
def readfile(filename):
    try:
        with open(filename,"r") as f:
         print ( f.read())
    except FileNotFoundError as e:
         print (f"File {filename} is not found")
        # print (e)


readfile("a.txt")
readfile("b.txt") # Now if we delete the b.txt from the file will not be present in the terminal so it will show that the file b.txt is not found<---
readfile("c.txt")
