import requests
from bs4 import BeautifulSoup

# Target website
url = 'https://ignalina.lt/'

# Send HTTP GET request
response = requests.get(url)

# Check if the request succeeded
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all paragraph elements
    paragraphs = soup.find_all('p')

    print("Paragraphs from Ignalina.lt:")
    for i, p in enumerate(paragraphs, 1):
        text = p.get_text(strip=True)
        # Print only non-empty paragraphs
        if text:
            print(f"{i}. {text}")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
    
