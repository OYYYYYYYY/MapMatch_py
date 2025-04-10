import pandas as pd
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
        from_id = []
        to_id = []
        for line in reader:
            link_id.append(float(line['link_id']))
            from_id.append(float(line['from_node_id']))
            to_id.append(float(line['to_node_id']))
    
    num = len(link_id)

    rows = []
    rows = [0] * num * num
    col =[]
    col = [0] * num * num
    val = []
    val = [0.0] * num * num

    count = 0
    for i in range(num):
        for j in range(num):
            if(i == j):
                continue
            if((from_id[i] == from_id[j]) | (from_id[i] == to_id[j]) | (to_id[i] == to_id[j]) | (to_id[i] == from_id[j])):
                rows[count] = i
                col[count] = j
                val[count] = 1
                count = count + 1
    print(count)
    with open(output, 'w') as fw:
        fw.write((str(int(num))+' '+str(int(num))+'\n'))
        for k in range(count):
            fw.write((str(int(rows[k]))+' '+str(int(col[k]))+' '+str(int(val[k]))+'\n'))

if __name__ == '__main__':
    sys.exit(main(sys.argv))

# with open('./data/adj.mat','w+', encoding='utf-8') as f:
#     f.write('2\n')
#     f.write('\n')
#     for line in df.values:
#         f.write((str(line[3])+' '+str(line[4])+' 1\n'))
