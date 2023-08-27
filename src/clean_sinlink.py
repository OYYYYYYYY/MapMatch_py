import pandas as pd
import numpy as np
import csv
import math
import sys

def main(argv):
    input = argv[1]
    # poi_input = argv[2]
    output = argv[2]
    # output1 = argv[4]

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

    # with open(poi_input, 'r') as fp:
    #     readerp = csv.DictReader(fp)
    #     poi_osm_id = []
    #     for rowp in readerp:
    #         poi_osm_id.append(float(rowp['osm_way_id']))

    # num_poi = len(poi_osm_id)

    # poi_score = []
    # poi_score = [0] * num_link

    # count = 0
    # # 根据poi_withwayid.csv对poi进行路段匹配
    # for i in range(num_poi):
    #     for j in range(num_link):
    #         if(poi_osm_id[i] == osm_id[j]):
    #             poi_score[j] += 1
    #             count = count + 1
    # print(count)

    # with open('./data/cd_taxi/link_single_new.csv', 'w') as fw:
    #     fw.write('link_id,from_node_id,to_node_id,lng,lat\n')
    #     for i in range(num_link):
    #         fw.write((str(link_id[i])+','+str(from_id[i])+','+str(to_id[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))
    with open(output, 'w') as fww:
        fww.write('link_id,lng,lat\n')
        for i in range(num_link):
            fww.write((str(link_id[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))
    
    # df = pd.read_csv(output)
    # df_sorted = df.sort_values("poi_score")
    # df_sorted.to_csv(output1)

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))