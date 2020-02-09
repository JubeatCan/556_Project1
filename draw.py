import numpy as np
import matplotlib.pyplot as plot

f = open('65535_100.txt','r')
lenth = 0
time = 0
band_with_error = 0
lilun = 0
l = []
t = []
be = []

while lenth != 99:
    lenth, time, band_with_error = f.readline().split()
    lenth = int(lenth)
    time = float(time)
    band_with_error = float(band_with_error)
    l.append(lenth)
    t.append(time)
    be.append(band_with_error)

x2 = np.arange(len(l))
plot.figure(figsize=(16,10))
plot.plot(x2, t, 'ro-')
plot.xticks(x2, l, rotation='vertical')
plot.title('i5-8279U with Shuffle On')
plot.xlabel('Size (Bytes)')
plot.ylabel('Time (Seconds)')
plot.legend()

plot.savefig('Data2.png')