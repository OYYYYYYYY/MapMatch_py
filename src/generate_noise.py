import pandas as pd
import numpy as np
import csv
import math
import sys
import random

def main(argv):

    # input tensor file .csv
    input = argv[1]
    output = argv[2]
    mode = int(argv[3])
    # chengdu dataset 7471*288*28, number of entris is 13092310, time interval is 5min.
    num_road = 7471
    num_time = 288
    num_day = 28
    
    corrupted_rate = float(argv[4])
    num_entry = 13092310
    num_corrupted = int(num_entry * corrupted_rate)
    randomlist = random.sample(range(1, int(num_entry + 1)), num_corrupted)

    selected_data = []

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

    # road mode loss
    if(mode == 1):
        road_rate = int(num_road * (1 - rate))
        print("number of road is ", road_rate)
        randomlist = random.sample(range(1, int(num_road + 1)), road_rate)
        print("finish new array")
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
        with open(output, 'w') as fww:
            fww.write('road,time,days,values\n')
            for i in range(num):
                if(times[i] in randomlist):
                    block = 1
                else:
                    fww.write((str(link_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))
    
    # time mode loss
    if(mode == 2):
        time_rate = int(num_time * (1 - rate))
        print("number of time is ", time_rate)
        randomlist = random.sample(range(1, int(num_time + 1)), time_rate)
        print("finish new array")
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
        with open(output, 'w') as fww:
            fww.write('road,time,days,values\n')
            for i in range(num):
                if(times[i] in randomlist):
                    block = 1
                else:
                    fww.write((str(link_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))
    if(mode == 3):
        day_rate = int(num_day * (1 - rate))
        print("number of day is ", day_rate)
        randomlist = random.sample(range(1, int(num_day + 1)), day_rate)
        print("finish new array")
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
        with open(output, 'w') as fww:
            fww.write('road,time,days,values\n')
            for i in range(num):
                if(days[i] in randomlist):
                    block = 1
                else:
                    fww.write((str(link_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))
    num_nnz = 30447
    # random little loss
    if(mode == 5):
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
        
        index = [0] * num_nnz
        for i in range(num_nnz):
            index[i] = i

        num_to_remove = int(num_nnz * rate)
        data_to_remove = random.sample(index, num_to_remove)
        new_index = [x for x in index if x not in data_to_remove]


        with open(output, 'w') as fww:
        # fww.write('3\n')
        # fww.write('5180 1080 25\n')
            fww.write('road,time,days,values\n')
            for i in range(num):
                # if(i % 4 == 0):
                if(i in new_index):
                    # block = 1
                # else:
                    fww.write((str(link_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))

        

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))