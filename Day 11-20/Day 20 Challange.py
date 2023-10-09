import requests
from bs4 import BeautifulSoup

url = "https://example.com" #change url to your url
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        print(link.get('title'))
else:
    print("Failed to retrieve the webpage.")
