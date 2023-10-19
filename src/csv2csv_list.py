import pandas as pd
import numpy as np
import csv
import math
import sys

def main(argv):
    # input tensor file .csv
    input = argv[1]
    output = argv[2]

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

    num = len(link_id)
    with open(output, 'w') as fww:
        fww.write('road,time,days,values\n')
        for i in range(num):
            fww.write((str(link_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))