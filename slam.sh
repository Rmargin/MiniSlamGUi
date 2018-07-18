#!/bin/bash
cd /home/wangrz/workspace/workcode/Carto2018-04-18
pwd
source devel_isolated/setup.bash
sudo chmod 777 /dev/ttyUSB0
ls
python test_slamGUI.py

sleep 10
