import pandas as pd
import numpy as np
import csv
import math
import sys

def main(argv):
    # input tensor file .csv
    input = argv[1]
    output = argv[2]
    # output_end = argv[3]
    # num_road = int(argv[3])

    # df = pd.read_csv(input)
    # df_sum = df.groupby(['road','time','days'])['values'].sum()
    # df_sum.to_csv(output)

    # read tensor file
    with open(input, 'r') as f:
        reader = csv.DictReader(f)
        link_id = []
        times = []
        days = []
        values = []
        for row in reader:
            temp0 = float(row['road'])
            if(int(temp0) != 10000):
                temp1 = float(row['time'])
                temp2 = float(row['days'])
                link_id.append(int(temp0))
                times.append(int(temp1))
                days.append(int(temp2))
                values.append(float(row['values']))

    num = len(link_id)
    num_road = 7471
    num_time = 1080
    num_day = 28

    for i in range(num):
        if(times[i] > num_time | link_id[i] > num_road | days[i] > num_day):
            print(link_id[i], times[i], days[i])

    with open(output, 'w') as fww:
        fww.write('road,time,days,values\n')
        for i in range(num):
            fww.write((str(link_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))



    # record the number of lost value in each mode
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(num_road):
        if((i + 1) in link_id):
            count1 = count1
        else:
            count1 = count1 + 1
  
    for i in range(num_time):
        if((i + 1) in times):
            count2 = count2
        else:
            count2 = count2 + 1
    
    for i in range(num_day):
        if((i + 1) in days):
            count3 = count3
            # print(i + 1)
        else:
            count3 = count3 + 1
        
    print(count1)
    print(count2)    
    print(count3)



    # using the lost value array to compress the tensor mode-1
    # new_id = [0] * num
    # r = 2
    # new_id[0] = 1
    # for i in range(1, num):
    #     if(link_id[i] != link_id[i - 1]):
    #         new_id[i] = r
    #         r = r + 1
    #     else:
    #         new_id[i] = new_id[i - 1]

    # with open(output, 'w') as fww:
    #     fww.write('road,time,days,values\n')
    #     for i in range(num):
    #         fww.write((str(new_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))
    
    # new_time = [0] * num
    # r = 2
    # new_time[0] = 1
    # for i in range(1, num):
    #     if(times[i] != times[i - 1]):
    #         new_time[i] = r
    #         r = r + 1
    #     else:
    #         new_time[i] = new_time[i - 1]
    # print(r)

    # with open(output, 'w') as fww:
    #     fww.write('road,time,days,values\n')
    #     for i in range(num):
    #         fww.write((str(link_id[i])+','+str(times[i])+','+str(days[i])+','+str(values[i])+'\n'))
    
    # new_day = [0] * num
    # r = 2
    # new_day[0] = 1
    # for i in range(1, num):
    #     if(days[i] != days[i]):
    #         new_day[i] = r
    #         r = r + 1
    #     else:
    #         new_day[i] = new_day[i - 1]
    
    # with open(output, 'w') as fww:
    #     fww.write('road,time,days,values\n')
    #     for i in range(num):
    #         fww.write((str(link_id[i])+','+str(times[i])+','+str(new_day[i])+','+str(values[i])+'\n'))
        
    
    # # for i in range(num_day):
    #     # print(i)

    # # print(count1)
    # # print(count2)    
    # # print(count3)

    # # with open(output, 'w') as fww:
    # #     fww.write('link_id,poi_score,lng,lat\n')
    # #     for i in range(num_link):
    # #         fww.write((str(link_id[i])+str(poi_score[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))
    

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))