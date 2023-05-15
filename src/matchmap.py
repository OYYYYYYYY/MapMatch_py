import pandas as pd
import numpy as np
import csv
import math
import osm2gmns as og
import datetime


# 读取数据文件
with open('./data/gps_sample.csv', 'rt') as f:
    reader = csv.DictReader(f)
    lngs = []
    lats = []
    times = []
    for row in reader :
        # 将经纬度字符串转换为数值
        temp0 = float(row['lng'])
        temp1 = float(row['lat'])

        lngs.append(temp0)
        lats.append(temp1)

        # lngs.append(float(row['lng']))
        # lats.append(float(row['lat']))
        times.append(int(row['time']))
count_gps = len(times)
print("Load gps data\n")

time_num = 60 * 60 * 24 / 30

# 创建存储张量的三个维度的数组
segments = []
segments = [0] * count_gps
timeoday = []
timeoday = [0] * count_gps 
days = []
days = [0] * count_gps
values = []
values = [0] * count_gps

# 获取道路经纬度信息
with open('./data/link_single.csv','r') as fn:
    # readern = csv.reader(fn, delimiter = ',')
    readern = csv.DictReader(fn)
    lane_id = []
    lngs_lane = []
    lats_lane = []
    for rown in readern:
        lane_id.append(float(rown['link_id']))
        lngs_lane.append(float(rown['lng']))
        lats_lane.append(float(rown['lat']))
# 获取道路总数
count = len(lane_id)

# 道路总数
print("The number of links:", count)


print("\nLoad link data and record the id of links\n")

# 获取GPS数据集中每一个轨迹点与路段进行匹配 / 遍历每一条路段
# for i in range(len(times)):
#     # 遍历路网link_geo_p文件中每一行(每一行都为一条路段)
#     flag = 0
#     for l in range(count):
#         with open("./data/link_geo_lane_temp.csv", "w") as flw:
#             writerlw = csv.writer(flw)
#             row_lane = rowslr[l]
#             writerlw.writerow(row_lane)



#         # 将一行数据扩展成多行,并转换的二维数据
#         with open('./data/link_geo_lane.csv', 'r') as infile, open('./data/link_geo_lane_temp.csv', 'w') as outfile:
#             stripped = (line.strip() for line in infile)
#             lines = ([sent] for para in (line.split(",") for line in stripped if line) for sent in para)
#             writer = csv.writer(outfile)
#             writer.writerows(lines)

#         with open('./data/link_geo_lane_temp.csv','r') as fr3:
#             lines3 = fr3.readlines()
#         with open('./data/link_lane_new.csv','w') as fw3:
#             fw3.write('lon,lat\n')
#             for line3 in lines3:
#                 fw3.write(line3.replace(' ',','))
                    
#         # 此时每一行表示该路段的一个坐标点(经度 纬度)
#         with open('./data/link_lane_new.csv', 'r') as fla:
#             reader1 = csv.DictReader(fla)
#             lane_lons = []
#             lane_lats = []
#             for row1 in reader1 :
#                 temp3 = float(row1['lon'])
#                 temp4 = float(row1['lat'])
#                 lane_lons.append(temp3)
#                 lane_lats.append(temp4)

#         for j in range(len(lane_lons)):
#             if((abs(lons[i] - lane_lons[i]) < 0.000045) and (lats[i] - lane_lats[i]) < 0.000045):
#                 segments[i] = lane_id[l]
#                 timeoday[i] = times[i]
#                 days[i] = 1
#                 flag = 1
#                 print("road:",l,"\n")
#                 break
#         if(flag == 1):
#             print(lane_id[l])
#             print("\n")
#             break

# 轨迹点与道路匹配, count_com表示有多少个轨迹点落在道路上, i in total number of gps, j in total number of 
print("len of lngs:", len(lngs), ",lats:", len(lats), ",times:", len(times))
print("len of lngs_lane:", len(lngs_lane), ",lats_lane:", len(lats_lane), ",lane_id:", len(lane_id))
print("len of segments:", len(segments), ",timeoday:", len(timeoday), ",days:", len(days), ",values:", len(values))
count_com = 0
num = 0
for i in range(len(times)):
    for j in range(len(lane_id)):
        if ((math.fabs(lngs[i] - lngs_lane[j]) < 0.001) | (math.fabs(lats[i] - lats_lane[j]) < 0.001)):
            num += 1
            segments[count_com] = int(lane_id[j])
            timeoday[count_com] = int(times[i])
            days[count_com] = 0
            values[count_com] = 1
            count_com = count_com + 1
            # print(count_com)
            break


print(count_com)
print(num)
print(len(segments), len(timeoday), len(days))

#检查是否张量内是否有重复元素
ii = 0
print("count_com = ", count_com)
com_count = 0
for ii in range(count_com):
    for jj in range(ii + 1, count_com):
        # print(jj)
        if((int(segments[ii]) == int(segments[jj])) & (int(timeoday[ii]) == int(timeoday[jj])) & (int(days[ii]) == int(days[jj]))):
            segments[jj] = -1
            values[ii] += 1
            com_count += 1
            

with open('./data/sz_temp.csv','w') as fw:
    # fw.write('3\n')
    # fw.write((str(len(segments))+' '+str(len(timeoday))+' '+str(len(days))+'\n'))
    fw.write('segments,timeofday,days,values\n')
    for s in range(len(days)):
        fw.write((str(segments[s])+','+str(timeoday[s])+','+str(days[s])+','+str(values[s])+'\n'))

df = pd.read_csv("./data/sz_temp.csv")
ff = df[['segments','timeofday','days','values']]
df.drop_duplicates(inplace=True)
df = df.loc[~(df['segments'].eq(-1))]
    
with open('./data/sz.tns','w') as ft:
    # ft.write('link_id,from_node_id,to_node_id,lng,lat\n')
    ft.write('3\n')
    ft.write((str(len(lane_id))+' '+str(time_num)+' '+str(1)+'\n'))
    for line in df.values:
        ft.write((str(line[0])+','+str(line[1])+','+str(line[2])+','+str(line[3])+'\n'))

print("finish")