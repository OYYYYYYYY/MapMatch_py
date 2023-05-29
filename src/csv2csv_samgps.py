import pandas as pd
import numpy as np
import csv
import math

# 读取数据文件
with open('./data/cd_taxi/cdc_0828.csv', 'rt') as f:
    reader = csv.DictReader(f)
    lngs = []
    lats = []
    times = []
    days = []
    for row in reader :
        # 将经纬度字符串转换为数值
        temp0 = float(row['lng'])
        temp1 = float(row['lat'])
        # 将时间字符串转换为数值
        h, m, s = row['time'].strip().split(':')
        temp2 = int(h) * 3600 + int(m) * 60 + int(s)
        temp3 = int(row['day'])
        if(temp2 % 60 == 0):
            lngs.append(temp0)
            lats.append(temp1)
            times.append(temp2 / 60)
            days.append(temp3)

print("read data file")
with open('./data/cd_taxi/sample_60s_d25.csv','w') as fw:
    fw.write('lng,lat,time,day\n')
    for s in range(len(lngs)):
        fw.write((str(lngs[s])+','+str(lats[s])+','+str(times[s])+','+str(days[s])+'\n'))