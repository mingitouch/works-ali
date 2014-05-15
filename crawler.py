import urllib2
import csv
import re
import time
from multiprocessing.dummy import Pool as ThreadPool

query = []
amazon = 'http://www.amazon.com/s/ref=nb_sb_noss?field-keywords='
ebay = 'http://www.ebay.com/sch/i.html?_nkw='
base = ebay

amazonPattern = '<span class="fontSize115">\n(.*)<\/span>'
ebayPattern = 'Did you mean(.*)'
patt = '<a (.*)>(.*)<\/a>'


def getContent(url):
    header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36' }
    try:
        request = urllib2.Request(url, headers = header)
        content = urllib2.urlopen(request, timeout=10).read()
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
    reader = open('sort_query_with_pv')
    urls = []
    count = 0
    results = []
    begin = time.time()
    for line in reader:
        if count == 100:
            break
        print count
        count = count + 1
#        print line
        key, value = line.split(',')
        key = key.replace(' ','+')
        urls.append(base+key)
        query.append(key)
        results.append(getContent(base+key))
        time.sleep(2)
    end = time.time()
    print end-begin
    cnt = 0
    for item in results:
        if type(item) == list:
            cnt += 1
        print item
    reader.close()
    print cnt
    return urls

   
if __name__ == '__main__':
    urls = readKey()
#    print urls
#    crawler(urls, '')
