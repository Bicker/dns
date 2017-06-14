import json
from pprint import pprint
from sortedcontainers import SortedDict

f = open('list02', 'r')
d = {}

f2 = open('output', 'r')
d2 = SortedDict(json.loads(f2.read()))

for line in f.readlines():
    tmp = line.strip('\n').split('|')

    if len(tmp) == 3:
        if tmp[1].strip(' ') in d:
            if d[tmp[1].strip(' ')] != (tmp[0].strip(' '), tmp[2].strip(' ')):
                # print d[tmp[1].strip(' ')], (tmp[0].strip(' '), tmp[2].strip(' '))
                print tmp[1].strip(' '), tmp[0].strip(' ')

        d[tmp[1].strip(' ')] = (tmp[0].strip(' '), tmp[2].strip(' '))

# for tld in d2:
#     for host in d2[tld]:
#         print tld, d[d2[tld][host][0]][1]
#
# for i in d:
#     print d[i]
