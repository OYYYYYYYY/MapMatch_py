import transbigdata as tbd
import pandas as pd
# 地图匹配包
from leuvenmapmatching.matcher.distance import DistanceMatcher
from leuvenmapmatching.map.inmem import InMemMap
from leuvenmapmatching import visualization as mmviz
from shapely.geometry import Polygon,LineString,Point
 
#读取数据
data = pd.read_csv('./data/TaxiData-Sample.csv',header = None)
data.columns = ['VehicleNum','Time','lon','lat','OpenStatus','Speed']

#从GPS数据提取OD与路径GPS
oddata = tbd.taxigps_to_od(data,col = ['VehicleNum','Time','lon','lat','OpenStatus'])
data_deliver,data_idle = tbd.taxigps_traj_point(data,oddata,col=['VehicleNum', 'Time', 'lon', 'lat', 'OpenStatus'])

# 获取路网
import osmnx as ox
bounds = [113.75, 22.4, 114.62, 22.86]
north, south, east, west = bounds[3], bounds[1], bounds[2], bounds[0]
G = ox.graph_from_bbox(north, south, east, west, network_type='drive')

# #存储路网
# ox.save_graphml(G,'shenzhen.graphml')

# #获取道路中心点坐标
# nodes, edges = ox.graph_to_gdfs(G, nodes=True, edges=True)
# edges['lon'] = edges.centroid.x
# edges['lat'] = edges.centroid.y

# #转换路网的坐标系
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
# tmp_gdf = data_deliver[data_deliver['ID'] == 22].sort_values(by = 'Time')
# #轨迹增密
# tmp_gdf = tbd.traj_densify(tmp_gdf,col = ['ID', 'Time', 'lon', 'lat'],timegap = 15)
# #转换轨迹的坐标系为地理坐标系
# tmp_gdf['geometry'] = gpd.points_from_xy(tmp_gdf['lon'],tmp_gdf['lat'])
# tmp_gdf = gpd.GeoDataFrame(tmp_gdf)
# tmp_gdf.crs = {'init':'epsg:4326'}
# tmp_gdf = tmp_gdf.to_crs(2416)
# #获得轨迹点
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
# states, _ = matcher.match(path, unique=False)
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

