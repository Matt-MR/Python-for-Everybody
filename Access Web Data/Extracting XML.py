import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

counter = 0 
sum = 0

address = input("Enter location: ")
html = urllib.request.urlopen(address).read()

print("Retrieving", address)
print("Retreived", len(html), "characters")

tree = ET.fromstring(html)
result = tree.findall("comments/comment")

for line in result:
    num = int(line.find("count").text)
    counter = counter + 1
    sum = sum + num

print(counter)
print(sum)