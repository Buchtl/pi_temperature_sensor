#!/bin/bash
python3 -m src.plot_temperature --root-dir ./test_device --sensor-filename w1_slave --interval 1 --url="http://pi4b:8090/temp" --name="kammerl"
