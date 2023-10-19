import pandas as pd
import numpy as np
import csv
import math
import sys
import scipy.io as sio

def main(argv):
    # input tensor file .csv
    input = argv[1]
    # output tensor file .csv
    output = argv[2]

    data = pd.read_csv(input)
    print(data.shape)
    data_dict = data.to_dict()
    sio.savemat(output, data_dict)
    # X = data.drop(['class'], axis = 1)
    # X = X.values
    # Y = data.drop(['class'])
    # Y = Y.values
    # sio.savemat(output, {'X' : X, 'Y': Y})
    # dataprint = sio.io.loadmat(output)
    # print(dataprint)
    # np.save(output, data)

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))