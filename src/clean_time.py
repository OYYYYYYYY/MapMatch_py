import pandas as pd
import numpy as np
import csv
import math
import osm2gmns as og
import datetime


# 读取数据文件
with open('./data/cd_taxi/sample_data_30s/chengdu08.csv', 'rt') as f:
    reader = csv.DictReader(f)
    lngs = []
    lats = []
    times = []
    dates = []
    for row in reader :
        # 将经纬度字符串转换为数值
        temp0 = float(row['lng'])
        temp1 = float(row['lat'])
        lngs.append(temp0)
        lats.append(temp1)
        times.append(int(row['time']))
        dates.append(int(row['day']))
count_gps = len(times)
print("Load gps data\n")

for i in range(count_gps):
    times[i] = times[i] / 30

with open('./data/cd_taxi/sample_data_30s/chengdu08_new.csv', 'w') as fw:
    fw.write('lng,lat,time,day\n')
    for s in range(len(lngs)):
        fw.write((str(lngs[s])+','+str(lats[s])+','+str(int(times[s]))+','+str(int(dates[s]))+'\n'))