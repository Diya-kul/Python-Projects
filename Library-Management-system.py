from datetime import datetime as dt, timedelta as td

class Book:
    def __init__( self, book_id, title, author, copies):
        self.book_id= book_id
        self.title =title
        self.author= author
        self.copies =copies
        
    def __str__(self):
        return f"{self.book_id} | {self.title} by {self.author} | Available: {self.copies}"
    
class user:
    def __init__( self, name):
        self.name = name
        
    def show_role(self):
        return "user"

#----------------------Member class--------------------------------------------------------------
class Member(user):
    FINE_PER_DAY =10
    
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = {}
        
    def show_role(self):
        return "Member"

#-----------Borrow book------------------------>    
    def borrow_book( self, book, days=28):
        if book.copies > 0:
            due_date = dt.now() + td( days=days )
            self.borrowed_books[ book.book_id ] = due_date
            book.copies -=1
            print( f" //book borrowed. Due date: { due_date.date()}" )
        else:
            print(" Book not avaliable.")
            
#-------------Return book--------------->
    def return_book(self, book):
        if book.book_id in self.borrowed_books:
            due_date = self.borrowed_books.pop( book.book_id )
            book.copies += 1
            
            today = dt.now()
            if today > due_date:
                late_days = (today - due_date).days
                fine = late_days * self.FINE_PER_DAY
                
                print( f" Late return! Fine: ₹{ fine}")
            
            else:
                print(" Book returned on time. No fine.")
            
        else:
            print(" You did not borroe this book. ")
            
    #----------Renue book--------------------->
    def reune_book(self, book, days=28):
        
        if book.book_id in self.borrowed_books:
            due_date = self.borrowed_books.pop( book.book_id )
            
            today = dt.now()
            if today >due_date:
                late_days = ( today - due_date).days
                fine = late_days * self.FINE_PER_DAY
                
                print( f"Late return! Fine: ₹{ fine}")
                
            else:
                print(" Book returned on time. No fine")
                
            
            due_date = dt.now() + td( days=days )    
            self.borrowed_books[ book.book_id ] = due_date 
     
#---------------admin class----------------------------------------------------------------------------       
class Admin(user):
    def show_role(self):
        return "Admin"
    
    #------FUNCTION TO CHECK STATUS OF BOOKS IN THE LIBRARY--------->
    def bookStatus(self):
    
        print(" book_id    copies avaliable       copies borrowed       Total copies")
        # ek loop laga ke dictionary ke sare item ko print kr do
    
    #-------FUNCTION TO ADD COPIES IN LIBRARY-------->
    def add_book( self, library, book):
        library.books[ book.book_id ]=book
        print(" Book added successfully.")
        
    #------function to remove books from library------>    
    def remove_book(self, library, book_id):
        if book_id in library.books:
            del library.books[book_id]
            print(" Book removed.")
        else:
            print(" Book not found.")
            
    #--------function to check records----->
    def checkRecords(self):
        print( f"Copies Present: {Book.copies}")
        print(" copies borrowed")
        print(" copies extend list")
        
#-------------library class-----------------------------------
class Library:
    def __init__(self):
        self.books = {}
        
    def display_books(self):
        if not self.books:
            print("No books avaliable.")
        else:
            print("\n------ Avaliable Books-----")
            
            for book in self.books.values():
                print(book)
    
    def get_book(self, book_id):
        return self.books.get(book_id, None)
#--------------------------------------------------------------




#-----------MAIN FUNCTION start------------------------------------------------------
def main():
    
    
    library = Library()
    
    admin =Admin("Librarian")
    
    admin.add_book( library, Book(1, "Python Programming", "Guido", 3 ))
    admin.add_book( library, Book(2, "Data Structures", "Mark Allen", 2))
    
    while True:
        print("\n=================Library Management System====================")
        print("1. Login as Admin")
        print("2. Login as Member")
        print("3. Exit")
        
        admin_choice = input(" choose option: ")
        
        if admin_choice == "1":
            while True:
                print("|------------ADMIN PANEL---------------------|")
                print(" 1. Check status of books")
                print(" 2. Add books")
                print(" 3. Remove books")
                print(" 4. Check Records")
                print(" 5. LOGOUT")
                
                #admins choice
                ch = input(" Choose Option: ")
                
                if ch == "1":
                    admin.bookStatus()
                elif ch == "2":
                    book_id = int(input("Book ID: "))
                    title = input("Title: ")
                    author = input("Author: ")
                    copies = int(input("Copies: "))
                    admin.add_book(library, Book(book_id, title, author, copies))
                elif ch == "3":
                    book_id = int(input("Book ID to remove: "))
                    admin.remove_book(library, book_id)
                elif ch == "4":
                    admin.checkRecords()
                else:
                    break
                
        elif admin.choice == "2":
            while True:
                print("\n--- Member Panel ---")
                print("1. View Books")
                print("2. Borrow Book")
                print("3. Return Book")
                print("4. Renue Book")
                print("5. Logout")

                member_choice = input("Enter choice: ")
                
                if member_choice == "1":
                    library.display_books()
                    
                elif member_choice == "2":
                    book_id = int(input("Enter Book ID: "))
                    book = library.get_book(book_id)
                    if book:
                        Member.borrow_book(book)
                    else:
                        print(" Book not found.")
                
                elif member_choice == "3":
                    book_id = int(input("Enter Book ID: "))
                    book = library.get_book(book_id)
                    if book:
                        Member.return_book(book)
                    else:
                        print(" Book not found.")
                        
                elif member_choice == "4":
                    book_id = int(input("Enter Book ID: "))
                    book = library.get_book(book_id)
                    if book:
                        Member.renue_book(book)
                    else:
                        print(" Book not found.")
                        
                else:
                    break
        
        else:
            return 0            
#-------------MAIN FUNCTION ends------------------------------------------
            
                

               


if __name__ == "__main__":
    main()