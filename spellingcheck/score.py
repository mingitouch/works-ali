#coding=utf-8

import urllib2
import csv
import re
import time
import sys
import cookielib
import os
import urllib

base = 'http://www.aliexpress.com/wholesale?'

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
pattern = 'Do you mean:(.*)'
patt = ' <a(.*)>(.*)<\/a>'

header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrom\
   e/28.0.1500.72 Safari/537.36' }

def download():
    reader = csv.reader(open('check'))
    output = open('output','w')
    token = {}
    for key, value, score in reader:
        if token.has_key(key):
            token[key].append([value, score])
        else:
            token[key] = [[value, score]]
    
    for key in token:
        content = ''
        url = base + urllib.urlencode({'SearchText':key})
        print url
        try:
            request = urllib2.Request(url, headers = header)
            content = urllib2.urlopen(request, timeout=5).read()
        except:
            break
#            print url
#            return [url]

        found = re.findall(pattern, content)
        if found:
            found = found[0][0:-2]
            found = found.split(',')
            temp = []
            for item in found:
                find = re.findall(patt, item)
                temp.append[find[0][1]]

            if len(temp) == 0:
                continue
            else:
                output.write(key)
            
            for item in temp:
                output.write(','+item)
            output.write('\n')

def score(benchmark):
    dictionary = {}
    reader = None
    if benchmark == 'amazon':
        reader = csv.reader(open('amazoncheckNew'))
    elif benchmark == 'ebay':
        reader = csv.reader(open('ebaycheckNew'))

    for line in reader:
        key = line[0]
        value = line[1]
        key = key.replace('+',' ')
        dictionary[key] = value

    reader = csv.reader(open('output'))
    cnt = len(dictionary)
    count = 0
    hitcnt = 0
    accuracycnt = 0
    for line in reader:
        if count % 100 == 0:
            #print count
            pass
        count += 1
        key = line[0]
        key = key.replace('+', ' ')
        value = line[1:3]#line[1:]
        if dictionary.has_key(key):
            if dictionary[key] in value:
                hitcnt += 1
        accuracycnt += len(value)
        
    print 1.0 * hitcnt / cnt, 1.0 * hitcnt / accuracycnt


print 'amazon',
score('amazon')
print 'ebay',
score('ebay')
