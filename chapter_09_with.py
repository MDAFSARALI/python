with open('chapter_09_with.txt','r') as f:
    a=f.read()
with open('chapter_09_with.txt',"w") as f:
    a=f.write("Me")
print(a)
# this is the best method to open or close 
# it does not need for write f.close()