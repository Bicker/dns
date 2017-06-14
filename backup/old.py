# IP mapping
pbar = tqdm(total=len(data))

for item in data.copy():
    try:
        ip = socket.getaddrinfo(item['host'], None, socket.AF_INET)[-1][-1][0]
    except Exception as e:
        ip = None

    if ip and 'ip' in item:
        new_item = item.copy()
        new_item['ip'] = ip
        data.append(new_item)
    elif ip:
        item['ip'] = ip

    try:
        ip = socket.getaddrinfo(item['host'], None, socket.AF_INET6)[-1][-1][0]
    except Exception as e:
        ip = None

    if ip and'ip' in item:
        new_item = item.copy()
        new_item['ip'] = ip
        data.append(new_item)
    elif ip:
        item['ip'] = ip

    if not 'ip' in item:
        item['ip'] = None

    pbar.update(1)
pbar.close()

# html parser
url = "https://www.iana.org/domains/root/db/"
html = urlopen(url)
soup = BeautifulSoup(html, 'html5lib')
data_tld_orgs = []

for item in soup.find_all(attrs={'class': 'iana-table'}):
    for table in soup.find_all(attrs={'class': 'iana-table'}):
        values = [td.get_text(strip=True) for td in table.find_all('td')]

        for i in range(0, len(values), 3):
            data_tld_orgs.append({'tld': values[i].strip('.'), 'type': values[i + 1], 'organisation': values[i + 2]})

# Root zone parser
data = []

with open('data/root.zone') as f:
    # Skip header and root servers
    for i in range(21):
        next(f)

    for line in f:
        values = line.split()

        if values[3] == 'NS':
            tld = values[0][:-1]
            ns = values[-1][:-1]
            data.append({'host': ns, 'tld': tld})
