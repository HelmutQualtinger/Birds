import pandas as pd
import numpy as np
birddata = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@bird_tracking.csv", index_col=0)
birddata.head()

# First, use `groupby()` to group the data by "bird_name".
grouped_birds = birddata.groupby("bird_name")
print(len(grouped_birds))
grouped_birds.head()
# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds.speed_2d.mean()


# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds.altitude.mean()

print (mean_speeds, mean_altitudes)

# Convert birddata.date_time to the `pd.datetime` format.
import datetime as dt
ts=[]
for i in range(len(birddata)):
    ts.append(dt.datetime.strptime(birddata.date_time.iloc[i][0:-12],"%Y-%m-%d"))
#birddata.date = pd.to_datetime(birddata.date_time)
print (ts[0:5])

# Create a new column of day of observation
birddata["date"] = ts 

# Use `groupby()` to group the data by date.
grouped_bydates = birddata.groupby("date")
print (len(grouped_bydates))

# Find the mean `altitude` for each date.
mean_altitudes_perday = grouped_bydates.altitude.mean()
print (mean_altitudes_perday[0:100])

# Use `groupby()` to group the data by bird and date.
grouped_birdname = birddata.groupby(["bird_name", "date"])
#print(grouped_birdname)
# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = grouped_birdname.altitude.mean()
print(mean_altitudes_perday)

eric_daily_speed  = grouped_birdname.speed_2d.mean()["Eric"]
print(eric_daily_speed)
sanne_daily_speed  = grouped_birdname.speed_2d.mean()["Sanne"]
print(sanne_daily_speed)
nico_daily_speed  = grouped_birdname.speed_2d.mean()["Nico"]
print(nico_daily_speed)

eric_daily_altitude  = grouped_birdname.altitude.mean()["Eric"]
sanne_daily_altitude  = grouped_birdname.altitude.mean()["Sanne"]
nico_daily_altitude  = grouped_birdname.altitude.mean()["Nico"]

import matplotlib.pyplot as plt
#sanne_daily_speed = grouped_birdname.speed_2d[name=="Sanne"].mean()
#nico_daily_speed  = grouped_birdname.speed_2d[name=="Nico"].mean()
#plt.figure(figsize=(12,6))
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
