# with open("first.txt") as f:
#     content1=f.read()
# with open("second.txt") as f:
#     content2=f.read()  
# if content1==content2:
#     print ("The contents are same")
# else:
#     print("The content are not same")

# By harry:
file1="first.txt"
file2="second.txt"
with open (file1)as f:
    f1=f.read()
with open (file2)as f:
    f2=f.read()
if file1==file2:
    print ("Files are identical")
else:
    print ("Files are not identical")