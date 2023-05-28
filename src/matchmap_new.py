import pandas as pd
import numpy as np
import csv
import math
import osm2gmns as og
import datetime


# 读取数据文件
with open('./data/cd_taxi/sample_data_60s/sample_60s_d00.csv', 'rt') as f:
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

# 时间片总数
time_num = 60 * 60 * 24 / 60

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
with open('./data/cd_taxi/link_single.csv','r') as fn:
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

print("Load link data and record the id of links")

# 轨迹点与道路匹配, count_com表示有多少个轨迹点落在道路上, i in total number of gps, j in total number of 
print("len of lngs:", len(lngs), ",lats:", len(lats), ",times:", len(times))
print("len of lngs_lane:", len(lngs_lane), ",lats_lane:", len(lats_lane), ",lane_id:", len(lane_id))
print("len of segments:", len(segments), ",timeoday:", len(timeoday), ",days:", len(days), ",values:", len(values))
count_com = 0
for i in range(len(times)):
    for j in range(len(lane_id)):
        if ((math.fabs(lngs[i] - lngs_lane[j]) < 0.0005) & (math.fabs(lats[i] - lats_lane[j]) < 0.0005)):
            segments[count_com] = int(lane_id[j])
            timeoday[count_com] = int(times[i])
            days[count_com] = int(dates[i])
            values[count_com] = 1
            count_com = count_com + 1
            print(count_com)
            break


print(count_com)
print(num)
print(len(segments), len(timeoday), len(days))

# with open('./data/cd_taxi/sample_data_60s/match_d00.csv', 'w') as fm:
#     fm.write('segment, timeoday, day, value')
#     for m in range(count_com):
#         fw.write((str(segments[m])+','+str(timeoday[m])+','+str(days[m])+','+str(values[m])+'\n'))


#检查是否张量内是否有重复元素
ii = 0
print("count_com = ", count_com)
# com_count 重复元素的数量
com_count = 0
for ii in range(count_com):
    for jj in range(ii + 1, count_com):
        # print(jj)
        if((int(segments[ii]) == int(segments[jj])) & (int(timeoday[ii]) == int(timeoday[jj])) & (int(days[ii]) == int(days[jj]))):
            segments[jj] = -1
            values[ii] += 1
            com_count += 1

print(com_count)

with open('./data/cd_taxi/cd_temp_new.csv','w') as fw:
    # fw.write('3\n')
    # fw.write((str(len(segments))+' '+str(len(timeoday))+' '+str(len(days))+'\n'))
    fw.write('segments,timeofday,days,values\n')
    for s in range(len(days)):
        fw.write((str(segments[s])+','+str(timeoday[s])+','+str(days[s])+','+str(values[s])+'\n'))

print("write to cd_temp_new.csv\n")

# df = pd.read_csv("./data/cd_taxi/cd_temp_new.csv")
# ff = df[['segments','timeofday','days','values']]
# df.drop_duplicates(inplace=True)
# df = df.loc[~(df['segments'].eq(-1))]

# print("ready to write to cd_new.csv\n")

# with open('./data/cd_taxi/cd_new.tns','w') as ft:
#     # ft.write('link_id,from_node_id,to_node_id,lng,lat\n')
#     ft.write('3\n')
#     ft.write((str(len(lane_id))+' '+str(int(time_num))+' '+str(28)+'\n'))
#     for line in df.values:
#         ft.write((str(line[0])+','+str(line[1])+','+str(line[2])+','+str(line[3])+'\n'))

# print("finish")