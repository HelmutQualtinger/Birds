import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd
import numpy as np
birddata = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@bird_tracking.csv", index_col=0)
birddata.head()
bird_list = set(birddata["bird_name"])

# Convert birddata.date_time to the `pd.datetime` format.
import datetime as dt
ts=[]
for i in range(len(birddata)):
    ts.append(dt.datetime.strptime(birddata.date_time.iloc[i][0:-12],"%Y-%m-%d"))


# Create a new column of day of observation
birddata["date"] = ts

# Use `groupby()` to group the data by bird and date.
grouped_birdname = birddata.groupby(["bird_name", "date"])

eric_daily_speed  = grouped_birdname.speed_2d.mean()["Eric"]
sanne_daily_speed  = grouped_birdname.speed_2d.mean()["Sanne"]
nico_daily_speed  = grouped_birdname.speed_2d.mean()["Nico"]

eric_daily_altitude  = grouped_birdname.altitude.mean()["Eric"]
sanne_daily_altitude  = grouped_birdname.altitude.mean()["Sanne"]
nico_daily_altitude  = grouped_birdname.altitude.mean()["Nico"]

eric_daily_latitude = grouped_birdname.latitude.mean()["Eric"]
eric_daily_longitude = grouped_birdname.longitude.mean()["Eric"]

nico_daily_latitude = grouped_birdname.latitude.mean()["Nico"]
nico_daily_longitude = grouped_birdname.longitude.mean()["Nico"]

sanne_daily_latitude = grouped_birdname.latitude.mean()["Sanne"]
sanne_daily_longitude = grouped_birdname.longitude.mean()["Sanne"]

import matplotlib.pyplot as plt
plt.xlabel('Datum')
plt.subplot(2,2,1)
plt.xlabel('Datum')
plt.ylabel('Geschwindkeit')
eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.subplot(2,2,2)
plt.xlabel('Datum')
plt.ylabel('Seehöhe')
eric_daily_altitude.plot(label="Eric")
sanne_daily_altitude.plot(label="Sanne")
nico_daily_altitude.plot(label="Nico")
plt.legend(loc="center")
plt.subplot(2,2,3)
plt.scatter(eric_daily_longitude, eric_daily_latitude,alpha=0.3)
plt.scatter(nico_daily_longitude, nico_daily_latitude,alpha=0.3)
plt.scatter(sanne_daily_longitude, sanne_daily_latitude,alpha=0.3)

plt.show()

proj =ccrs.Mercator()

plt.figure(figsize=(6,8),dpi=75)
ax = plt.axes(projection=proj)
ax.set_extent((-35.0, 30.0, 62.0, 0.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=":")
for name in bird_list:
    ix = birddata ["bird_name"] == name
    x,y=birddata.longitude[ix],birddata.latitude[ix]
    ax.plot(x,y,"",transform=ccrs.Geodetic(),label=name,alpha=0.8)
plt.legend(loc="upper left")
plt.show()

from bokeh.plotting import figure, output_file, show
from bokeh.tile_providers import CARTODBPOSITRON, WIKIMEDIA, get_provider
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from pyproj import Transformer


TRAN_4326_TO_3857 = Transformer.from_crs("EPSG:4326", "EPSG:3857")

def mytransform(lat, lon):
  return TRAN_4326_TO_3857.transform(lat, lon)


output_file("tile.html")

tile_provider = get_provider(WIKIMEDIA)
lat_M_low,lon_M_lo = TRAN_4326_TO_3857.transform(29.,-96.)
lat_M_hi,lon_M_hi = TRAN_4326_TO_3857.transform(32,-99)
# range bounds supplied in web mercator coordinates
p = figure(x_range=(-10000000, -9500000), y_range=(3000000, 4000000),
           x_axis_type="mercator", y_axis_type="mercator")
p.add_tile(tile_provider)
source = ColumnDataSource(
    data=dict(lat=[ 3029000,  3020000,  3029000],
              lon=[-9770000, -9774000, -9778000])
)

p.circle(x="lon", y="lat", size=25, fill_color="red", fill_alpha=1, source=source)
show(p)
