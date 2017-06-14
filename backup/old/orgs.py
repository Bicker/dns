from collections import Counter,defaultdict
from bs4 import BeautifulSoup
from pprint import pprint

import matplotlib.pyplot as plt
import urllib2
import json

if __name__ == "__main__":
    data = {}
    url = "https://www.iana.org"
    html = urllib2.urlopen(url + "/domains/root/db")
    soup = BeautifulSoup(html)
    f = open('list04', 'w')




    # for item in soup.find_all(attrs={'class': 'iana-table'}):
    for table in soup.find_all(attrs={'class': 'iana-table'}):
        values = [td.get_text(strip=False) for td in table.find_all('td')]

        for i in range(0, len(values), 3):
            if values[i + 2] in data:
                data[values[i + 2]].append(values[i])
            else:
                data[values[i + 2]] = [values[i]]
            # print values[i], values[i + 2]
            # f.write(values[i] + '\t' +values[i+2])


    # f = open('output', 'w')
    f.write(json.dumps(data))

    # pprint(data)
    #
    # D = {u'Label1':26, u'Label2': 17, u'Label3':30}
    #
plt.bar(range(len(data)), [len(i) for i in data.values()], align='center')
plt.xticks(range(len(data)), data.keys())

plt.show('kino')
