with open("log.txt") as f:
    content=f.read().lower()
if 'python' in content :#Case sensative hai agar python ka P upper case me likh diye to detect nahi kar payega.
    print("Yes python is present") 
else:
    print (" No! python is not present")

# BY the use of lower() we can detect either python is written in any case 
# We have written python in 327 line no.
# we can also write if 'python' in content.lower() in line no 3 if we  dont write lower() in 2nd line .