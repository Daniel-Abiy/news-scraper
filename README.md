# News Scraper - Latest Headlines from BBC

## Description
This Python script scrapes the latest news headlines from the BBC News website. It uses the `requests` library to fetch the webpage and the `BeautifulSoup` library to parse and extract news headlines. The script then prints out the list of headlines along with their associated links.

## Features
- Scrapes the latest headlines from BBC News.
- Displays the title of each headline along with a link to the full article.
- Uses `requests` to fetch the webpage and `BeautifulSoup` to parse the HTML content.

## Requirements
- Python 3.x.
- The `requests` library to fetch the webpage. Install it using the following command:

   ```bash
   pip install requests
   ```

- The `BeautifulSoup` module from `bs4` to parse the HTML content. Install it using the following command:

   ```bash
   pip install beautifulsoup4
   ```

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Daniel-Abiy/news-scraper
   ```

2. Navigate to the project folder:

   ```bash
   cd news-scraper
   ```

3. Install the required libraries:

   ```bash
   pip install requests beautifulsoup4
   ```

4. Run the news scraper script:

   ```bash
   python news_scraper.py
   ```

## How to Use
1. Run the script, and it will fetch the latest news headlines from the BBC News homepage.
2. The headlines will be printed in the console with their respective links.

## Example Output

```
Latest News Headlines:
0. BBC News - https://www.bbc.com/news
1. World News - https://www.bbc.com/news/world
2. Business News - https://www.bbc.com/news/business
...
```

## Contributing
Feel free to fork the project, make improvements, and submit pull requests.

## License
This project is open-source and available under the MIT License.
