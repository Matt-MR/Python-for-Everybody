import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter the URL you wish to scrape: ")
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
numbers = list()

tags = soup("span")
for tag in tags:
    x = tag
    num = int()
    for num in x:
        count = count + 1
        numbers.append(int(num))

print("Count", count)
print("Sum", sum(numbers))
