Check if success
```
lsmod | grep w1
w1_therm               24576  0
w1_gpio                12288  0
wire                   40960  2 w1_gpio,w1_therm
```

if not

```
sudo modprobe w1-gpio
sudo modprobe w1-therm
```