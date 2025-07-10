from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()
DATABASE_URL = "sqlite:///scraped_data.db"
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

class WebContent(Base):
    __tablename__ = 'web_contents'
    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

import requests
from bs4 import BeautifulSoup

def scrape_site(url):
    print(f"Scraping: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to load {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]
    print(f"Found {len(paragraphs)} paragraphs")
    return paragraphs

def save_paragraphs(source, paragraphs):
    session = Session()
    for text in paragraphs:
        entry = WebContent(source=source, content=text)
        session.add(entry)
    session.commit()
    session.close()
    print(f"Saved {len(paragraphs)} paragraphs from {source}")

    if __name__ == "__main__":
        websites = [
            "https://www.ignalina.lt",
            "https://www.svencionys.lt",
            "https://www.utena.lt"
        ]
    
        for site in websites:
            paragraphs = scrape_site(site)
            save_paragraphs(source=site, paragraphs=paragraphs)
    
        print("{paragraphs}")
        print("Done scraping and saving data!")


# This script scrapes paragraphs from specified websites and saves them to a SQLite database. Print scrapet data to console.
# It uses SQLAlchemy for ORM and BeautifulSoup for HTML parsing.
# The database is named 'scraped_data.db' and contains a table 'web_contents'
# with columns for ID, source URL, content, and timestamp.

print("Web scraping and database operations completed successfully.")
print("You can now query the database to see the scraped content.")
# This code defines a simple web scraping application that collects paragraphs from specified websites

print("Scraped data printed to console.")

quoery = input("Enter a query to search for specific content: ")
session = Session()
results = session.query(WebContent).filter(WebContent.content.contains(quoery)).all()
session.close()         
if results:
    print(f"Found {len(results)} entries containing '{quoery}':")
    for entry in results:
        print(f"ID: {entry.id}, Source: {entry.source}, Content: {entry.content[:100]}...")  # Print first 100 chars
else:
    print(f"No entries found containing '{quoery}'.")
# This code allows you to search the database for specific content and prints the results.

