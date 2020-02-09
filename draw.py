import numpy as np
import matplotlib.pyplot as plot

f = open('dataJadeOpal.txt','r')
lenth = 0
time = 0
l = []
t = []

while lenth != 65500:
    lenth, time = f.readline().split()
    lenth = int(lenth)
    time = float(time)
    if time > 0 :
        l.append(lenth)
        t.append(time)

plot.figure(figsize=(20,10))
plot.plot(l, t)
plot.xticks(np.arange(min(l), max(l) + 1, 1000), rotation='vertical')
plot.title('Independent Delay between Jade and Opal')
plot.xlabel('Size (Bytes)')
plot.ylabel('Time (MSec)')
plot.legend()

plot.savefig('Data2.png')