import osmium

class OSMHandler(osmium.SimpleHandler):
    def __init__(self, min_lon, min_lat, max_lon, max_lat):
        super(OSMHandler, self).__init__()
        self.min_lon = min_lon
        self.min_lat = min_lat
        self.max_lon = max_lon
        self.max_lat = max_lat
        self.output = open('/data/oydata/MapMatch_py/data/osm_file/sf_0.osm', 'w', encoding='utf-8')
        self.output.write("<?xml version='1.0' encoding='UTF-8'?>\n")
        self.output.write("<osm version='0.6' generator='YourSoftwareName'>\n")

    def node(self, n):
        if self.min_lon <= n.location.lon <= self.max_lon and self.min_lat <= n.location.lat <= self.max_lat:
            self.output.write(f"  <node id='{n.id}' lat='{n.location.lat}' lon='{n.location.lon}'/>\n")

    def way(self, w):
        if any(self.min_lon <= n.location.lon <= self.max_lon and self.min_lat <= n.location.lat <= self.max_lat for n in w.nodes):
            self.output.write(f"  <way id='{w.id}'>\n")
            for node in w.nodes:
                if self.min_lon <= node.location.lon <= self.max_lon and self.min_lat <= node.location.lat <= self.max_lat:
                    self.output.write(f"    <nd ref='{node.ref}'/>\n")
            for tag in w.tags:
                self.output.write(f"    <tag k='{tag.k}' v='{tag.v}'/>\n")
            self.output.write("  </way>\n")

    def finalize(self):
        self.output.write("</osm>\n")
        self.output.close()

if __name__ == '__main__':
    # Specify the bounding box coordinates for your desired small area
    min_lon = -122.51
    min_lat = 37.33
    max_lon = -121.95
    max_lat = 37.92

    handler = OSMHandler(min_lon, min_lat, max_lon, max_lat)
    handler.apply_file("/data/oydata/MapMatch_py/data/osm_file/north-america-latest.osm.pbf")
