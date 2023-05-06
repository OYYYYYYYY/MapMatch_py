import transbigdata as tbd
import pandas as pd
import matplotlib.pyplot as plt

# 地图匹配包
from leuvenmapmatching.matcher.distance import DistanceMatcher
from leuvenmapmatching.map.inmem import InMemMap
from leuvenmapmatching import visualization as mmviz
 
#读取数据
# data = pd.read_csv('./chengdu/chengdu201608.csv',header = None)
# data = pd.read_csv('./chengdu/cdc_tony.csv',header = None)
# data.columns = ['hour', 'lon', 'lat']

# 获取路网
import osmnx as ox
# bounds = [103.4668, 29.5468, 130.3851, 46.7926]
# north, south, east, west = bounds[3], bounds[1], bounds[2], bounds[0]
# G = ox.graph_from_bbox(north, south, east, west, network_type='drive')
G = ox.graph_from_place('Chengdu, Sichuan', network_type='dirve')

#存储路网
# ox.save_graphml(G,'chengdu.graphml')

#路网投影到UTM
# G_p = ox.project_graph(G)
# ox.plot_graph(G_p)

fig, ax = ox.plot_graph(G, node_size=2, node_color='r', edge_color='w', edge_linewidth=0.2)


#获取道路中心点坐标
# nodes, edges = ox.graph_to_gdfs(G, nodes=True, edges=True)
# edges['lon'] = edges.centroid.x
# edges['lat'] = edges.centroid.y

#转换路网的坐标系

# #投影到UTM
# G_p = ox.project_graph(G, to_crs=2416)
# nodes_p, edges_p = ox.graph_to_gdfs(G_p, nodes=True, edges=True)

# edges_p.plot()

# # 将路网转换为网络
# map_con = InMemMap(name='pNEUMA', use_latlon=False) # , use_rtree=True, index_edges=True)
 
# # 构建网络
# for node_id, row in nodes_p.iterrows():
#     map_con.add_node(node_id, (row['y'], row['x']))
# for node_id_1, node_id_2, _ in G_p.edges:
#     map_con.add_edge(node_id_1, node_id_2)

# #用transbigdata提取出行轨迹
# import geopandas as gpd
# tmp_gdf = data_deliver[data_deliver['ID'] == 22].sort_values(by = 'hour')
# #轨迹增密
# # tmp_gdf = tbd.traj_densify(tmp_gdf,col = ['ID', 'Time', 'Lng', 'Lat'],timegap = 15)
# #转换轨迹的坐标系为地理坐标系
# tmp_gdf['geometry'] = gpd.points_from_xy(tmp_gdf['lon'],tmp_gdf['lat'])
# tmp_gdf = gpd.GeoDataFrame(tmp_gdf)
# tmp_gdf.crs = {'init':'epsg:4326'}
# tmp_gdf = tmp_gdf.to_crs(2416)
#获得轨迹点
# path = list(zip(tmp_gdf.geometry.y, tmp_gdf.geometry.x))
# #构建地图匹配工具
# matcher = DistanceMatcher(map_con, 
#                           max_dist=500, 
#                           max_dist_init=170, 
#                           min_prob_norm=0.0001,
#                         non_emitting_length_factor=0.95,
#                         obs_noise=50, 
#                           obs_noise_ne=50,
#                               dist_noise=50,
#                               max_lattice_width=20,
#                               non_emitting_states=True)
# #进行地图匹配
# states, lastidx = matcher.match(path, unique=False)
# #绘制底图匹配结果
# mmviz.plot_map(map_con, matcher=matcher,
#                show_labels=False, show_matching=True,# show_graph=True,
#                filename=None)

# #获取地图匹配的路径geodataframe
# pathdf = pd.DataFrame(matcher.path_pred_onlynodes,columns = ['u'])
# pathdf['v'] = pathdf['u'].shift(-1)
# pathdf = pathdf[-pathdf['v'].isnull()]
# pathgdf = pd.merge(pathdf,edges_p.reset_index())
# pathgdf = gpd.GeoDataFrame(pathgdf)
# pathgdf.plot()
# pathgdf.crs = {'init':'epsg:2416'}
# pathgdf_4326 = pathgdf.to_crs(4326)

# #与路网一起可视化
# import matplotlib as mpl
# import matplotlib.pyplot as plt
 
# fig     = plt.figure(1,(8,8),dpi = 100)    
# ax      = plt.subplot(111)
# plt.sca(ax)
# fig.tight_layout(rect = (0.05,0.1,1,0.9))
# #设定可视化边界
# bounds = pathgdf_4326.unary_union.bounds
# gap = 0.003
# bounds = [bounds[0]-gap,bounds[1]-gap,bounds[2]+gap,bounds[3]+gap]
# #绘制匹配的路径
# pathgdf_4326.plot(ax = ax,zorder = 1)
# #绘制底图路网
# tbd.clean_outofbounds(edges,bounds,col = ['lon','lat']).plot(ax = ax,color = '#333',lw = 0.1)
# #绘制GPS点
# tmp_gdf.to_crs(4326).plot(ax = ax,color = 'r',markersize = 5,zorder = 2)
 
# plt.axis('off')
# plt.xlim(bounds[0],bounds[2])
# plt.ylim(bounds[1],bounds[3])
# plt.show()

