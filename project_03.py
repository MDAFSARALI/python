class Library:
    def __init__(self,listofBooks):
        self.books=listofBooks
    def displayAvailableBooks(self):
        print ("Books present in this library are : ")
        for book in self.books:
            print (" *"+ book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been isseued {bookName} please keep it safe! and return it within 30 days. ")
            self.books.remove(bookName)
            return True
        else:
            print ("Sorry this book is either not Available now or somebody issued it  !! Please wait untill the book is available.")
            return False

    def returnBook(self,bookName):
        def __init__(self):
            self.book=[]
        self.books.append(bookName)
        print ("Thanks for returning this book ! Hope you have enejoyed it. Have a great day ahead!!")
class Student:
    def requestBook(self):
        self.book=input("Enter the name of the book you want to borrow!: ")
        return self.book

    def returnBook(self):
        self.book=input("Enter the name of the book you want to return or add!: ")
        return self.book
        
if __name__=="__main__":
    centralLibrary=Library(["Algorithms","Django","Clrs","Python Notes"])
    student=Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg='''\n========Welcome to central library =======
        please choose an option :
        1.List all the books
        2.Request a book
        3.Add/Return a book 
        4.Exit the library
        '''
        print(welcomeMsg)
        a=int(input("Enter a choice!!"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing central Library.! Have a great day ahead!")
            exit()
        else:
            print ("Invalid choice !")
        
        