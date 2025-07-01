from book import Book
from library import Library
def main():
    # Create a library instance
    library = Library()

    # Create some book instances
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book4 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)   
    book5 = Book("Brave New World", "Aldous Huxley", 1932)  
    book6 = Book("Fahrenheit 451", "Ray Bradbury", 1953)    

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)

    # List all books in the library
    library.list_books()

    # Find a specific book
    library.find_book("1984")

    # Remove a book from the library
    library.remove_book("The Great Gatsby")

    # List books again to see the changes
    library.list_books()

    print(f"Is '1984' a classic? {'Yes' if book1.is_classic() else 'No'}")
if __name__ == "__main__":
    main()
# This code creates a library, adds several books to it, lists the books, finds a specific book, removes a book, and checks if a book is a classic based on its publication year
print("Library operations completed successfully.")
