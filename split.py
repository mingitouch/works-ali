import sys
import os
import string

if __name__ == '__main__':
    n = int(sys.argv[1])
    inputFile = sys.argv[2]
    filename = [str(i) for i in range(n)]
#    print filename
    lineNum = string.atoi(os.popen('wc -l ' + inputFile).read().split(' ')[0])
    
    step = int(round(lineNum * 1.0 / n))
    file = open(inputFile)
    perfix = 'splitData/'
    count = 0
    i = 0
    fp = []
    for item in filename:
        fp.append(open(perfix+item, 'w'))
    
    for line in file:
        if count < step:
            fp[i].write(line)
            count += 1
        else:
            print count * (i+1)
            count = 0
            i += 1
            fp[i].write(line)

    for item in fp:
        item.close()
    file.close()
