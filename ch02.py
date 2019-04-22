import geopandas as gpd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from descartes import PolygonPatch

fp = "/Users/taehwanyoon/PycharmProjects/geopy/Data/DAMSELFISH_distributions.shp"
data = gpd.read_file(fp)

type(data)
data.head()
data.plot()

out = r"/Users/taehwanyoon/PycharmProjects/geopy/Data/DAMSELFISH_distributions_SELECTION.shp"
selection = data[0:50]
selection.to_file(out)

fp2 = "/Users/taehwanyoon/PycharmProjects/geopy/Data/DAMSELFISH_distributions_SELECTION.shp"
data2 = gpd.read_file(fp2)

data2.plot()

data['geometry'].head()

selection = data[0:5]
for index, row in selection.iterrows():
    poly_area = row['geometry'].area
    print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))

data['area'] = data.area
data['area'].head(2)

max_area = data['area'].max()
mean_area = data['area'].mean()
print("Max area: %s\nMean area: %s" % (round(max_area, 2), round(mean_area, 2)))
# Okey, so the largest Polygon in our dataset seems to be 1494 square decimal degrees (~ 165 000 km2) and the average
# size is ~20 square decimal degrees (~2200 km2).

#-----------------------------------------------------
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon

newdata = gpd.GeoDataFrame()

newdata['geometry'] = None

coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coordinates)

newdata.loc[0, 'geometry'] = poly
newdata.loc[0, 'Location'] = 'Senaatintori'

from fiona.crs import from_epsg
newdata.crs = from_epsg(4326)

outfp = r"/Users/taehwanyoon/PycharmProjects/geopy/Data/Senaatintori.shp"
newdata.to_file(outfp)

grouped = data.groupby('BINOMIAL')

for key, values in grouped:
    individual_fish = values

import os
outFolder = r"/Users/taehwanyoon/PycharmProjects/geopy/Data"
resultFolder = os.path.join(outFolder, 'Results')
if not os.path.exists(resultFolder):
    os.makedirs(resultFolder)

for key, values in grouped:
    outName = "%s.shp" % key.replace(" ", "_")
    print("Processing: %s" % key)
    outpath = os.path.join(resultFolder, outName)
    values.to_file(outpath)

# map projection
import geopandas as gpd
fp ="/Users/taehwanyoon/PycharmProjects/geopy/Europe_borders/Europe_borders.shp"
data = gpd.read_file(fp)

data.crs

data['geometry'].head()

data_proj = data.copy()
data_proj = data_proj.to_crs(epsg=3035)

data_proj['geometry'].head()

import matplotlib.pyplot as plt
data.plot(facecolor='gray');
plt.title("WGS894 projection");
plt.tight_layout()
data_proj.plot(facecolor='blue');
plt.title("ETRS Lambert Azimuthal Equal Area projection");
plt.tight_layout()


# Korea
fp = "/Users/taehwanyoon/PycharmProjects/geopy/korea/korea.shp"
data_korea = gpd.read_file(fp)
data_korea_proj = data_korea.copy()
# data_korea_proj = data_korea_proj.to_crs(epsg=4326)
data_korea.plot(facecolor='gray');
plt.title("WGS894 projection");
plt.tight_layout()
# data_korea_proj.plot(facecolor='blue');
# plt.title("ETRS Lambert Azimuthal Equal Area projection");
# plt.tight_layout()

# 한국 행정구역
fp = "/Users/taehwanyoon/PycharmProjects/geopy/CTPRVN_201902/TL_SCCO_CTPRVN.shp"
data_korea = gpd.read_file(fp)
data_korea_proj = data_korea.copy()
data_korea.plot(facecolor='gray');
plt.title("WGS894 projection: South Korea");
plt.tight_layout()

from fiona.crs import from_epsg
data_proj.crs = from_epsg(3035)
data_proj.crs
# data_korea_proj.crs = from_epsg(3035)
outfp = r"/Users/taehwanyoon/PycharmProjects/geopy/Europe_borders/Europe_borders_epsg3035.shp"
data_proj.to_file(outfp)


# import pycrs
# crs_info = pycrs.parser.from_epsg_code(3035)

# Exercise 2 --------------------------------------------------------------------------------------------------------
geo = gpd.GeoDataFrame(data, geometry='geometry', crs=from_epsg(4326))

# Geocoding
# geopy

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

fp = r"/Users/taehwanyoon/PycharmProjects/geopy/addresses.txt"
data = pd.read_csv(fp, sep=';')

from geopandas.tools import geocode

geo = geocode(data['addr'], provider='nominatim')

join = geo.join(data)

outfp = r"/Users/taehwanyoon/PycharmProjects/geopy/addresses.shp"
join.to_file(outfp)

join.plot()
plt.tight_layout()



import osmnx as ox
import matplotlib.pyplot as plt
place_name = "Dogok, Seoul, Korea"
place_name = "Kamppi, Helsinki, Finland"
graph = ox.graph_from_place(place_name)
type(graph)

fig, ax = ox.plot_graph(graph)
plt.tight_layout()



