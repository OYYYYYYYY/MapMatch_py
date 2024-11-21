# clean poi.csv to get simple centroid information
import pandas as pd
import random
import math
import csv

# # get the poi_id and store in list
# with open('./data/cd_taxi/poi.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     poi_id = []
#     for line in reader:
#         poi_id.append(int(line['poi_id']))

#     num = len(poi_id)

df = pd.read_csv("/data/oydata/MapMatch_py/data/week_sz_taxi/poi.csv")

df=df[['name','poi_id','osm_way_id','osm_relation_id','building','amenity','leisure','way','geometry','centroid','area','area_ft2']]

# get centroid information store in file 
with open('./data/cd_taxi/poi_temp.csv', 'w') as fs:
    for line in df.values:
        fs.write((str(line[1])+','+str(line[9])+'\n'))

# clean string POINT (
with open('./data/cd_taxi/poi_temp.csv', 'r') as fr:
    linesr = fr.readlines()
with open('./data/cd_taxi/poi_temp1.csv', 'w') as fw:
    for liner in linesr:
        fw.write(liner.replace('POINT (', ''))

# clean string )
with open('./data/cd_taxi/poi_temp1.csv', 'r') as fr1:
    lines1 = fr1.readlines()
with open('./data/cd_taxi/poi_temp2.csv', 'w') as fw1:
    for line1 in lines1:
        fw1.write(line1.replace(')',''))

# clean string blank
with open('./data/cd_taxi/poi_temp2.csv', 'r') as fr2:
    lines2 = fr2.readlines()
with open('./data/cd_taxi/poi_new.csv', 'w') as fw2:
    fw2.write('poi_id,lng,lat\n')
    for line2 in lines2:
        fw2.write(line2.replace(' ',','))

df1 = pd.read_csv("./data/cd_taxi/poi_temp3.csv")

df1 = df1[['poi_id', 'centroid']]

with open ('./data/cd_taxi/poi_new.csv', 'w') as fn:
    fn.write('poi_id,lng,lat\n')
    for linen in df1.values:
        fn.write((str(linen[0])+','+str(linen[1])+','+str(linen[2])+'\n'))

