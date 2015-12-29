#!/usr/bin/env python
#coding:utf-8

from itertools import islice
fr1 = open('../../data/sh_rzrq_all.txt', 'r')
fw1 = open('../../data/sh_rzrq_result_all.txt', 'w')

fw1.write('opDate,rzye,rqye,rzrqjyzl,rzzj,rqzj' + '\n')
dict1 = {}

def format_data(yedata):
    yedata = float(yedata) / 100000000
    yedata = float('%0.2f' %yedata)
    return yedata 
    
for line in islice(fr1, 1, None):
    line = line.strip('\n')
    fields = line.split(',')
    opDate = fields[1]
    rzye = format_data(fields[2])
    rqylje = format_data(fields[5])
    rzrqjyzl = fields[7]
    dict1[opDate] = ','.join([str(rzye), str(rqylje), rzrqjyzl])
    
list1 = sorted(dict1.items(), key=lambda d: d[0])
tmp = list1[0][1]
rztmp = float(tmp.split(',')[0])
rqtmp = float(tmp.split(',')[1])

for key, value in list1:
    fields = value.split(',')
    rzye = float(fields[0])
    rqye = float(fields[1])
    rzzj = rzye - rztmp
    rztmp = rzye
    rqzj = rqye - rqtmp
    rqtmp = rqye
    print_str = key + ',' + value + ',' + str(rzzj) + ',' + str(rqzj) + '\n'
    fw1.write(print_str)

fr1.close()
fw1.close()
