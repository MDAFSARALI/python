# list=[7,14,21,28,35,42,49,56,63,70] // List ke content integer the isi liye use vertical print karne ke liye usko str me convert karna padega.
l=[str(i*7) for i in range (1,11)] #If string nahi likhenge to error dega q ki itterable nahihai mtlb list iterable nah hai # produces typeError.
print (l)
verticalTable="\n".join(l)
print (verticalTable)