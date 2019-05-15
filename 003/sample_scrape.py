# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


""" url = ("https://www.yachtworld.com/core/listing/cache/searchResults.jsp?"
    "cit=true"
    "&slim=quick"
    "&ybw="
    "&sm=3"
    "&searchtype=advancedsearch"
    "cit=true"
    "&slim=quick"
    "&ybw="
    "&sm=3"
    "&searchtype=advancedsearch"
    "cit=true"
    "&slim=quick"
    "&ybw="
    "&sm=3"
    "&searchtype=advancedsearch"
    "&Ntk=boatsEN"
    "&Ntt="
    "&is="
    "&man="
    "&hmid=0"
    "&ftid=0"
    "&enid=0"
    "&type=%28Sail%29"
    "&fromLength=22"
    "&toLength=48"
    "&fromYear="
    "&toYear="
    "&fromPrice=0"
    "&toPrice=300000"
    "&luom=126"
    "&currencyid=100"
    "&city="
    "&pbsint="
    "&boatsAddedSelected=-1"
    "&fracts=1"
)
my_url = ("https://www.yachtworld.com/core/listing/cache/searchResults.jsp?"
    "uom=ft"
    "&currency=USD"
    "&length=22-48"
    "&price=0-300000"
    "&fractionalShares=0"
    "&boatType=sail"
    "&page=1"
    "&pageSize=100"
    "&searchtype=advancedsearch"
    ) """

my_url = "https://www.yachtworld.com/core/listing/cache/searchResults.jsp?price=0-300000&page=1&uom=ft&length=22-48&pageSize=50&boatType=sail&fractionalShares=0&currency=USD&No=0&ps=50"

""" response = requests.get(my_url)
html = response.text
 """
uClient = uReq(my_url)
page_html = uClient.read()
# print(page_html)
uClient.close()

""" try:
    with open('scrape_results.html', 'w') as output_file:
        output_file.write(page_html)
except:
    print("exception error")

print(output_file.closed())
 """
page_soup = soup(page_html, "html.parser")



listing_rows = page_soup.findAll(class_='listing row')
info_container = page_soup.findAll("div", {"class":"information-container"})

print(page_soup.title)
print(len(info_container))

for container in info_container:
    #print(container)
    length_container = container.findAll("span", {"class":"length feet"})
    length = length_container[0].text.strip()
    print("length: " + length)

    make_container = container.findAll("a")
    #make = make_container.text.strip()
    # print("make: " + make)
    print(make_container)



"""
results = soup.find_all(id='searchResultsDetailsABTest')
listing_rows = soup.find_all(class_='listing row')

 for listing in listing_rows:
    listing.div[0]
 """
