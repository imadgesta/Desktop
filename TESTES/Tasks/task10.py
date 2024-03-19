import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get(url)
print(response)

soup = BeautifulSoup(response.text, "lxml")  # "html.parser"
#data = list(soup.findAll("a", class_=""))
data = soup.find("div", class_="w-full rounded border")
print(data)

name = data.find("h4", class_="p-4")
print(name)