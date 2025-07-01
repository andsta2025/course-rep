from book import Book
from library import Library

def print_menu():
    print("\nLibrary Menu:")
    print("1. Add a new book")
    print("2. Remove a book by title")
    print("3. Find a book by title")
    print("4. List all books")
    print("5. Exit")

def main():
    library = Library()
    print("Welcome to the Library CLI!")

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            year_str = input("Enter year: ").strip()
            if not year_str.isdigit():
                print("Invalid year. Book not added.")
                continue
            year = int(year_str)
            new_book = Book(title, author, year)
            library.add_book(new_book)

        elif choice == '2':
            title = input("Enter the title of the book to remove: ").strip()
            library.remove_book(title)

        elif choice == '3':
            title = input("Enter the title of the book to find: ").strip()
            library.find_book_by_title(title)

        elif choice == '4':
            library.list_books()

        elif choice == '5':
            print("Exiting the Library CLI. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()