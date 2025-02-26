import pandas as pd
import numpy as np
import random
import math
import csv
import sys 

def main(argv):
    input = argv[1]
    output = argv[2]
    with open(input , 'r') as f:
        reader = csv.DictReader(f)
        link_id = []
        length = []
        lanes = []
        link_type = []
        for line in reader:
            link_id.append(float(line['link_id']))
            length.append(float(line['length']))
            lanes.append(float(line['lanes']))
            link_type.append(float(line['link_type']))
    
    num = len(link_id)

    rows = []
    rows = [0] * num * num
    cols =[]
    cols = [0] * num * num
    vals = []
    vals = [0.0] * num * num

    count = 0
    count_0 = 0
    for i in range(num):
        for j in range(num):
            # vec1 = np.array([length[i], lanes[i], link_type[i]])
            # vec2 = np.array([length[j], lanes[j], link_type[j]])
            if(i != j):
                # dot_product = np.dot(vec1, vec2)
                # norm_vec1 = np.linalg.norm(vec1)
                # norm_vec2 = np.linalg.norm(vec2)
                dot_product = length[i] * length[j] + lanes[i] * lanes[j] + link_type[i] * link_type[j]
                norm_vec1 = np.sqrt(length[i]**2 + lanes[i]**2 + link_type[i]**2)
                norm_vec2 = np.sqrt(length[j]**2 + lanes[j]**2 + link_type[j]**2)
                rows[count] = i
                cols[count] = j
                vals[count] = dot_product / (norm_vec1 * norm_vec2)
                # print(dot_product)
                # print(norm_vec1)
                # print(norm_vec2)
                # print(vals[count])
                # if(vals[count] == 0):
                #     count_0 = count_0 + 1
                count = count + 1
    print(count)
    with open(output, 'w') as fw:
        fw.write((str(int(num))+' '+str(int(num))+'\n'))
        for k in range(count):
            fw.write((str(int(rows[k]))+' '+str(int(cols[k]))+' '+str(vals[k])+'\n'))

if __name__ == '__main__':
    sys.exit(main(sys.argv))

# with open('./data/adj.mat','w+', encoding='utf-8') as f:
#     f.write('2\n')
#     f.write('\n')
#     for line in df.values:
#         f.write((str(line[3])+' '+str(line[4])+' 1\n'))
