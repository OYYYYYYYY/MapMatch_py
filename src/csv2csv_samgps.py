import pandas as pd
import numpy as np
import csv
import math
import sys


def main(argv):
    count = 0
    min = 18 * 3600 + 60 * 60
    h_min = 24
    m_min = 61
    s_min = 61
    # 读取数据文件
    input = argv[1]
    output = argv[2]
    with open(input, 'rt') as f:
        reader = csv.DictReader(f)
        lngs = []
        lats = []
        times = []
        days = []
        for row in reader :
        # 将经纬度字符串转换为数值
            temp0 = float(row['lng'])
            temp1 = float(row['lat'])
        # 将时间字符串转换为数值
            h, m, s = row['time'].strip().split(':')
            temp2 = (int(h) - 6) * 3600 + int(m) * 60 + int(s)
            temp3 = int(row['day'])
            if(int(s) % 60 == 0):
                lngs.append(temp0)
                lats.append(temp1)
                times.append(temp2 / 60)
                days.append(temp3)
            elif(row['time'] == '23:59:59'):
                lngs.append(temp0)
                lats.append(temp1)
                times.append(temp2 / 60 + 1)
                days.append(temp3)
                count = count + 1
    print(count)

    print("read data file")
    with open(output,'w') as fw:
        fw.write('lng,lat,time,day\n')
        for s in range(len(lngs)):
            fw.write((str(lngs[s])+','+str(lats[s])+','+str(times[s])+','+str(days[s])+'\n'))

if __name__ == '__main__':
    sys.exit(main(sys.argv))