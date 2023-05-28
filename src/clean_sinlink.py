import pandas as pd
import numpy as np
import csv
import math


df = pd.read_csv("./data/cd_taxi/link_single.csv")
ff = df[['link_id','from_node_id','to_node_id','lng','lat']]

with open('./data/cd_taxi/link_single_noid.csv','w') as fww:
    fww.write('link_id,lng,lat\n')
    for line in df.values:
        fww.write((str(line[0])+','+str(line[3])+','+str(line[4])+'\n'))

print("finish")