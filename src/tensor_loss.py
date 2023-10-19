import pandas as pd
import numpy as np
import csv
import math
import sys
import random

def main(argv):
    # randomlist = random.sample(range(1, 10), 3)
    # print(randomlist)
    # array = [0] * 5
    # for row in range(5):
    #     array[row] = row
    # for row in range(5):
    #     if(array[row] in randomlist):
    #         print(row)

    # input tensor file .csv
    input = argv[1]
    output = argv[2]
    mode = int(argv[3])
    num_road = 5180
    num_time = 1080
    num_day = 25

    if(mode == 4):
        adj_input = argv[4]

    selected_data = []

    # road mode poi loss 
    if(mode == 1):
        randomlist = random.sample(range(1, int(num_road + 1)), 800)
        randomlist_new = [0] * len(randomlist) * 3 
        print("finish new array")
        for i in range(len(randomlist)):
            if(randomlist[i] - 1 not in randomlist):
                randomlist_new.append(randomlist[i] - 1)
            if(randomlist[i] not in randomlist):
                randomlist_new.append(randomlist[i])
            if(randomlist[i] + 1 not in randomlist):
                randomlist_new.append(randomlist[i] + 1)
        print("finish new array append")
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
                if(link_id[i] in randomlist):
                    block = 1
                else:
                    fww.write((str(link_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))
    # if(mode == 1):
    #     randomlist = random.sample(range(1, int(num_road + 1)), 800)
    #     randomlist_new = [0] * len(randomlist) * 3 
    #     print("finish new array")
    #     for i in range(len(randomlist)):
    #         if(randomlist[i] - 1 not in randomlist):
    #             randomlist_new.append(randomlist[i] - 1)
    #         if(randomlist[i] not in randomlist):
    #             randomlist_new.append(randomlist[i])
    #         if(randomlist[i] + 1 not in randomlist):
    #             randomlist_new.append(randomlist[i] + 1)
    #     print("finish new array append")
    #     with open(input, 'r') as f:
    #         reader = csv.reader(f)
    #         for row in reader:
    #             if(row[0] in randomlist_new):
    #                 blank = 1
    #             else:
    #                 selected_data.append(row)
    #     print("read")
    #     with open(output, 'w') as file:
    #         writer = csv.writer(file)
    #         writer.writerows(selected_data)

    # time mode loss
    if(mode == 2):
        randomlist = random.sample(range(1, int(num_time + 1)), int(num_time / 3))
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
    # if(mode == 2):
    #     randomlist = random.sample(range(1, int(num_time + 1)), int(num_time / 3))
    #     with open(input, 'r') as f:
    #         reader = csv.reader(f)
    #         for row in reader:
    #             if(row[1] in randomlist):
    #                 blank = 1
    #             else:
    #                 selected_data.append(row)
    #     with open(output, 'w') as file:
    #         writer = csv.writer(file)
    #         writer.writerows(selected_data)

    # day mode loss 
    if(mode == 3):
        randomlist = random.sample(range(1, int(num_day + 1)), int(num_day / 4))
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
    # if(mode == 3):
    #     randomlist = random.sample(range(1, int(num_day + 1)), int(num_day / 3))
    #     with open(input, 'r') as f:
    #         reader = csv.reader(f)
    #         for row in reader:
    #             if(row[2]in randomlist):
    #                 blank = 1
    #             else:
    #                 selected_data.append(row)
    #     with open(output, 'w') as file:
    #         writer = csv.writer(file)
    #         writer.writerows(selected_data)

    # space road loss
    if(mode == 4):
        with open(adj_input, 'r') as fa:
            readera = csv.DictReader(fa)
            rowinds = []
            colinds = []
            values = []
            for rowa in readera:
                temp0 = float(rowa['row'])
                temp1 = float(rowa['col'])
                temp2 = float(rowa['value'])
                rowinds.append(int(temp0))
                colinds.append(int(temp1))
                values.append(temp2)
        print("read adj_mat")
        randomlist = random.sample(range(1, int(num_road + 1)), 300)
        randomlist_new = []
        print("create new array")
        for i in range(len(rowinds)):
            if((rowinds[i]) in randomlist):
                if(rowinds[i] in randomlist_new):
                    number = 1
                else:
                    randomlist_new.append(rowinds[i])
                if(colinds[i] in randomlist_new):
                    number = 1
                else:
                    randomlist_new.append(colinds[i])
        # print("len of randomlist_new is " + len(randomlist_new))
        print(len(randomlist_new))
        print("finish new array append")
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
                if(link_id[i] in randomlist):
                    block = 1
                else:
                    fww.write((str(link_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))
        # with open(input, 'r') as f:
        #     reader = csv.reader(f)
        #     for row in reader:
        #         if(row[0] in randomlist_new):
        #             blank = 1
        #         else:
        #             selected_data.append(row)
        # with open(output, 'w') as file:
        #     writer = csv.writer(file)
        #     writer.writerows(selected_data)
    num_nnz = 12360224
    # random little loss
    if(mode == 5):
        # randomlist = random.sample(range(1, int(num_nnz + 1)), int(num_nnz / 5))
        # df = pd.read_csv(input)
        # df.columns = ['road','time','days','values']
        # # for i in range(len(randomlist)):
        # df.drop(randomlist)

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
        # fww.write('3\n')
        # fww.write('5180 1080 25\n')
            fww.write('road,time,days,values\n')
            for i in range(num):
                if(i % 4 == 0):
                    block = 1
                else:
                    fww.write((str(link_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))

        

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))