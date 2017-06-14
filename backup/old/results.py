from pprint import pprint

import json

if __name__ == "__main__":
    f = open('output', 'r')
    data = json.loads(f.read())
    pprint(data)
