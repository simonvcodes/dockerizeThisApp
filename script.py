import requests as rq
from bs4 import BeautifulSoup

url = "https://mate-solutions.de/"
if ("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)
soup = BeautifulSoup(data.text, "html.parser")
links = []
for link in soup.find_all("a"):
    print(link)
