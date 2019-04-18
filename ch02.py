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


