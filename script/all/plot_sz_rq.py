#!/usr/bin/env python
#encoding:utf-8
import numpy as np  
import pandas as pd  
import matplotlib as mpl
mpl.use('Agg') 
from matplotlib.pyplot import *

import sys

#mpl.rcParams['font.family'] = ['sans-serif']
#mpl.rcParams['font.sans-serif'] = ['SimHei']
myfont = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/truetype/simhei.ttf')
begin_date = sys.argv[1]
end_date = sys.argv[2]
#begin_date = '2015-06-01'
#end_date = '2015-08-07'
SCALE = 10

figure(figsize=(20,12), dpi=200)
title(begin_date + u' ~ ' + end_date + u' 深市每日融券余额及增减图', fontproperties=myfont, fontsize = 28)
#df = pd.read_csv('sh_rzrq_result.txt', index_col=0, parse_dates=True)
df = pd.read_csv('../../data/sz_rzrq_result_all.txt', index_col=0)
df = df.sort_index().loc[begin_date:end_date,'rqzj']

df1 = df.copy()
df1[df1.values < 0] = 0
df1[df1.values > SCALE] = SCALE
df1.plot(kind='bar', color='red', label=u'较前一日0-%s亿的增加量' %SCALE)

df2 = df.copy()
df2[df2.values > 0] = 0
df2[df2.values < -SCALE] = -SCALE
df2.plot(kind='bar', color='green', label=u'较前一日0-%s亿的减少量' %SCALE)

legend(loc='best')
ylim(-SCALE * 1.05, SCALE * 1.05)
#yticks([-SCALE, -SCALE/2, 0, SCALE/2, SCALE],
#       [r'$-10$', r'$-5$', r'$0$', r'$5$', r'$10$'], fontsize=18)
#ylabel(u'每日融券增减 (亿)', fontproperties=myfont, fontsize=18)
yticks([-SCALE, -SCALE/2, 0, SCALE/2, SCALE],
       [r'$0$', r'$12.5$', r'$25$', r'$37.5$', r'$50$'], fontsize=24)
ylabel(u'每日融券余额 (亿)', fontproperties=myfont, fontsize=24)
axhline(0,linestyle='-',linewidth=1, color='black')
grid(True)
ax1 = gca()
leg = ax1.get_legend()
ltext  = leg.get_texts()
setp(ltext, fontproperties=myfont, fontsize=24)
ax2 = ax1.twinx()

df7 = pd.read_csv('../../data/sz_rzrq_result_all.txt', index_col=0)
df7 = df7.sort_index().loc[begin_date:end_date,'rqye']
df7 = (df7 - 25) / 2.5
df7.plot(color="#EE00EE",linewidth=2.5,linestyle="-")

#xticks([])
x_min, x_max = ax2.get_xlim()
xlim(x_min - 1, x_max + 1)
ylim(-SCALE * 1.05, SCALE * 1.05)
#yticks([-SCALE, -SCALE*3/4, -SCALE/2, -SCALE/4, 0, SCALE/4, SCALE/2, SCALE*3/4, SCALE],
#       [r'$-20$', r'$-15$', r'$-10$', r'$-5$', r'$0$', r'$5$', r'$10$', r'$15$', r'$20$'], fontsize=18)
#yticks([-SCALE, -SCALE/2, 0, SCALE/2, SCALE],
#       [r'$0$', r'$12.5$', r'$25$', r'$37.5$', r'$50$'], fontsize=18)
#ylabel(u'每日融券余额 (亿)', fontproperties=myfont, fontsize=18)
yticks([-SCALE, -SCALE/2, 0, SCALE/2, SCALE],
       [r'$-10$', r'$-5$', r'$0$', r'$5$', r'$10$'], fontsize=24)
ylabel(u'每日融券增减 (亿)', fontproperties=myfont, fontsize=24)

savefig(u'../../pic/sz_rq_%s_Fig.jpg' %end_date, dpi=200)  
