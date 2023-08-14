# f=open("poem.txt","r")
# a=f.read()
# # x=a.count("twinkle") #This shows how many times we found the word twinkle
# x=a.find("twinkle") # The output of this is 9 (it is the position) starting from 0;
# print(x)
# f.close()
                # Code with harry:
f=open('poem.txt') # It will automaaticlly open in read mode.
t=f.read()
if 'twinkle' in t:
    print("'twinkle' word is available in the poems.txt")
else:
    print("'twinkle' word is not available in the poems.txt")
f.close()