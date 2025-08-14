# Task -1: Web Scraper Example
# Requirements:
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def scrape_titles(url, tag, class_name=None):
    try:
        # Send an HTTP request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all elements by tag and optional class name
    if class_name:
        elements = soup.find_all(tag, class_=class_name)
    else:
        elements = soup.find_all(tag)

    # Extract and clean text from elements
    titles = [el.get_text(strip=True) for el in elements]
    return titles

# Example usage:
if __name__ == "__main__":
    # Replace with the website you want to scrape 
    url = "https://quotes.toscrape.com/"
    
    # Example: Extract all quote texts from <span class="text">
    data = scrape_titles(url, "span", "text")

    print("\nExtracted Data:")
    for idx, item in enumerate(data, start=1):
        print(f"{idx}. {item}")
