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
SCALE = 500

figure(figsize=(20,12), dpi=200)
title(begin_date + u' ~ ' + end_date + u'  沪市每日融资余额及增减图', fontproperties=myfont, fontsize = 28)
#df = pd.read_csv('sh_rzrq_result.txt', index_col=0, parse_dates=True)
df = pd.read_csv('../../data/sh_rzrq_result_all.txt', index_col=0)
df = df.sort_index().loc[begin_date:end_date,'rzzj']

df1 = df.copy()
df1[df1.values < 0] = 0
df1[df1.values > SCALE] = SCALE
df1.plot(kind='bar', color='red', label=u'较前一日0-500亿的增加量')

df2 = df.copy()
df2[df2.values > 0] = 0
df2[df2.values < -SCALE] = -SCALE
df2.plot(kind='bar', color='green', label=u'较前一日0-500亿的减少量')

df3 = df.copy()
df3 = df3 - SCALE
df3[df3.values < 0] = 0
df3[df3.values > SCALE] = SCALE
if (df3 > 0).any():
    df3.plot(kind='bar', color='yellow', label=u'较前一日500-1000亿的增加量')

df4 = df.copy()
df4 = df4 + SCALE
df4[df4.values > 0] = 0
df4[df4.values < -SCALE] = -SCALE
if (df4 < 0).any():
    df4.plot(kind='bar', color='cyan', label=u'较前一日500-1000亿的减少量')

df5 = df.copy()
df5 = df5 - SCALE * 2
df5[df5.values < 0] = 0
if (df5 > 0).any():
    df5.plot(kind='bar', color='white', label=u'较前一日1000-1500亿的增加量')

df6 = df.copy()
df6 = df6 + SCALE * 2
df6[df6.values > 0] = 0
if (df6 < 0).any():
    df6.plot(kind='bar', color='blue', label=u'较前一日1000-1500亿的减少量')

#df1.plot(color="yellow",linestyle="-o")
#xticks(np.arange(len(df.index)), df.index, rotation='vertical')
legend(loc='best')
ylim(-SCALE * 1.05, SCALE * 1.05)
#yticks([-SCALE, -SCALE/2, 0, SCALE/2, SCALE],
#       [r'$-500$', r'$-250$', r'$0$', r'$250$', r'$500$'], fontsize=18)
#yticks([-SCALE, -SCALE*4/5, -SCALE*3/5, -SCALE*2/5, -SCALE*1/5, 0, SCALE*1/5, SCALE*2/5, SCALE*3/5, SCALE*4/5, SCALE],
#       [r'$-500$', r'$-400$', r'$-300$', r'$-200$', r'$-100$', r'$0$', r'$100$', r'$200$', r'$300$', r'$400$', r'$500$'], fontsize=18)
#ylabel(u'每日融资增减 (亿)', fontproperties=myfont, fontsize=18)
yticks([-SCALE, -SCALE*4/5, -SCALE*3/5, -SCALE*2/5, -SCALE*1/5, 0, SCALE*1/5, SCALE*2/5, SCALE*3/5, SCALE*4/5, SCALE],
       [r'$5000$', r'$6000$', r'$7000$', r'$8000$', r'$9000$', r'$10000$', r'$11000$', r'$12000$', r'$13000$', r'$14000$', r'$15000$'], fontsize=24)
ylabel(u'每日融资余额 (亿)', fontproperties=myfont, fontsize=24)
axhline(0,linestyle='-',linewidth=1, color='black')
grid(True)
#grid(ydata=np.arange(-SCALE, SCALE, 100))
ax1 = gca()
x_min, x_max = ax1.get_xlim()
xlim(x_min - 1, x_max + 1)
leg = ax1.get_legend()
ltext  = leg.get_texts()
setp(ltext, fontproperties=myfont, fontsize=18)
ax2 = ax1.twinx()

df7 = pd.read_csv('../../data/sh_rzrq_result_all.txt', index_col=0)
df7 = df7.sort_index().loc[begin_date:end_date,'rzye']
df7 = df7 / 10 - 1000
#df7.plot(color="#FF9900",linewidth=2.5,linestyle="-")
df7.plot(color="#EE00EE",linewidth=2.5,linestyle="-")

#xticks([])
x_min, x_max = ax2.get_xlim()
xlim(x_min - 1, x_max + 1)
ylim(-SCALE * 1.05, SCALE * 1.05)
#yticks([-SCALE, -SCALE/2, 0, SCALE/2, SCALE],
#       [r'$5000$', r'$7500$', r'$10000$', r'$12500$', r'$15000$'], fontsize=18)
#yticks([-SCALE, -SCALE*4/5, -SCALE*3/5, -SCALE*2/5, -SCALE*1/5, 0, SCALE*1/5, SCALE*2/5, SCALE*3/5, SCALE*4/5, SCALE],
#       [r'$5000$', r'$6000$', r'$7000$', r'$8000$', r'$9000$', r'$10000$', r'$11000$', r'$12000$', r'$13000$', r'$14000$', r'$15000$'], fontsize=18)
#ylabel(u'每日融资余额 (亿)', fontproperties=myfont, fontsize=18)
yticks([-SCALE, -SCALE*4/5, -SCALE*3/5, -SCALE*2/5, -SCALE*1/5, 0, SCALE*1/5, SCALE*2/5, SCALE*3/5, SCALE*4/5, SCALE],
       [r'$-500$', r'$-400$', r'$-300$', r'$-200$', r'$-100$', r'$0$', r'$100$', r'$200$', r'$300$', r'$400$', r'$500$'], fontsize=24)
ylabel(u'每日融资增减 (亿)', fontproperties=myfont, fontsize=24)

savefig(u'../../pic/sh_rz_%s_Fig.jpg' %end_date, dpi=200)
