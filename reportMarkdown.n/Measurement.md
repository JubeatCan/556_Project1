# Project 1 (Client/Server Measurement)

## Member

Can Sun, cs94

Junjie Zhao, 

Ying Zhou, 

## Measure Report

### Method

$Independent\_Delay = Total\_Latency - Dependent\_Delay$

$Dependent\_Delay = \frac{Data\_Size}{BandWidth}$

### Details

In our calculation, we suppose the $BandWidth$ to be 10Gbps and $Total\_Latency$ is the time interval between *the start of send from client to server* and *the end of receive from server to client*, which is a 2-way latency.

To minimize the error, we choose the average result for the measurement of a single data size.

```shell
for i in {11..65535}
do
    if [[ $(($i % 100)) == 0 ]];
    then
        ./client_num jade.clear.rice.edu 18005 $i 100
    fi
done
```

As the script shows, we calculate the latency for data size from 100 to 65500 with the step size of 100.

### Result

![Data2](/Users/cansun/Documents/GR_2sem/556_NW/556Network_Project1/556_Project1/reportMarkdown/Data2.png)

As we can tell from the plot, the results are stable **between 10000 bytes and 35000 bytes**, which is **0.13 ms**.

However, it is unstable when the size of data is less than 10000 bytes. or more than 35000 bytes. For the lower part, $Dependent\_Delay$ is so small that the result depends on the $Total\_Latency$. For the higher part, the send and recv relies on I/O speed and it may bring unpredictable result to the latency test.

