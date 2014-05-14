import csv
mapping = {}
reader = csv.reader(open('sort_query'))
count = 0
cntGEQ1 = 0
cntGEQ2 = 0
cntGEQ5 = 0
cntGEQ10 = 0
cntGEQ20 = 0
cntGEQ50 = 0
cntGEQ100 = 0
for line in reader:
    value = int(line[-1])
#    print value
    if count % 100000 == 0:
        pass
#        print count
    count = count + 1
    if value >= 2:
        cntGEQ2 += 1
    if value >= 5:
        cntGEQ5 += 1
#        print cntGEQ5
    if value >= 10:
        cntGEQ10 += 1
    if value >= 20:
        cntGEQ20 += 1
    if value >= 50:
        cntGEQ50 += 1
    if value >= 100:
        cntGEQ100 += 1

print cntGEQ2, count, cntGEQ2*1.0/count
print cntGEQ5, count, cntGEQ5*1.0/count
print cntGEQ10, count, cntGEQ10*1.0/count
print cntGEQ20, count, cntGEQ20*1.0/count
print cntGEQ50, count, cntGEQ50*1.0/count
print cntGEQ100, count, cntGEQ100*1.0/count

