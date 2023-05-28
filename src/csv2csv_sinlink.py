import pandas as pd
import numpy as np
import csv
import math


# 记录道路的总数

with open('./data/cd_taxi/link_auto.csv','r') as f:
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


with open("./data/cd_taxi/link_geo_temp3.csv", "r") as f1:
    reader1 = f1.readlines()

with open("./data/cd_taxi/link_geo_temp4.csv", "w") as f2:
    for line1 in reader1:
        f2.write(line1.replace(' ',','))

with open("./data/cd_taxi/link_geo_temp4.csv", "r") as f3:
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
        # print("i=",i,",count1=",count1,",count2=",count2,",ave1=",ave1,",ave2=",ave2,",round=",round,"\n")
        lng[round] = ave1
        lat[round] = ave2
        # print(round," ")
        round = round + 1

print("Read the geo file\n")

ii = 0
com_count = 0
for ii in range(count):
    jj = ii + 1
    for jj in range(count):
        if((int(from_id[ii]) == int(to_id[jj])) & (int(to_id[ii]) == int(from_id[jj]))):
            lng[ii] = (lng[ii] + lng[jj]) / 2
            lat[ii] = (lat[ii] + lng[jj]) / 2
            lane_id[jj] = -1
            com_count += 1


print("com_count=",com_count)

with open('./data/cd_taxi/link_single_temp.csv','w') as fw:
    fw.write('link_id,from_node_id,to_node_id,lng,lat\n')
    for s in range(len(lane_id)):
        fw.write((str(int(lane_id[s]))+','+str(int(from_id[s]))+','+str(int(to_id[s]))+','+str(lng[s])+','+str(lat[s])+'\n'))
       
df = pd.read_csv("./data/cd_taxi/link_single_temp.csv")
ff = df[['link_id','from_node_id','to_node_id','lng','lat']]
df.drop_duplicates(inplace=True)
df = df.loc[~(df['link_id'].eq(-1))]

with open('./data/cd_taxi/link_single.csv','w') as fww:
    fww.write('link_id,from_node_id,to_node_id,lng,lat\n')
    for line in df.values:
        fww.write((str(line[0])+','+str(line[1])+','+str(line[2])+','+str(line[3])+','+str(line[4])+'\n'))

print("finish")