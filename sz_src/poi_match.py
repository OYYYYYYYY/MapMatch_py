import pandas as pd
import numpy as np
import csv
import math
import sys

def main(argv):
    input = argv[1]
    poi_input1 = argv[2]
    output = argv[3]

    # read road segment information
    with open(input, 'r') as f:
        reader = csv.DictReader(f)
        link_id = []
        time = []
        days =[]
        values = []
        from_id = []
        to_id = []
        lngs = []
        lats = []
        for row in reader:
            link_id.append(row['road'])
            # osm_id.append(float(row['osm_way_id']))
            from_id.append(row['from_id'])
            to_id.append(row['to_id'])
            lngs.append(float(row['lng']))
            lats.append(float(row['lat']))
            # time.append(row['time'])
            # days.append(row['days'])
            # values.append(row['values'])

    num_link = len(link_id)

    # read poi information poi_new.csv poi_id,lng,lat
    with open(poi_input1, 'r') as fp:
        readerp = csv.DictReader(fp)
        poi_lngs = []
        poi_lats = []
        for rowp in readerp:
            poi_lngs.append(float(rowp['lng']))
            poi_lats.append(float(rowp['lat']))

    num_poi = len(poi_lngs)


    count = 0
    poi_score = []
    poi_score = [0] * num_link
    for i in range(num_poi):
        for j in range(num_link):
            if ((math.fabs(lngs[j] - poi_lngs[i]) < 0.001) | (math.fabs(lats[j] - poi_lats[i]) < 0.001)):
                count += 1
                poi_score[j] += 1
    print(count)

    with open(output, 'w') as fww:
        fww.write('road,poi_score,from_id,to_id,lng,lat\n')
        for i in range(num_link):
            # fww.write((str(link_id[i])+','+str(poi_score[i])+','+str(time[i])+','+str(days[i])+','+str(values[i])+','+str(from_id[i])+','+str(to_id[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))
            fww.write((str(link_id[i])+','+str(poi_score[i])+','+str(from_id[i])+','+str(to_id[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))
    
    import pandas as pd

    # 读取CSV文件
    df = pd.read_csv(output)

    # 按照 poi_score 列的值从大到小排序
    df = df.sort_values(by='poi_score', ascending=False).reset_index(drop=True)

    # 重新编号 road 列
    new_road_index = 0
    prev_road_value = None
    new_road_values = []

    for index, row in df.iterrows():
        if row['road'] == prev_road_value:
            new_road_values.append(new_road_index)
        else:
            new_road_index += 1
            new_road_values.append(new_road_index)
            prev_road_value = row['road']

    df['new_road'] = new_road_values

    # 保存新的CSV文件
    df.to_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_poi.csv', index=False)

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))