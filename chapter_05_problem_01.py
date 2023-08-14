Mydictionary={
    "Pankha":"Fan",
    "Dabba":"Box",
    "Wastu":"Item"
}
print ("Options are ",Mydictionary.keys())
a=input("Enter the hindi word\n")
  #print ("The meaning of your word is :",Mydictionary[a])
  #Below line will not throw any error if the key is not present in the dictionary.
print ("The meaning of your word is :",Mydictionary.get(a))