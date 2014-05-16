import urllib2
import csv
import re
import time
import sys
import cookielib
import os
from multiprocessing.dummy import Pool as ThreadPool

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)

query = []
delay = {}
amazon = 'http://www.amazon.com/s/ref=nb_sb_noss?field-keywords='
ebay = 'http://www.ebay.com/sch/i.html?_nkw='
base = ''

pattern = ''

amazonPattern = '<span class="fontSize115">\n(.*)<\/span>'
ebayPattern = 'Did you mean(.*)'
patt = '<a (.*)>(.*)<\/a>'

inputpath = ''
outputpath = ''
delaypath = ''

def getContent(url):
    header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36' }
    try:
        request = urllib2.Request(url, headers = header)
        content = urllib2.urlopen(request, timeout=5).read()
    except:
        return [url]

    pattern = ebayPattern
#    pattern = amazonPattern
#    patt = '<a (.*)>(.*)<\/a>'
    found = re.findall(pattern, content)
    if found:
        found = re.findall(patt, found[0])
        keyword = found[0][-1]
        return keyword
    else:
        return False


def crawler(urls, filename):
    pool = ThreadPool(8)

    results = pool.map(getContent, urls)

    pool.close()
    pool.join()

    n = len(results)
    m = len(query)
    
    for i in range(n):
        print query[i],',',results[i]

def readKey():
    out = open(outputpath, 'w')
    outdelay = open(delaypath, 'w')
    reader = open(inputpath)
    urls = []
    count = 0
    results = []
    begin = time.time()
    for line in reader:
        if count % 1000 == 0:
	    mark = time.time()
            print count,',',mark-begin
        count = count + 1
	if count < 9722:
	    continue
#        print line
	line = line.split(',')
	value = line[-1]
	key = ' '.join(line[:-1])
        key = key.replace(' ','+')
        urls.append(base+key)
        startFlag = time.time()
        temp = getContent(base+key)
        if type(temp) == list:
            delay[key] = temp[0]
            outdelay.write(str(key)+','+str(temp)+'\n')
        else:
            query.append(key)
            results.append(temp)
            out.write(str(key)+','+str(temp)+'\n')
        endFlag = time.time()
        if endFlag-startFlag<1:
            time.sleep(1-endFlag+startFlag)
        else:
            pass
    end = time.time()
    print end-begin
    cnt = 0
    m = len(query)
    n = len(results)
    if m != n:
        print 'wrong'

#    for i in range(n):
#        out.write(str(query[i])+','+str(results[i])+'\n')
    print len(delay)
#    for k in delay:
#        outdelay.write(str(k)+','+str(delay[k])+'\n')
    reader.close()
    out.close()
    outdelay.close()
    print cnt
    return urls

   
if __name__ == '__main__':
    if sys.argv[1] == 'ebay':
        base = ebay
        pattern = ebayPattern
    elif sys.argv[1] == 'amazon':
        base = amazon
        pattern = amazonPattern
        
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]
    delaypath = sys.argv[4]
    urls = readKey()
#    print urls
#    crawler(urls, '')
