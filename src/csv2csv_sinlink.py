import pandas as pd
import numpy as np
import csv
import math
import osm2gmns as og
import datetime

# 地图匹配包
from pandas import DataFrame
from pandas import Series

# 记录道路的总数

with open('./data/link_auto.csv','r') as f:
    reader = csv.DictReader(f)
    lane_id = []
    from_id = []
    to_id = []
    for row in reader:
        lane_id.append(int(row['link_id']))
        from_id.append(int(row['from_node_id']))
        to_id.append(int(row['to_node_id']))

# 道路总数
count = len(lane_id)
print("The number of links:", count)


print("\nLoad link data and record the id of links\n")

# with open("./data/link_geo_temp3.csv", "r") as f1:
#     reader1 = f1.readlines()
#     for line1 in reader1:
#         line1.replace(' ', ',')
#         line1_new = [int(x) for x in ]

with open("./data/link_geo_temp3.csv", "r") as f1:
    reader1 = f1.readlines()

with open("./data/link_geo_temp5.csv", "w") as f2:
    for line1 in reader1:
        f2.write(line1.replace(' ',','))

with open("./data/link_geo_temp5.csv", "r") as f3:
    rows = csv.reader(f3, delimiter = ',')
    lng = []
    lng = [0.000000] * count
    lat = []
    lat = [0.000000] * count
    print("len of lng:",len(lng))
    print("len of lat:",len(lat))
    round = 0
    for row in rows:
        i = 0
        count1 = 0.0000000
        count2 = 0.0000000
        ave1 = 0.0000000
        ave2 = 0.0000000
        geo_temp = list(row)
        geo = []
        geo = [0.000000] * len(geo_temp) 
        for j in geo_temp:
            geo[i] = float(j)
            # print(geo[i]," ")
            i = i + 1
        for k in range(len(geo)):
            if(k % 2 == 0):
                count1 = count1 + geo[k]
            else:
                count2 = count2 + geo[k]
        ave1 = count1 / (i / 2)
        ave2 = count2 / (i / 2)
        print("i=",i,",count1=",count1,",count2=",count2,",ave1=",ave1,",ave2=",ave2,",round=",round,"\n")
        lng[round] = ave1
        lat[round] = ave2
        # print(round," ")
        round = round + 1

# len = 5
# for t in range(5):
#     print(lng[t])
#     print(lat[t])

print("Read the geo file\n")

with open('./data/link_single.csv','w') as fw:
    fw.write('link_id,from_node_id,to_node_id,lng,lat\n')
    for s in range(len(lane_id)):
        # fw.write((str(lane_id[s])+','+str(from_id[s])+','+str(to_id[s])+','+str(lng[s])+','+str(lat[s])+'\n'))
        fw.write((str(lane_id[s])+','))
        fw.write((str(from_id[s])+','))
        fw.write((str(to_id[s])+','))
        fw.write((str(lng[s])+','))
        fw.write((str(lat[s])+'\n'))        

            

# with open('./data/sz.tns','w') as fw:
#     fw.write('3\n')
#     # fw.write((str(len(segments))+' '+str(len(timeoday))+' '+str(len(days))+'\n'))
#     for s in range(len(days)):
#         fw.write((str(segments[s])+' '+str(timeoday[s])+' '+str(days[s])+'\n'))

print("finish")