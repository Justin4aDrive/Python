import requests
from bs4 import BeautifulSoup

url = "https://pixelford.com/blog/"
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
response = requests.get(url, headers=HEADERS)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

a_tags = soup.find_all('a', class_="entry-title-link")

for a_tag in a_tags:
    print(a_tag.get_text())

titles = list(map(lambda a_tag: a_tag.get_text(), a_tags))
print(titles)
              





