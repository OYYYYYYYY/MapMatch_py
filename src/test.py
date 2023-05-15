import pandas as pd
import random
import math
import csv

# # x = '1,2,3'
# # x1 = " ".join(str(i) for i in x)
# # print(x1)

# # with open('./src/111.csv', 'r') as f:
# #     rows = csv.reader(f, delimiter=',')
# #     output = []
# #     x = {}
# #     i = 0
# #     for row in rows :
# #         output = list(row)
# #         for each in output:
# #             x[i] = int(each)
# #             print(x[i])
# #             print("\n")
# #             i = i + 1
# row_num = 0
# for index, line in enumerate(open("./src/111.csv",'r')): 
#     row_num += 1
# print(row_num)

# with open("./src/111.csv", "r") as f3:
#     rows = csv.reader(f3, delimiter = ',')
#     lng = []
#     lng = [0] * row_num
#     # s = 1
#     # for s in range(4):
#     #     lng[s] = 0
#     print(lng)
#     round = 0
#     for row in rows:
#         geo_temp = []
#         # print(row)
#         i = 0
#         count = 0
#         ave = 0
#         geo_temp = list(row)
#         # print(len(geo_temp))
#         geo = {}
#         for j in geo_temp:
#             geo[i] = float(j)
#             i = i + 1
#         for k in range(len(geo)):
#             # print("count=",count)
#             count = count + geo[k]
#         # print("count=",count)   
#         ave = count / i
#         lng[round] = ave
#         print("round=",round)
#         print(lng[round])
#         round = round + 1
#         # lat[i] = ave2
#         # print(round," ")
#         # round = round + 1
#     # for t in range(len(lng)):
#         # print(lng[t])
# # print((len(lng)))
# print(lng)
# # t = 0
# # for t in range(len(lng)):
# #     print(lng[t])
for i in range(5):
    for j in range(i, 5):
        print(j)