import pandas as pd
import numpy as np
import csv
import math
import sys

def main(argv):
    # input = argv[1]
    # output = argv[2]

    # df = pd.read_csv(input)
    # # df_sorted = df.sort_values("poi_score")
    # df_sorted = df.sort_values(by='a', ascending = False)
    # df_sorted.to_csv(output)
    for i in range(1,5):
        print(i)
    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))