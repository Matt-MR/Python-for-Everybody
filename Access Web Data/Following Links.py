import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter URL: ")
count = int(input("Enter count:"))      #How many times you want to repeat the process
position = int(input("Enter position:"))    #Which position to click the link

for names in range(count):

    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup("a")    #Find anchor tags
    htmls = []
    names = []
    for tag in tags:
        x = tag.get("href", None)
        htmls.append(x)
        y = tag.text
        names.append(y)

    print(htmls[position-1])
    print(names[position-1])
    url = htmls[position-1]
  