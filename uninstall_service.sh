#!/bin/bash
sudo systemctl stop plot_temperature.service
sudo systemctl disable plot_temperature.service
sudo rm /etc/systemd/system/plot_temperature.service
sudo systemctl daemon-reload
sudo systemctl reset-failed
