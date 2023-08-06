import pandas as pd
import numpy as np
import csv
import math
import sys

def main(argv):
    # input tensor file .csv
    input = argv[1]
    # output_m1_sort = argv[2]
    # output_m1_clean = argv[3]
    # output_m2_sort = argv[4]
    # output_m2_clean = argv[5]
    # output_m3_sort = argv[6]
    # output = argv[2]

    # # resort according to mode 1
    # df = pd.read_csv(input)
    # df_sorted = df.sort_values(by='road', ascending = True)
    # df_sorted.to_csv(output)

    # # resort according to mode 2
    # df = pd.read_csv(input)
    # df_sorted = df.sort_values(by='time', ascending = True)
    # df_sorted.to_csv(output)

    # # resort according to mode 1
    # df = pd.read_csv(input)
    # df_sorted = df.sort_values(by='days', ascending = True)
    # df_sorted.to_csv(output)

    # read tensor file
    with open(input, 'r') as f:
        reader = csv.DictReader(f)
        # link_id = []
        times = []
        # days = []
        # values = []
        for row in reader:
            # temp0 = float(row['road'])
            temp1 = float(row['time'])
            # temp2 = float(row['day'])
            # link_id.append(int(temp0))
            times.append(int(temp1))
            # days.append(int(temp2))
            # values.append(float(row['values']))

    num = len(times)
    num_road = 7471
    num_time = 1440
    num_day = 28
    count = 0
    for i in range(times):
        if(times[i] == 0):
            count += 1
    print(count)
    # record the number of lost value in each mode
    # count1 = 0
    # count2 = 0
    # count3 = 0
    # # for i in range(num_road):
    # #     if((i + 1) in link_id):
    # #         count1 = count1
    # #     else:
    # #         count1 = count1 + 1
  
    # # for i in range(num_time):
    # #     if((i + 1) in times):
    # #         count2 = count2
    # #     else:
    # #         count2 = count2 + 1
    
    # for i in range(num_day):
    #     if((i + 1) in days):
    #         count3 = count3
    #         print(i + 1)
    #     else:
    #         count3 = count3 + 1
        
    # # print(count1)
    # # print(count2)    
    # print(count3)


    

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))