import pandas as pd
import numpy as np
import csv
import math


# df = pd.read_csv("./data/cd_taxi/link_single.csv")
# df = df[['link_id','from_node_id','to_node_id','lng','lat']]

# with open('./data/cd_taxi/link_single_noid.csv','w') as fww:
#     fww.write('link_id,lng,lat\n')
#     for line in df.values:
#         fww.write((str(line[0])+','+str(line[3])+','+str(line[4])+'\n'))

with open('./data/cd_taxi/link_single.csv', 'r') as f:
    reader = csv.DictReader(f)
    link_id = []
    from_id = []
    to_id = []
    lngs = []
    lats = []
    for row in reader:
        link_id.append(row['link_id'])
        from_id.append(row['from_node_id'])
        to_id.append(row['to_node_id'])
        lngs.append(float(row['lng']))
        lats.append(float(row['lat']))

num = len(link_id)

new_id = []
new_id = [0] * num

for i in range(num):
    new_id[i] = i

with open('./data/cd_taxi/link_single_new.csv', 'w') as fw:
    fw.write('link_id,from_node_id,to_node_id,lng,lat\n')
    for i in range(num):
        fw.write((str(new_id[i])+','+str(from_id[i])+','+str(to_id[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))
with open('./data/cd_taxi/link_single_noid_new.csv', 'w') as fww:
    fww.write('link_id,lng,lat\n')
    for i in range(num):
        fww.write((str(new_id[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))
print("finish")