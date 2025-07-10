from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define database URL (SQLite file)
DATABASE_URL = "sqlite:///example.db"

# Create engine and base class
engine = create_engine(DATABASE_URL, echo=True)
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

# Create tables (if they don't exist)
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a book
def add_book(title, author, year):
    new_book = Book(title=title, author=author, year=year)
    session.add(new_book)
    session.commit()
    print(f"Book '{title}' added successfully.")
# Function to fetch all books
def fetch_books():
    books = session.query(Book).all()
    return books        
# Function to update a book
def update_book(book_id, title=None, author=None, year=None):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        if title:
            book.title = title
        if author:
            book.author = author
        if year:
            book.year = year
        session.commit()
        print(f"Book with ID {book_id} updated successfully.")
    else:
        print(f"Book with ID {book_id} not found.")
# Function to delete a book
def delete_book(book_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print(f"Book with ID {book_id} deleted successfully.")
    else:
        print(f"Book with ID {book_id} not found.")
# Main function to demonstrate CRUD operations
def main():
    # Add some books
    add_book("1984", "George Orwell", 1949)
    add_book("To Kill a Mockingbird", "Harper Lee", 1960)

    # Fetch and display all books
    print("Books in the database:")
    books = fetch_books()
    for book in books:
        print(book)

    # Update a book
    update_book(1, title="Nineteen Eighty-Four")

    # Delete a book
    delete_book(2)

    # Display remaining books
    print("Remaining books after modifications:")
    books = fetch_books()
    for book in books:
        print(book)
if __name__ == "__main__":
    main()
    session.close()
    print("Database operations completed successfully.")

    print("Current books in the database:")
    books = fetch_books()
    for book in books:
        print(book)         
# This code demonstrates how to use SQLAlchemy to perform CRUD operations on a SQLite database.