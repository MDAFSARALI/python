            #File I/O:
'''types of file I/O:
1)Text file (.ext,.c etc)
2)Binary files(.jpg,.dat,etc)
OPENING FUNCTION:
open("this.text","mode")//mode=read,write,append'''
# Use open function to read the content of the file.
f=open('chapter_09_01.txt','r')#If we dont specify the mode then it automatically receive the "r"
# f=open('chapter_09_01.txt') #for reading both lines are True
# data=f.read()-----(1)
afsar=f.read(8)# It will only read 8 characters.--------(2)
# print(data)--------(1)
print(afsar)#---------(2)
f.close() #It is necessarily for closing the file.