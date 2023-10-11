import requests
from bs4 import BeautifulSoup
import datetime

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
blogs = soup.find_all('article', class_="type-post")

for blog in blogs:
    title = blog.find('a', class_="entry-title-link").get_text()
    
    blog_datetime_string = blog.find('time', class_="entry-time").get('datetime')
    blog_datetime = datetime.datetime.fromisoformat(blog_datetime_string)
    pretty_date=blog_datetime.strftime("%b %d %Y")
    
    print(f"{pretty_date} - {title}")

