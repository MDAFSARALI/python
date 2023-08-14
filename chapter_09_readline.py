f=open('chapter_09_01.txt')
# read first line 
data=f.readline()# Its meaning that it will read only 1 line
print(data,end="")
# read second line 
data=f.readline() #This line will print the second line of the text file.
# data=f.readlines() #This line produces the string of the all lines in the text
print(data,end="")
# read third line
data=f.readline()
print(data,end="")
# read forth line
data=f.readline()
print(data,end="")
# Read fifth line
data=f.readline()
print(data,end="")
f.close()

''' Mode of opening a file:
r--->Open for reading
w--->Open for writing
a--->Open for appending(Adding data at the end of the file)
+--->open for updating====(read+write)
'rb' will open for read in binary mode
'rt' will open for reading in text mode'''