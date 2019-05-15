
from bs4 import BeautifulSoup as bs
import requests
import csv
import lxml.html


my_url = "https://www.yachtworld.com/core/listing/cache/searchResults.jsp?price=0-300000&page=2&uom=ft&length=22-48&pageSize=50&boatType=sail&fractionalShares=0&currency=USD&No=0&ps=50"

source = requests.get(my_url).text

soup = bs(source, 'lxml')


with open("my_html_results.html", "w") as my_file:
    my_file.write(soup.prettify())

""" 
listing_rows = soup.findAll("div",{ "class":"Listing row" })
print(f"This {len(listing_rows)}")
 """

""" 
for listing_row in listing_rows:
    # image_container = listing_row.findAll("div",{ "class":"image-container"})
    print(listing_row[0])
 """


# Sample output to CSV
""" csv_file = open('sample_output.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video'])
for a in as:
    csv_writer.writerow([headline, summary, video])

csv_file.close() """
