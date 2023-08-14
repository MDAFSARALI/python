# 01:
'''def increment (num):
    try:
        return int (num)+1
    except:
        raise ValueError ("This is a value error !!")
# a=increment(10)
a=increment('12kfg')
print (a)'''
# The above is the example of user defined error or User raised error!!!
# try--except--else(below):
# 02:
'''try:
    i=int (input("Enter a number: "))
    c=1/i
    print (c)
except Exception as e:
    print (e)
    exit()
else:# else wala portion exception part chalne ke bad nahi chalega woh tabhi chalege jab try ka code run hoga 
    print ("We were Successful !!")

# print ("Thansk for using this code!!")'''

# Use of try-except-finally:
# 03:
'''try:
    i=int (input("Enter a number: "))
    c=1/i
    print (c)
except Exception as e:
    print (e)
    exit()
finally:#{ Ye har hal me execute hoga hi hoga }
    print ("Finally we have done!!!")

print ("Thanks for using this program !!!")
# The use of finally-----> is to show ----print ("Finally we have done!!!") at any condition if we write it directly then at the time of exit() it will be ended!'''