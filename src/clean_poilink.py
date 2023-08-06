import pandas as pd
import numpy as np
import csv
import math
import sys

def main(argv):
    input = argv[1]
    output = argv[2]

    with open(input, 'r') as f:
        reader = csv.DictReader(f)
        link_id = []
        from_id = []
        to_id = []
        lngs = []
        lats = []
        for row in reader:
            temp0 = float(row['link_id'])
            link_id.append(int(temp0))
            # osm_id.append(float(row['osm_way_id']))
            from_id.append(row['from_node_id'])
            to_id.append(row['to_node_id'])
            lngs.append(float(row['lng']))
            lats.append(float(row['lat']))

    num_link = len(link_id)

    # with open(output, 'w') as fw:
    #     fw.write('link_id,from_node_id,to_node_id,lng,lat\n')
    #     for i in range(num_link):
    #         fw.write((str(link_id[i])+','+str(from_id[i])+','+str(to_id[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))
    with open(output, 'w') as fw:
        fw.write('link_id,lng,lat\n')
        for i in range(num_link):
            fw.write((str(link_id[i])+','+str(lngs[i])+','+str(lats[i])+'\n'))

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))