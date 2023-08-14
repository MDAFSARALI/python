import os
oldname="afsar.txt"
newname="renamed_by_python.txt"
with open (oldname) as f:
    content=f.read()
with open (newname,"w") as f:
    new=f.write(content)
#  We wantto delete the 123.txt file bcz after running the code we have the oldname file also available here iska matlab rename to hua nahi shirf af new file ban gya nam renamed_by_python.txt ho kr 
# is liye hame woh purana file oldname wala delete karna padega.
os.remove(oldname)