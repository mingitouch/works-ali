import csv
import urllib

amazonReader = csv.reader(open('amazoncheckNew'))
ebayReader = csv.reader(open('ebaycheckNew'))
aliReader = csv.reader(open('check'))

query = {}

output = open('result','w')
for line in amazonReader:
    key, value = line
    if query.has_key(key):
        query[key][0] = value
    else:
        query[key] = [value, '0', []]

for line in ebayReader:
    key, value = line
    if query.has_key(key):
        query[key][1] = value
    else:
        query[key] = ['0', value, []]

for line in aliReader:
    key, value, score = line
    if query.has_key(key):
        query[key][2].append([value, score])
    else:
        query[key] = ['0', '0', [[value, score]]]

for key in query:
    temp = key.replace('+',' ')
    output.write(temp+'^'+query[key][0]+'^'+query[key][1]+'^')
    for item in query[key][2]:
        output.write(item[0]+'\x02'+item[1]+'\x01')
    if len(query[key][2]) == 0:
        output.write('0')

    output.write('\n')
    
