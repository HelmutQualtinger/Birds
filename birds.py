import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd
import numpy as np
birddata = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@bird_tracking.csv", index_col=0)
birddata.head()

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
dlat=dict()
dlong=dict()
dlat["Eric"]=eric_daily_latitude
dlong["Eric"]=eric_daily_longitude
dlat["Nico"]=nico_daily_latitude
dlong["Nico"]=nico_daily_longitude
dlat["Sanne"]=sanne_daily_latitude
dlong["Sanne"]=sanne_daily_longitude

plt.figure(figsize=(8,8))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=":")
bird_name = ["Eric","Sanne","Nico"] 
for name in bird_name:
    ix = birddata ["bird_name"] == name
    x,y=birddata.longitude[ix],birddata.latitude[ix]
    ax.plot(dlong[name],dlat[name],".",transform=ccrs.Geodetic(),label=name)
plt.legend(loc="upper left")
plt.show()