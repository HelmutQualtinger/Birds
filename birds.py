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

import matplotlib.pyplot as plt

plt.subplot(2,1,1)
eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.subplot(2,1,2)
eric_daily_altitude.plot(label="Eric")
sanne_daily_altitude.plot(label="Sanne")
nico_daily_altitude.plot(label="Nico")
plt.legend(loc="center")
plt.show()