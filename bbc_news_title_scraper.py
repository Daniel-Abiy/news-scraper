import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h2', class_='sc-8ea7699c-3 dhclWg')

    print("Latest News Headlines:")
    
    for idx in range(len(headlines)):
        headline = headlines[idx]
        title = headline.get_text(strip=True)
        link = headline.find_parent('a')['href']
        full_link = f"https://www.bbc.com{link}" if link.startswith('/') else link
        print(f"{idx}. {title} - {full_link}")
else:
    print(f"Failed to retrieve the page.")
