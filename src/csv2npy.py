import pandas as pd
import numpy as np
import csv
import math
import sys

def main(argv):
    # input tensor file .csv
    input = argv[1]
    # output tensor file .csv
    output = argv[2]

    data = pd.read_csv(input)
    print(data.shape)
    np.save(output, data)
    # data = np.load(input)
    # print(data)
    # data1 = data.reshape(-1, 3, 6)
    # print(data1)
    # print(data1.shape)
    

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))