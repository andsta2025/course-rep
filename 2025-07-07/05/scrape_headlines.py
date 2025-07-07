import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    """
    Fetches the HTML content of the given URL and extracts headlines.
    """

    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for HTTP errors (e.g., 404, 500)
        
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: extract all <h2> tags as headlines
        headlines = soup.find_all('h2')
        
        print("Headlines found:")
        for idx, headline in enumerate(headlines, start=1):
            print(f"{idx}. {headline.get_text(strip=True)}")
    
    except requests.RequestException as e:
        # Handle network-related errors
        print("Error fetching the webpage:", e)
    except Exception as e:
        # Handle all other errors (e.g., parsing errors)
        print("An unexpected error occurred:", e)

def main():
    """
    Example usage of scrape_headlines function.
    Replace the URL with any site you want to scrape.
    """
    url = 'https://ignalina.lt/' # Replace with the website you want to scrape

    print(f"Scraping headlines from: {url}")
    scrape_headlines(url)

# This script scrapes headlines from a specified website using BeautifulSoup.

if __name__ == "__main__":
    main()