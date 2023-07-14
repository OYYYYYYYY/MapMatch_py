import pandas as pd
import numpy as np
import csv
import math
import sys

def main(argv):
    input = argv[1]
    poi_input = argv[2]
    output = argv[3]

    with open(input, 'r') as f:
        reader = csv.DictReader(f)
        link_id = []
        osm_id = []
        from_id = []
        to_id = []
        lngs = []
        lats = []
        for row in reader:
            link_id.append(row['link_id'])
            osm_id.append(float(row['osm_way_id']))
            from_id.append(row['from_node_id'])
            to_id.append(row['to_node_id'])
            lngs.append(float(row['lng']))
            lats.append(float(row['lat']))

    num_link = len(link_id)

    with open(poi_input, 'r') as fp:
        readerp = csv.DictReader(fp)
        poi_osm_id = []
        for rowp in readerp:
            poi_osm_id.append(float(row['osm_way_id']))

    num_poi = len(poi_osm_id)

    new_id = []
    new_id = [0] * num

    # 根据poi_withwayid.csv对poi进行路段匹配
    for i in range(num_poi):
        for i in range(num_link):
            if

    # for i in range(num):
        # new_id[i] = i

    with open('./data/cd_taxi/link_single_new.csv', 'w') as fw:
        fw.write('link_id,from_node_id,to_node_id,lng,lat\n')
        for i in range(num):
            fw.write((str(new_id[i])+','+str(from_id[i])+','+str(to_id[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))
    with open(output, 'w') as fww:
        fww.write('link_id,lng,lat\n')
        for i in range(num):
            fww.write((str(new_id[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))
    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))