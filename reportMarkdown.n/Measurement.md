# Project 1 (Client/Server Measurement)

## Member

Can Sun, cs94

Junjie Zhao, 

Ying Zhou, 

## Measure Report

### Method

$Independent\_Delay = Total\_Latency - Dependent\_Delay$

$Dependent\_Delay = \frac{Data\_Size}{BandWidth}$

We derive a formula from this: $TotalDelay = \frac{1}{BandWidth}DataSize + IndependentDelay$

### Details

In our calculation, $Total\_Latency$ is the time interval between *the start of send from client to server* and *the end of receive from server to client*, which is a 2-way latency.

To minimize the error, we choose the average result for the measurement of a single data size.

```shell
for i in {11..65535}
do
    if [[ $(($i % 10)) == 0 ]];
    then
        ./client_num jade.clear.rice.edu 18005 $i 100
    fi
done
```

As the script shows, we calculate the latency for data size from 20 to 65500 with the step size of 10.

### Result

![Data2](/Users/cansun/Documents/GR_2sem/556_NW/556Network_Project1/556_Project1/reportMarkdown.n/pic1.png)

After the linear approximation, we found that the **independent delay is** **0.1008 Msec** and **the bandwidth is 5330 Mbps**.

