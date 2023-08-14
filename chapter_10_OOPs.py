# It is mainly use to increase the reuseability of the code.
# OOps is implemented in (DRY)==Do not repear yourself.
# PROCEDIRAL ORIENTED PROGRAMMING:
# a=12
# b=34
# print ("The sum of a and b is",a+b) 
# OBJECT ORIENTED PROGRAMMING:
class number:
    def sum (self):
        return self.a +self.b
num=number()
num.a=12
num.b=35
s=num.sum()
print (s)
# class Test :(Test ka "T" capital me hai q ki class ka nam pascle case me likha jata hai )
# method & variables
'''Pascle case:
EmployeeName---->PascleCase
#  In pascle case first letetr and the next word leters are started in upper case 
Camel case:
isNumeric,isFloatOrInt------->camelCase 
#  In camel case first letetr is lower case and the next word leters are started in upper case
Focus on the naming of pascle case and camel case.'''


