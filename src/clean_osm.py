#!/usr/bin/python
# -*- coding: UTF-8 -*-
import osm2gmns as og
# from CarRecord import *
# from Arc import *
# from math import *
# import queue
# import matplotlib.pyplot as plt
# import sys
# import time
# import os


net = og.getNetFromFile('./data/map_sz.osm',network_types=('auto',), POI=True, default_lanes=True, default_speed=True, default_capacity=True)
og.consolidateComplexIntersections(net, auto_identify=True)
og.connectPOIWithNet(net)
og.outputNetToCSV(net, output_folder='')