import requests

# Your API key and CSE ID
API_KEY = 'YOUR_API_KEY'
CSE_ID = 'YOUR_CSE_ID'

# Define the search query
query = 'Python programming tutorials'

# Make the request to the Google Custom Search API
url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CSE_ID}'
response = requests.get(url)
results = response.json()

# Print the search results
for item in results.get('items', []):
    print(f"Title: {item['title']}")
    print(f"Link: {item['link']}")
    print(f"Snippet: {item['snippet']}\n")
