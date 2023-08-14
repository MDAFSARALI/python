def rectangle( length, breadth):
    print (f"The area of the rectangle of length {length} and breadth {breadth} is " + str(length*breadth))
def sqare(side):
    print (f"The area of the square having length {side} is " + str(side*side))
length=int (input("Enter the lenght for rectangle  :"))
breadth=int (input("Enter the breadth for rectangle  :"))
side=int (input("Enter the length of side of the square : "))
rectangle(length,breadth)
sqare(side)
