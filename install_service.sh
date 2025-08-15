#!/bin/bash
sudo cp ./systemd/plot_temperature.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable plot_temperature.service
sudo systemctl start plot_temperature.service


# check
sudo systemctl status plot_temperature.service
#sudo journalctl -u plot_temperature.service -f