import pandas as pd
import numpy as np
import csv
import math
import sys

def main(argv):
    # input tensor file .csv
    input = argv[1]
    input_link = argv[2]
    output = argv[3]
    lost_num = int(argv[4])

    # read tensor file
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

    with open(input_link, 'r') as fl:
        readerl = csv.DictReader(fl)
        lane_id = []
        from_id = []
        to_id = []
        lng = []
        lat = []
        for rowl in readerl:
            temp = float(rowl['link_id'])
            lane_id.append(int(temp0))
            from_id.append(float(rowl['from_node_id']))
            to_id.append(float(rowl['to_node_id']))
            lng.append(rowl['lng'])
            lat.append(rowl['lat'])
    

    num = len(link_id)
    num_road = 7471
    num_exit = num_road - lost_num

    new_id = [0] * num_exit
    new_from = [0.0] * num_exit
    new_to = [0.0] * num_exit
    new_lng = [0.0] * num_exit
    new_lat = [0.0] * num_exit
    count = 0
    for i in range(num_road):
        if((i + 1) in link_id):
            new_id[count] = count + 1
            new_from[count] = from_id[count]
            new_to[count] = to_id[count]
            new_lng[count] = lng[count]
            new_lat[count] = lat[count]
            count = count + 1

    with open(output, 'w') as fww:
        fww.write('link_id,from_node_id,to_node_id,lng,lat\n')
        for i in range(num_exit):
            fww.write((str(new_id[i])+','+str(new_from[i])+','+str(new_to[i])+','+str(new_lng[i])+','+str(new_lat[i])+'\n'))


    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))