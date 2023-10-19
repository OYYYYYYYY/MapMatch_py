import pandas as pd
import numpy as np
import csv
import math
import sys
import random

def main(argv):
   
    # input tensor file .csv
    input = argv[1]
    output_temp = argv[2]
    # output = argv[3]
    num_road = 5180
    num_time = 1080
    num_day = 25

    # random little loss
    with open(input, 'r') as f:
        reader = csv.DictReader(f)
        link_id = []
        times = []
        days = []
        values = []
        for row in reader:
            temp0 = float(row['road'])
            temp1 = float(row['time'])
            temp2 = float(row['days'])
            link_id.append(int(temp0))
            times.append(int(temp1))
            days.append(int(temp2))
            values.append(float(row['values']))

    num = len(link_id)
    full_num = num_road * num_time * num_day 
    new_i = [0] * full_num
    new_j = [0] * full_num
    new_k = [0] * full_num
    new_value = [0.0] * full_num

    for i in range(num_road):
        for j in range(num_time):
            for k in range(num_day):
                ind = i * num_time * num_day + j * num_day + k
                new_i[ind] = i + 1
                new_j[ind] = j + 1
                new_k[ind] = k + 1
                new_value[ind] = 0.0
    
    for i in range(num):
        inds = (link_id[i] - 1) * num_time * num_day + (times[i] - 1) * num_day + days[i] - 1
        new_i[inds] = link_id[i]
        new_j[inds] = times[i]
        new_k[inds] = days[i]
        new_value[inds] = values[i]

    with open(output_temp, 'w') as fw:
        fw.write('road,time,days,values\n')
        for i in range(full_num):
            fw.write((str(new_i[i])+','+str(new_j[i])+','+str(new_k[i])+','+str(new_value[i])+'\n'))

    # with open(output_temp, 'w') as fww:
    #     fww.write('road,time,days,values\n')
    #     for i in range(num):
    #         fww.write((str(link_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))
    #     for i in range(num_road):
    #         for j in range(num_time):
    #             for k in range(num_day):
    #                 fww.write((str(i + 1)+','+str(j + 1)+','+str(k + 1)+','+str(0)+'\n'))

    # df = pd.read_csv(output_temp)
    # df_sum = df.groupby(['road','time','days'])['values'].sum()
    # df_sum.to_csv(output)

        

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))