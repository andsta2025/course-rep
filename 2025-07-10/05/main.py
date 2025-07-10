from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the database URL (SQLite local file)
DATABASE_URL = "sqlite:///books.db"

# Create database engine and base class
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

# Define Book model
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer)

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year})>"

# Create the books table
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

# CRUD operations
def add_book(title, author, year):
    session = Session()
    new_book = Book(title=title, author=author, year=year)
    session.add(new_book)
    session.commit()
    session.close()
    print(f"Added: {new_book}")

def update_book(book_id, title=None, author=None, year=None):
    session = Session()
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        if title: book.title = title
        if author: book.author = author
        if year: book.year = year
        session.commit()
        print(f"Updated: {book}")
    else:
        print("Book not found!")
    session.close()

def delete_book(book_id):
    session = Session()
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print(f"Deleted book with ID {book_id}")
    else:
        print("Book not found!")
    session.close()

def list_books():
    session = Session()
    books = session.query(Book).all()
    print("\nAll books in the database:")
    for book in books:
        print(book)
    session.close()

# Simple text menu
def menu():
    while True:
        print("\n=== Book Management Menu ===")
        print("1. Add a book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. View all books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Enter book ID to update: "))
            title = input("New title (leave blank to keep current): ")
            author = input("New author (leave blank to keep current): ")
            year_input = input("New year (leave blank to keep current): ")
            year = int(year_input) if year_input else None
            update_book(book_id, title or None, author or None, year)
        elif choice == '3':
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)
        elif choice == '4':
            list_books()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()