#!/bin/bash
#source ~/.bash_profile

#begin_date_1=$1
#end_date=$2
#begin_date_2=$3
begin_date_1='2015-07-30'
end_date=`date --date='1 day ago' +%Y-%m-%d`
#end_date='2015-11-01'
begin_date_2='2015-08-03'
#begin_date_2='2015-01-01'

echo $begin_date_1
echo $end_date
echo $begin_date_2

python get_sh_rzrq.py $begin_date_1 $end_date
python reshape_sh_rzrq.py $begin_date_1 $end_date
python plot_sh_rq.py $begin_date_2 $end_date
python plot_sh_rz.py $begin_date_2 $end_date

python get_sz_rzrq.py $begin_date_1 $end_date
python reshape_sz_rzrq.py $begin_date_1 $end_date
python plot_sz_rq.py $begin_date_2 $end_date
python plot_sz_rz.py $begin_date_2 $end_date
