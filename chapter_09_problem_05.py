words=["donkey","mote","kaddu"]
with open("list.txt") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"#####@$%^")
with open("list.txt","w") as f:
    f.write(content)
# By using this program we have sencered the bad words which is given up