from pprint import pprint

import json
import subprocess
import whois

if __name__ == "__main__":
    f = open('output', 'r')
    d = json.loads(f.read())
    # bashCommand = "whois -h whois.cymru.com \" -v 192.42.173.30\""
    # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()
    #
    # r = []
    # x = output.split('\n')[2:-1]
    #
    # for y in x:
    #     z = y.split('|')
    #     r.append(z[0].strip(' '))
    #
    # print r

    f = open('list03', 'w')
    f.write('begin\n')


    for tld in d:
        print tld
        for host in d[tld]:
            f.write(d[tld][host][0] + '\n')

    f.write('end\n')
