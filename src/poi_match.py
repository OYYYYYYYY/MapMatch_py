import pandas as pd
import numpy as np
import csv
import math
import sys

def main(argv):
    input = argv[1]
    poi_input1 = argv[2]
    poi_input2 = argv[3]
    poi_output = argv[4]
    output = argv[5]
    output1 = argv[6]

    # read road segment information
    with open(input, 'r') as f:
        reader = csv.DictReader(f)
        link_id = []
        # osm_id = []
        from_id = []
        to_id = []
        lngs = []
        lats = []
        for row in reader:
            link_id.append(row['link_id'])
            # osm_id.append(float(row['osm_way_id']))
            from_id.append(row['from_node_id'])
            to_id.append(row['to_node_id'])
            lngs.append(float(row['lng']))
            lats.append(float(row['lat']))

    num_link = len(link_id)

    # read poi information poi_new.csv poi_id,lng,lat
    with open(poi_input1, 'r') as fp:
        readerp = csv.DictReader(fp)
        # poi_osm_id = []
        poi_id = []
        poi_lngs = []
        poi_lats = []
        for rowp in readerp:
            # poi_osm_id.append(float(rowp['osm_way_id']))
            poi_id.append(float(rowp['poi_id']))
            poi_lngs.append(float(rowp['lng']))
            poi_lats.append(float(rowp['lat']))

    num_poi = len(poi_id)

    # read poi information poi_withwayid.csv name,poi_id
    with open(poi_input2, 'r') as fp1:
        readerp1 = csv.DictReader(fp1)
        poi_id1 = []
        poi_name = []
        for rowp1 in readerp1:
            poi_id1.append(float(rowp1['poi_id']))
            poi_name.append(rowp1['name'])

    num_poi1 = len(poi_id1)

    poi_matchnum = 0
    poi_id_new = [0] * num_poi1
    poi_lngs_new = [0.00] * num_poi1
    poi_lats_new = [0.00] * num_poi1
    poi_name_new = ['a'] * num_poi1
    for i in range(num_poi):
        for j in range(num_poi1):
            if(poi_id[i] == poi_id1[j]):
                poi_id_new[poi_matchnum] = poi_id[i]            
                poi_lngs_new[poi_matchnum] = poi_lngs[i]
                poi_lats_new[poi_matchnum] = poi_lats[i]
                poi_name_new[poi_matchnum] = poi_name[j]
                # print(poi_matchnum, end = " " )
                poi_matchnum += 1
    
    if(len(poi_id_new) != poi_matchnum):
        print("match length error")
    
    # output poi information with full name
    with open(poi_output, 'w') as fpw:
        fpw.write('name,poi_id,lng,lat\n')
        for i in range(poi_matchnum):
            fpw.write((str(poi_name_new[i])+','+str(poi_id_new[i])+','+str(poi_lngs_new[i])+','+str(poi_lats_new[i])+'\n'))

    count = 0
    poi_score = []
    poi_score = [0] * num_link
    for i in range(num_link):
        for j in range(poi_matchnum):
            if ((math.fabs(lngs[i] - poi_lngs_new[j]) < 0.001) & (math.fabs(lats[i] - poi_lats_new[j]) < 0.001)):
                count += 1
                poi_score[i] += 1
    print(count)
    # for i in range(num_link):
        # print(poi_score[i], end = " " )
    # count = 0
    # # 根据poi_withwayid.csv对poi进行路段匹配
    # for i in range(num_poi):
    #     for j in range(num_link):
    #         if(poi_osm_id[i] == osm_id[j]):
    #             poi_score[j] += 1
    #             count = count + 1
    # print(count)

    with open(output, 'w') as fww:
        fww.write('link_id,poi_score,from_node_id,to_node_id,lng,lat\n')
        for i in range(num_link):
            fww.write((str(link_id[i])+','+str(poi_score[i])+','+str(from_id[i])+','+str(to_id[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))
    
    df = pd.read_csv(output)
    # df_sorted = df.sort_values("poi_score")
    df_sorted = df.sort_values(by='poi_score', ascending = False)
    df_sorted.to_csv(output1)

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))