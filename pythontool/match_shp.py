import transbigdata as tbd
import pandas as pd
import matplotlib.pyplot as plt
import osmnx as ox
import geopandas as gpd
import csv
import json

# 地图匹配包
from leuvenmapmatching.matcher.distance import DistanceMatcher
from leuvenmapmatching.map.inmem import InMemMap
from leuvenmapmatching import visualization as mmviz

#读取数据文件
# with open('./chengdu/cdc_tony.csv', 'rt') as f:
#     reader = csv.DictReader(f)
#     lons = []
#     lats = []
#     for row in reader :
#         lons.append(row['lon'])
#         lats.append(row['lat'])
# print(lons[:5])
# print(lats[:5])
data = pd.read_csv('./chengdu/cdc_tony.csv',header = None)
data.columns = ['hour', 'lon', 'lat']

#读取研究范围区域信息
cdc = gpd.read_file(r'chengdu/510100_full_cdc/510100_full_cdc.shp')
cdc.plot()
# plt.imshow(cdc)
plt.savefig("cdc.png") 
print("2")

# 数据预处理
#剔除研究范围外的数据，计算原理是在方法中先栅格化后栅格匹配研究范围后实现对应。因此这里需要同时定义栅格大小，越小则精度越高
data = tbd.clean_outofshape(data, cdc, col=['lon', 'lat'], accuracy=500)

# 定义研究范围边界
bounds = [103.4668, 29.5468, 130.3851, 46.7926]

# 通过边界获取栅格化参数
params = tbd.area_to_params(bounds, accuracy = 1000)
params

 #将GPS数据对应至栅格，将生成的栅格编号列赋值到数据表上作为新的两列
data['LONCOL'],data['LATCOL']= tbd.GPS_to_grids(data['lon'],data['lat'],params)

# 聚合集计栅格内数据量
grid_agg=data.groupby(['LONCOL','LATCOL']).count().reset_index()

# 生成栅格的几何图形
grid_agg['geometry']=tbd.grid_to_polygon([grid_agg['LONCOL'],grid_agg['LATCOL']],params)

# 转换为GeoDataFrame
grid_agg=gpd.GeoDataFrame(grid_agg)

# 绘制栅格
grid_agg.plot(column = 'lon',cmap = 'autumn_r')
plt.savefig("shange.png")

fig =plt.figure(1,(8,8),dpi=300)
ax =plt.subplot(111)
plt.sca(ax)

# 添加行政区划边界作为底图
cdc.plot(ax=ax,edgecolor=(0,0,0,1),facecolor=(0,0,0,0),linewidths=0.5)

# 绘制colorbar
cax=plt.axes([0.05, 0.33, 0.02, 0.3])
plt.title('Data count')
plt.sca(ax)

# 绘制OD
# od_gdf.plot(ax = ax,column = 'count',cmap = 'Blues_r',linewidth = 0.5,vmax = 10,cax = cax,legend = True)

# 添加比例尺和指北针
tbd.plotscale(ax,bounds=bounds,textsize=10,compasssize=1,accuracy=2000,rect = [0.06,0.03],zorder = 10)
plt.axis('off')
plt.xlim(bounds[0],bounds[2])
plt.ylim(bounds[1],bounds[3])
plt.savefig("shange1.png")

# G = ox.graph_from_place('Chengdu, Sichuan, China', network_type='dirve')

# bounds = [103.4668, 29.5468, 130.3851, 46.7926]
# north, south, east, west = bounds[3], bounds[1], bounds[2], bounds[0]
# print("1")
# G = ox.graph_from_bbox(north, south, east, west, network_type='drive')
# print("2")
# Gg = ox.plot_graph(G)


print("finish")
# 写json文件
# def write_json(data, json_file, format=None):
#     with open(json_file, "w") as f:
#         if format == "good":
#             f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
#         else:
#             f.write(json.dumps(data))

# write_json(read_csv('G:/nyc/data.csv'), 'data.json')


