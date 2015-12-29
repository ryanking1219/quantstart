#!/usr/bin/env python
import tushare as ts
import sys

begin_date = sys.argv[1]
end_date = sys.argv[2]
#begin_date = '2015-01-01'
#end_date = '2015-08-09'

df = ts.sh_margins(start=begin_date, end=end_date)
df.to_csv('../../data/sh_rzrq_all.txt')
