#!/usr/bin/python


import bs4
import csv
import requests

noxpage = requests.get('http://plants.usda.gov/java/noxComposite')

soup = bs4.BeautifulSoup(noxpage.text)
rows = soup.select('tr.rowon')

csvfile = open('noxious_plants.csv', 'wb') 
csv_writer = csv.writer(csvfile, delimiter=',')
csv_writer.writerow(['Scientific Name', 'Common Name', 'Federal Noxious Status', 'State Noxious Status', 'Native Status'])

for r in rows:
    cols = r.findAll('td')
    sciname = cols[0].text
    comname = cols[1].text
    fnox    = cols[2].text
    snox    = cols[3].text
    native  = cols[4].text

    csv_writer.writerow([sciname.encode('utf8'), comname, fnox, snox, native])





