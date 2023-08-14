''' We identify the following in our program:
Noun---->class---->Employee
Adjective--->Attributes--->name,age,salary
verb---->Methods---->getSalary(),increment()
'''
# Class attribute:// class attribute ka matlab hua ak aisa class jiske tamam employee ka company same ho jisko indivdual to individualchange na krna pde.
class Employee:
    company="Google"
    # If we write: salary=100 then what will be printed in (afsar.salary)?
    # Firstly it will be check in object whether any class attribute is present or not if there is not present then it eill check in class attribute .
    # To understand the upper line first uncomment the line 23 and 24 and  9 and then vice versa.
    salary=100
afsar=Employee()
afzal=Employee()
# afsar.salary=15
print(afsar.company)
print(afzal.company)
Employee.company="YouTube"
print(afsar.company)
print(afzal.company)
# instance attribute:// Afsar and afzal ka salary and name ye sab alag hai isi liye us sabho ko instance attribute me rakhenge indivdual to indivdual 
afsar.name="AFSAR"
afzal.name="AFZAl"
afsar.salary=300
afzal.salary=400
print (afsar.salary)
print (afzal.salary)
print (afsar.name)
print (afzal.name)
# print (afsar.address)  //'Employee' object has no attribute 'address'--->Error
