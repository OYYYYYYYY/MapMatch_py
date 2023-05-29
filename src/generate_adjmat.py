import pandas as pd
import random
import math
import csv

with open('./data/cd_taxi/link_single_new.csv', 'r') as f:
    reader = csv.DictReader(f)
    link_id = []
    from_id = []
    to_id = []
    for line in reader:
        link_id.append(int(row['link_id']))
        from_id.append(float(row['from_node_id']))
        form_id.append(float(row['to_node_id']))
    
    num = len(link_id)

    row = []
    row = [0] * num * num
    col =[]
    col = [0] * num * num
    val = []
    val = [0] * num * num

    count = 0
    for i in range(num):
        for j in range(num):
            if((from_id[i] == from_id[j]) | (from_id[i] == to_id[j]) | (from_id[j] == to_id[i]) | (from_id[j] == from_id[j])):
                row[count] = i
                col[count] = j
                val[count] = 1
                count = count + 1
    print(count)
with open('./data/cd_taxi/adj_mat.tns', 'w') as fw:
    fw.write('2\n')
    fw.write((str(int(num))+','+str(int(num))+'\n'))
    for k in range(count):
        fw.write((str(int(row[k]))+','+str(int(col[k]))+','+str(int(val[k]))+'\n'))

# with open('./data/adj.mat','w+', encoding='utf-8') as f:
#     f.write('2\n')
#     f.write('\n')
#     for line in df.values:
#         f.write((str(line[3])+' '+str(line[4])+' 1\n'))
