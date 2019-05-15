# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup as bs
import requests


url = "https://www.yachtworld.com/core/listing/cache/searchResults.jsp?cit=true&slim=quick&ybw=&sm=3&searchtype=advancedsearch&Ntk=boatsEN&Ntt=&is=&man=&hmid=0&ftid=0&enid=0&type=%28Sail%29&fromLength=22&toLength=48&fromYear=&toYear=&fromPrice=0&toPrice=300000&luom=126&currencyid=100&city=&pbsint=&boatsAddedSelected=-1&fracts=1"


response = requests.get(url)
html = response.text

try:
    with open('temp.html', 'w') as output_file:
        output_file.write(html)
except:
    print("error")



#print(response.status_code)

#print(response.text)

split = html.split("\"length feet\">")
#print(split)
temp = split[1]
split2 = temp.split("</span>")
temp2 = split2[0]

print(temp2.strip().replace('&nbsp;',' '))
