import pandas as pd
import numpy as np
import csv
import math

# 读取数据文件
with open('./data/TaxiData-Sample.csv', 'rt') as f:
    reader = csv.DictReader(f)
    lons = []
    lats = []
    times = []
    for row in reader :
        # 将经纬度字符串转换为数值
        temp0 = float(row['lon'])
        temp1 = float(row['lat'])
        # 将时间字符串转换为数值
        h, m, s = row['Time'].strip().split(':')
        temp2 = int(h) * 3600 + int(m) * 60 + int(s)
        if(temp2 % 30 == 0):
            lons.append(temp0)
            lats.append(temp1)
            times.append(temp2)

with open('./data/gps_sample.csv','w') as fw:
    fw.write('lng,lat,time\n')
    for s in range(len(lons)):
        fw.write((str(lons[s])+','+str(lats[s])+','+str(times[s])+'\n'))