from collections import Counter,defaultdict
from bs4 import BeautifulSoup
from pprint import pprint

import os
import glob
# import nltk
import math
import urllib2
import json

if __name__ == "__main__":
    data = {}
    url = "https://www.iana.org"
    html = urllib2.urlopen(url + "/domains/root/db")
    soup = BeautifulSoup(html)
    f = open('test', 'w')


    for item in soup.find_all(attrs={'class': 'iana-table'}):
        for link in item.find_all('a'):
            domain = link.get('href').split('/')[-1][:-5]
            print domain
            data[domain] = {}
            html = urllib2.urlopen(url + link.get("href"))
            soup2 = BeautifulSoup(html)

            for br in soup2.find_all("br"):
                br.replace_with("\n")

            for x in soup2.find_all(attrs={'class': 'iana-table'}):
                for table in soup2.find_all(attrs={'class': 'iana-table'}):
                    values = [td.get_text(strip=False) for td in table.find_all('td')]

                    for i in range(0, len(values), 2):
                        data[domain][values[i]] = values[i + 1].split("\n")[:2]


    f = open('output', 'w')
    f.write(json.dumps(data))
