import geopandas as gpd
import pandas as pd

seoul_file = "/Users/taehwanyoon/PycharmProjects/geopy/seoul_market/TL_SCCO_EMD_2015_W.shp"
seoul = gpd.read_file(seoul_file, encoding='euckr')
seoul.tail()

market_file = "/Users/taehwanyoon/PycharmProjects/geopy/seoul_market/contents.csv"
market = pd.read_csv(market_file, encoding='euckr')
market.tail(3)

address = "서울 특별시 " + market["지번주소"].sample(50)
address = list(address)
address[:3]

location = gpd.tools.geocode(address, provider='googlev3', api_key="AIzaSyBB2Y3YKZmVd64eVoCE8Mc9TNHwwd6dDd0")
location.tail()


import matplotlib
matplotlib.use('Tkagg')
import matplotlib.pyplot as plt

ax = seoul.plot(figsize=(11, 11), color="w", edgecolor="k")
ax.set_title("Seoul market")
location.plot(ax=ax, color='r')
ax.set_axis_off()
plt.show()