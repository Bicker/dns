import matplotlib.pyplot as plt
import json

f = open('list04', 'r')
data = json.loads(f.read())

plt.bar(range(len(data)), [len(i) for i in data.values()], align='center')
plt.xticks(range(len(data)), data.keys(),rotation=90)

plt.savefig('img', dpi=1000)
