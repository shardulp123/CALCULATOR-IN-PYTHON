class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False
    
    def check_out(self):
        self.checked_out = True
        
    def check_in(self):
        self.checked_out = False
        
    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        self.books.remove(book)
        
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def display_books(self):
        print("Library Catalogue:")
        for book in self.books:
            print(book)
            if book.checked_out:
                print("Checked out")
            else:
                print("Available")
    
    def check_out_book(self, title):
        book = self.search_book(title)
        if book:
            if not book.checked_out:
                book.check_out()
                print(f"{book.title} has been checked out")
            else:
                print(f"{book.title} is already checked out")
        else:
            print(f"{title} not found")
    
    def check_in_book(self, title):
        book = self.search_book(title)
        if book:
            if book.checked_out:
                book.check_in()
                print(f"{book.title} has been checked in")
            else:
                print(f"{book.title} is already checked in")
        else:
            print(f"{title} not found")

# create library object
library = Library()

# add some books
book1 = Book("To Kill a Mockingbird", "Harper Lee", "9780446310789")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book3 = Book("1984", "George Orwell", "9780451524935")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# display catalogue
library.display_books()

# check out a book
library.check_out_book("To Kill a Mockingbird")

# display catalogue again
library.display_books()

# check in a book
library.check_in_book("To Kill a Mockingbird")

# display catalogue one more time
library.display_books()
