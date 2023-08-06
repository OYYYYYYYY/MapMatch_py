######
清洗数据

check_tensor.py  对tensor的维度进行检查,去除掉一些

clean_csv.py  对csv文件进行清洗,筛选出需要的数据

clean_data.py 对得到的张量数据进行清洗,原来的张量数据在时间片范围为00:00-23:59.实际范围应该为6:00-23:59

clean_osm.py  清洗osm数据,生成link.csv,node.csv,poi.csv

clean_poi.py 对poi.csv进行清洗,只保留poi_id,centroid属性

clean_sinlink.py  对link_single.csv文件进行清洗,去除form_node_id和to_node_id,并对link_id进行重新编号

clean_tensor.cpp  对tensor进行清洗的cpp程序 待定

csv2csv_geo.py  对link.csv提取其中的geometry属性,目前已弃用

csv2csv_link.py  对link.csv进行清洗,保留属性link_id, from_node_id, to_node_id, geometry

csv2csv_node.py  对node.csv进行清洗,保留属性node_id, x_coord, y_coord

csv2csv_poi.py  对poi.csv进行清洗,保留属性poi_id, osm_way_id, geometry, centroid

csv2csv_samgps.py  对轨迹数据进行清洗

csv2csv_sinlink.py  对link_auto.csv进行简化,对其geometry属性中的坐标取平均值,最终只保留一个平均值

csv2csv.py  功能与clean_csv.py相同

generate_adjmat.py  生成路网的邻接矩阵

mapmatch.cpp  路网匹配c++程序

matchmap.py  路网匹配python程序,速度太慢,已经弃用

mergecsv.py  对csv文件进行合并

omain  mapmatch.cpp的可执行文件

poi_match.py  通过坐标将poi和link进行匹配

search_poi.py  通过高德/百度API搜寻对应坐标的poi,但API每天可调用的次数太低,已经弃用
