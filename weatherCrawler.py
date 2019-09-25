from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def parseData(tag):
    print("Time:\t" + tag.find("span", class_="dsx-date").text)
    print("Cond:\t" + tag.find("td", classname="hidden-cell-sm description").text)
    print("Temp:\t" + tag.find("td", classname="temp").text)
    print("Feel:\t" + tag.find("td", classname="feels").text)
    print("Humid:\t" + tag.find("td", classname="humidity").text)
    print("Wind:\t" + tag.find("td", classname="wind").text)
    print()

#https://programminghistorian.org/en/lessons/working-with-web-pages
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = "https://weather.com/de-DE/wetter/stundlich/l/GMXX1530:1:GM"

#request site
req = Request(url=reg_url, headers=headers)

#read website in html
html = urlopen(req).read()

#soupify html
soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

#search for all td tags containing the classname "temp"
for date in soup.find_all("tr", classname="clickable closed"):
    parseData(date)

for date in soup.find_all("tr", classname=" closed"):
    parseData(date)
