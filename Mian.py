import json
import random
name = 'dwa512'
filename = name+'.mtx'
nodeNum = 512
fileD = name+'-com.txt'
bands = list()


def load_words(filen):
    with open(filen) as f:
        for word in f:
            yield word.rstrip()

data = {}
data['nodes'] = []
data['edges'] = []

for i in range(0, nodeNum):
    data['nodes'].append({
        'id': i,
        'label': str(i),
    })

word_source = load_words(fileD)
j = 0
for line in word_source:
    line = line.split(" ")
    src = line[0]
    des = line[1]
    data['edges'].append({
        'source': int(src),
        'target': int(des),
        'id': 'e'+ str(j),
        'distance': random.randint(1, 50),
    })
    j = j + 1



with open('Graph_('+ name+" "+str(nodeNum) +').json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
