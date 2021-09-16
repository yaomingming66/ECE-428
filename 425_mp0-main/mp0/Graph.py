import matplotlib.pyplot as plt
import pandas as pd
import math










# Plot Delay Graph
plt.title('Delay Graph')
plt.xlabel('Time(s)')
plt.ylabel('Delay(ms)')
plt.xticks()

plt.plot(x,MaxDelay,maker='o',markersize=2)
plt.plot(x,MinDelay,maker='o',markersize=2)
plt.plot(x,MedianDelay,maker='o',markersize=2)
plt.plot(x,NinetyPercentileDelay,maker='o', markersize=2)

plt.legend(["Maximum Delay", "Minimum Delay", "Median Delay", "90th Percentile Delay"])

plt.show()


# Plot Average Bandwidth
plt.title('Bandwidth Graph')
plt.xlabel('Time(s)')
plt.ylabel('Bandwidth(bps)')
plt.xticks()

plt.plot(x,AvgBW,maker='o', makersize =2)

plt.legend(["Average Bandwidth"])

plt.show()