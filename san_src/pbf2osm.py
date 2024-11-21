# import pyrosm

# # 输入和输出文件路径
# input_pbf_file = "input_file.pbf"  # 替换为你的输入 PBF 文件路径
# output_osm_file = "output_file.osm"  # 替换为你的输出 OSM 文件路径

# min_lon = 37.33
# max_lon = 37.92
# min_lat = -122.50997
# max_lat = -122.01119

# # 定义感兴趣区域的边界框坐标 [min_lon, min_lat, max_lon, max_lat]
# bbox = [min_lon, min_lat, max_lon, max_lat]  # 替换为你感兴趣区域的实际坐标

# # 创建一个 OSM 数据读取器，限定边界框
# osm = pyrosm.OSM(input_pbf_file, bounding_box=bbox)

# # 读取 PBF 文件并将其写入 OSM 文件
# osm.download_data()
# osm.to_file(output_osm_file, "xml")  # 将数据写入为 XML 格式的 OSM 文件







# import osmium
# from shapely.geometry import Polygon, MultiPolygon, Point
# from shapely.ops import transform
# from functools import partial
# import pyproj

# # Function to convert latitude and longitude to projected coordinates
# def lonlat_to_xy(lon, lat):
#     proj = pyproj.Proj(proj='merc', ellps='WGS84')
#     return proj(lon, lat)

# class OSMHandler(osmium.SimpleHandler):
#     def __init__(self, polygon, outfile):
#         super(OSMHandler, self).__init__()
#         self.polygon = polygon
#         self.outfile = outfile

#     def way(self, w):
#         if 'highway' in w.tags:
#             coords = [(n.lon, n.lat) for n in w.nodes]
#             way_polygon = Polygon(coords)
#             if way_polygon.intersects(self.polygon):
#                 self.outfile.write(w)
#                 self.outfile.write('\n')

# def extract_osm_data(pbf_file, min_lon, min_lat, max_lon, max_lat, output_file):
#     # Convert lon/lat coordinates to projected coordinates
#     min_x, min_y = lonlat_to_xy(min_lon, min_lat)
#     max_x, max_y = lonlat_to_xy(max_lon, max_lat)

#     # Create polygon from projected coordinates
#     boundary = Polygon([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)])

#     # Initialize OSMHandler and parse the PBF file
#     with open(output_file, 'w') as outfile:
#         handler = OSMHandler(boundary, outfile)
#         handler.apply_file(pbf_file)

# if __name__ == '__main__':
#     pbf_file = 'your_osm_data.pbf'  # Path to your OSM PBF file
#     min_lon = -74.1  # Example minimum longitude
#     min_lat = 40.6  # Example minimum latitude
#     max_lon = -73.8  # Example maximum longitude
#     max_lat = 40.9  # Example maximum latitude
#     output_file = 'extracted_data.osm'  # Output file for extracted OSM data

#     extract_osm_data(pbf_file, min_lon, min_lat, max_lon, max_lat, output_file)





import osmium

class OSMHandler(osmium.SimpleHandler):
    def __init__(self):
        super(OSMHandler, self).__init__()
        self.output = open('/data/oydata/MapMatch_py/data/osm_file/sf.osm', 'w', encoding='utf-8')

    def node(self, n):
        self.output.write(f"  <node id='{n.id}' lat='{n.location.lat}' lon='{n.location.lon}'/>\n")

    def way(self, w):
        self.output.write(f"  <way id='{w.id}'>\n")
        for node in w.nodes:
            self.output.write(f"    <nd ref='{node.ref}'/>\n")
        for tag in w.tags:
            self.output.write(f"    <tag k='{tag.k}' v='{tag.v}'/>\n")
        self.output.write("  </way>\n")

    def finalize(self):
        self.output.write("</osm>\n")
        self.output.close()

if __name__ == '__main__':
    handler = OSMHandler()
    handler.apply_file("/data/oydata/MapMatch_py/data/osm_file/north-america-latest.osm.pbf")
