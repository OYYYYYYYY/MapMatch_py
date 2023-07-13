import json 
import requests
import csv

# # read node_id from link_single.csv
# with open('./data/cd_taxi/link_single.csv', 'r') as fl:
#     readerl = csv.DictReader(fl)
#     from_id = []
#     to_id = []
#     for rowl in readerl:
#         temp0 = float(rowl['from_node_id'])
#         temp1 = float(rowl['to_node_id'])
#         from_id.append(int(temp0))
#         to_id.append(int(temp1))

# len_id = len(from_id)
# print(len_id)
# # temp_id = []
# # temp_id = [0] * len_id * 2
# # s = 0

# temp_id = []
# for i in from_id:
#     if i not in temp_id:
#         temp_id.append(i)
# for j in to_id:
#     if j not in temp_id:
#         temp_id.append(j)
# # for i in range(len_id):
# #     for j in range(len_id):
# #         if(from_id[i] != to_id[j]):
# #             from_id.extend(to_id[j])
# len_id = len(temp_id)
# print(len_id)
# # print(count)

# # read x and y of node from node_sample.csv
# with open('./data/cd_taxi/node_sample.csv', 'r') as fn:
#     readern = csv.DictReader(fn)
#     x = []
#     y = []
#     for rown in readern:
#         temp0 = float(rown['x_coord'])
#         temp1 = float(rown['y_coord'])
#         x.append(temp0)
#         y.append(temp1)

# len_node = len(x)
# print(len_node)

# id = []
# id = [0] * len_id
# x_ind = []
# x_ind = [0.000000] * len_id
# y_ind = []
# y_ind = [0.000000] * len_id

# for k in range(len_id):
#     id[k] = temp_id[k]
#     x_ind[k] = x[int(id[k])]
#     y_ind[k] = y[int(id[k])]

# print("ready to write")

# with open('./data/cd_taxi/node_list.csv', 'w') as f:
#     f.write('node_id,lng,lat\n')
#     for s in range(len_id):
#         f.write((str(id[s])+','+str(x_ind[s])+','+str(y_ind[s])+'\n'))

with open('./data/cd_taxi/node_list.csv', 'r') as f:
    reader = csv.DictReader(f)
    id = []
    lng = []
    lat = []
    for row in reader:
        temp0 = float(row['node_id'])
        temp1 = float(row['lng'])
        temp2 = float(row['lat'])
        id.append(temp0)
        lng.append(temp1)
        lat.append(temp2)

length = len(id)

coordinate = []
for i in range(length):
    # strlist = "{}{}{}{}{}".format("'", lng[i], ",", lat[i], "'")
    strlist = "{}{}{}".format(lng[i], ",", lat[i])
    coordinate.append(strlist)
    
key = '32817f1d6e4d300e8f9f250ca8e593c1' 
url = 'https://restapi.amap.com/v5/place/around?key={}&location={}&radius={}'
radius = '200'
for j in range(10):    
    location = coordinate[j]
    response = requests.get(url.format(key, location, radius))
    print(response.json())

# with open('./src/111.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     a = []
#     b = []
#     c = []
#     for row in reader:
#         a.append(row['a'])
#         b.append(row['b'])
#         c.append(row['c'])

# len = len(a)

# strlist = "{}{}{}{}{}".format("'", b[0], ",", c[0], "'")
# print(strlist)




# key = '32817f1d6e4d300e8f9f250ca8e593c1'
# location = '104.126087,30.650629'
# radius = '100'
# # city = '北京市'
# # keywords = '餐厅'
# url = 'https://restapi.amap.com/v5/place/around?key={}&location={}&radius={}'
# response = requests.get(url.format(key, location, radius))
# print(response.json())