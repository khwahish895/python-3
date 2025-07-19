import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

# Configuration
BASE_URL = "https://example.com"  # Replace with the target website
SAVE_DIR = "website_data"

# Create directory to save data
os.makedirs(SAVE_DIR, exist_ok=True)

def download_file(url, folder):
    """Download a file from a URL and save it to a specified folder."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        filename = os.path.join(folder, os.path.basename(url))
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def scrape_website(url):
    """Scrape the website and download HTML, images, and other resources."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Save HTML content
        html_filename = os.path.join(SAVE_DIR, "index.html")
        with open(html_filename, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"Saved HTML to {html_filename}")

        # Download images
        for img in soup.find_all('img'):
            img_url = img.get('src')
            if img_url:
                # Handle relative URLs
                img_url = urllib.parse.urljoin(url, img_url)
                download_file(img_url, SAVE_DIR)

        # Download CSS and JS files
        for link in soup.find_all('link', href=True):
            css_url = link.get('href')
            if css_url.endswith('.css'):
                css_url = urllib.parse.urljoin(url, css_url)
                download_file(css_url, SAVE_DIR)

        for script in soup.find_all('script', src=True):
            js_url = script.get('src')
            js_url = urllib.parse.urljoin(url, js_url)
            download_file(js_url, SAVE_DIR)

        # Handle pagination (if applicable)
        next_page = soup.find('a', text='Next')  # Adjust based on the site's pagination
        if next_page:
            next_page_url = urllib.parse.urljoin(url, next_page['href'])
            scrape_website(next_page_url)  # Recursively scrape the next page

    except Exception as e:
        print(f"Failed to scrape {url}: {e}")

# Start scraping
scrape_website(BASE_URL)
print("Website data download complete.")
