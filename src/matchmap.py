import pandas as pd
import numpy as np
import csv
import math
import osm2gmns as og
import datetime

# 地图匹配包
from pandas import DataFrame
from pandas import Series


# data = pd.read_csv('./data/TaxiData-Sample.csv',header = None)
# data.columns = ['VehicleNum','Time','lon','lat','OpenStatus','Speed']

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
        # print(temp2)
        lons.append(temp0)
        lats.append(temp1)
        times.append(temp2)
print("Load gps data\n")

# 创建存储张量的三个维度的数组
segments = []
timeoday = []
days = []

# 记录道路的总数

with open('./data/link_auto.csv','r') as fn:
    readern = csv.DictReader(fn)
    lane_id = []
    for rown in readern:
        lane_id.append(int(rown['link_id']))
count = len(lane_id)

# 道路总数
print("The number of links:", count)


print("\nLoad link data and record the id of links\n")

with open("./data/link_geo_temp3.csv", "r") as flr:
    readerlr = csv.reader(flr)
    rowslr = list(readerlr)
print("Read the geo file\n")

# 获取GPS数据集中每一个轨迹点与路段进行匹配 / 遍历每一条路段
for i in range(len(times)):
    # 遍历路网link_geo_p文件中每一行(每一行都为一条路段)
    flag = 0
    for l in range(count):
        with open("./data/link_geo_lane_temp.csv", "w") as flw:
            writerlw = csv.writer(flw)
            row_lane = rowslr[l]
            writerlw.writerow(row_lane)
        # with open("./data/link_geo_temp3.csv", "r") as flr, open ("./data/link_geo_lane.csv", "w") as flw:
        #     # readerl = csv.reader(fl)
        #     # rowsl = list(readerl)
        #     # row_lane = rowsl[l]
        #     readerlr = csv.reader(flr)
        #     writerlw = csv.writer(flw)
        #     rowslr = list(readerlr)
        #     row_lane = rowslr[l]
        #     writerlw.writerow(row_lane)


        # 将一行数据扩展成多行,并转换的二维数据
        with open('./data/link_geo_lane.csv', 'r') as infile, open('./data/link_geo_lane_temp.csv', 'w') as outfile:
            stripped = (line.strip() for line in infile)
            lines = ([sent] for para in (line.split(",") for line in stripped if line) for sent in para)
            writer = csv.writer(outfile)
            writer.writerows(lines)

        with open('./data/link_geo_lane_temp.csv','r') as fr3:
            lines3 = fr3.readlines()
        with open('./data/link_lane_new.csv','w') as fw3:
            fw3.write('lon,lat\n')
            for line3 in lines3:
                fw3.write(line3.replace(' ',','))
                    
        # 此时每一行表示该路段的一个坐标点(经度 纬度)
        with open('./data/link_lane_new.csv', 'r') as fla:
            reader1 = csv.DictReader(fla)
            lane_lons = []
            lane_lats = []
            for row1 in reader1 :
                temp3 = float(row1['lon'])
                temp4 = float(row1['lat'])
                lane_lons.append(temp3)
                lane_lats.append(temp4)

        for j in range(len(lane_lons)):
            if((abs(lons[i] - lane_lons[i]) < 0.000045) and (lats[i] - lane_lats[i]) < 0.000045):
                segments[i] = lane_id[l]
                timeoday[i] = times[i]
                days[i] = 1
                flag = 1
                print("road:",l,"\n")
                break
        if(flag == 1):
            print(lane_id[l])
            print("\n")
            break
        

            

with open('./data/sz.tns','w') as fw:
    fw.write('3\n')
    # fw.write((str(len(segments))+' '+str(len(timeoday))+' '+str(len(days))+'\n'))
    for s in range(len(days)):
        fw.write((str(segments[s])+' '+str(timeoday[s])+' '+str(days[s])+'\n'))

print("finish")