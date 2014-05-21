import urllib2
import urllib
import re
import time
base = 'http://10.98.108.151:2088/cs?filters=qpsc&encode=utf-8&'

def getContent(url):
    header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36' }
    try:
        request = urllib2.Request(url, headers = header)
        content = urllib2.urlopen(request, timeout=5).read()
    except:
        return [url]

    pattern = '"q" : "(.*)"'
    scorepattern = '"score" : (.*)'
#    pattern = amazonPattern
#    patt = '<a (.*)>(.*)<\/a>'
    found = re.findall(pattern, content)
    score = re.findall(scorepattern, content)
    if found:
#        found = re.findall(patt, found[0])
#        keyword = found[0][-1]
        return found, score
#        return keyword
    else:
        return False, False

def download(filename):
    file = open(filename)
    output = open('jiangAE','w')
    result = []
    count = 0
    begin = time.time()
    for line in file:
        if count % 10000 == 0:
            print count
        if count == 99093:
            break
        count += 1
        line = line.split(',')
        key = ' '.join(line[:-1])
        query = urllib.urlencode({'query':key})
        found, score = getContent(base+query)
        if found == False:
            output.write(str(key)+','+str(found)+'\n')
        else:
            n = len(found)
            for i in range(n):
                output.write(str(key)+','+str(found[i])+','+str(score[i])+'\n')

    output.close()
    end = time.time()
    print end-begin
        
        
        
if __name__ == '__main__':
    filename = '../jiangTOP'
    download(filename)
