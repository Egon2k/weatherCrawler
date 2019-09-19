from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

#https://programminghistorian.org/en/lessons/working-with-web-pages
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = "https://weather.com/de-DE/wetter/stundlich/l/GMXX1530:1:GM"

#request site
req = Request(url=reg_url, headers=headers) 

#read website in html
html = urlopen(req).read() 

#soupify html
soup = BeautifulSoup(html, 'html.parser')

#search for all td tags containing the classname "temp"
for date in soup.find_all("tr", classname="clickable closed"):
 
    print(date.find("td", classname="hidden-cell-sm description").contents)
    print(date.find("td", classname="temp").contents)
    print(date.find("td", classname="feels").contents)
    print(date.find("td", classname="humidity").contents)
    print(date.find("td", classname="wind").contents)
    
    print("\n")
    
for date in soup.find_all("tr", classname=" closed"):

    print(date.find("td", classname="hidden-cell-sm description").contents)
    print(date.find("td", classname="temp").contents)
    print(date.find("td", classname="feels").contents)
    print(date.find("td", classname="humidity").contents)
    print(date.find("td", classname="wind").contents)
    
    print("\n")
