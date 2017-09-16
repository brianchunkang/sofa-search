from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import os

url = "http://www.ikea.com/ca/en/catalog/categories/departments/living_room/10662/"
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")

imgs = soup.findAll("div", {"class":"threeColumn product "})

counter = 0
information = []

for img in imgs:
    url2 = "http://www.ikea.com"+img.a['href']
    print(url2)
    html2 = urlopen(url2)
    soup2 = BeautifulSoup(html2, "lxml");
    img_needed = soup2.find("div", {"class":"rightContentContainer"})

    img_url = "http://www.ikea.com" + img_needed.img['src']

    urlretrieve(img_url, os.path.basename("scraped-sofas\sofa_" + str(counter) + ".jpg"))

    counter += 1;

    information.append({
        "link": url2, 
        "img-link": img_url, 
        "name": soup2.find("div", {"class":"productName"}).decode_contents(formatter="html").strip()
        })

print(information)
