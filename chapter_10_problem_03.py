class Sample:
    a="Harry"#It is a class attribute
obj=Sample()
obj.a="Vicky"# It is a instance attribute.
print (Sample.a)#No class attribute will not be change 
print (obj.a)
# If We want to change the class attribute then we have to write 
# Sample.a="Afsar" // Here we have changed the class attribute "Harry" to "Afsar"
# print (Sample.a)
