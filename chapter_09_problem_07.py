content=True
i=1
with open("log.txt") as f:
    while content:
        content=f.readline()
        if 'python' in content.lower() :
            print (content)
            print(f"Yes python is present on line number {i}")
        i=i+1
 # If we add python in multiple line then we will get the all the lines.       