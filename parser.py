import time

mapping = {}

def parser(filename):
    f = open(filename)
    count = 0
    cnt = 0
    for line in f:
        if count % 10000 == 0:
#            print count
            pass
        count = count + 1
#        time, QueryLog, pv, results, search_cookie, click_cookie, order_cookie = line.split('^')

        result = line.split('^')
        QueryLog = result[1]
        #search_cookie = result[4]
        pv = result[2]
        if mapping.has_key(QueryLog):
            try:
                #mapping[QueryLog] += int(search_cookie)
                mapping[QueryLog] += int(pv)
            except:
                print line
        else:
            if len(QueryLog) < 1:
                count = count - 1
                continue
            try:
                #mapping[QueryLog] = int(search_cookie)
                mapping[QueryLog] = int(pv)
                cnt = cnt + 1
            except:
                print line
    print cnt, count
    print cnt * 1.0 / count


if __name__ == '__main__':
    file  = open('filename')
    filename = []
    for line in file:
        line = line[:-1]
        filename.append('data/'+line)
    count = 0
    begin = time.time()
    for item in filename:
#        print item
        print count,'#########'
        parser(item)
        count = count + 1
        
    end = time.time()
    print end-begin
    result = sorted(mapping.iteritems(), key=lambda d:d[1], reverse = True)
    query = open('sort_query_with_pv','w')
    count = 0
    print len(mapping)
    for key in result:
        if count % 100000 == 0:
            print count
        count = count + 1
        query.write(key[0]+','+str(key[1])+'\n')

