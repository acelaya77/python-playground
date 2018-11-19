#!/usr/bin/env python

from random import *
from beautifultable import BeautifulTable

import os
import string
import random
import json
import csv


random.seed = (os.urandom(1024))
chars = string.ascii_letters + string.digits + '-_.'
names = json.loads(open('names.json').read())

'''
# Example table output
table = BeautifulTable()

table.column_headers=["FirstName","LastName"]
for name in names:
    table.append_row([name["firstname"],name["lastname"]])

print(table)

######
'''
item = {}
list = []
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['First_Name','Last_Name','User_Name','Password']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for name in names:
        name_extra = ''.join(random.choice(string.digits))

        username = str(name["firstname"]).lower() \
            + '.' \
            + str(name["lastname"]).lower() \
            + random.choice(['@yahoo.com','@gmail.com','@microsoft.com','@msn.com'])
        password = ''.join(random.choice(chars) for i in range(8))

        item['First_Name'] = name["firstname"]
        item['Last_Name'] = name["lastname"]
        item['User_Name'] = username
        item['Password'] = password
        list.append(item)
        writer.writerow(item)
