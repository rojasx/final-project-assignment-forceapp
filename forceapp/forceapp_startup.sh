#!/bin/sh
sleep 2
bluetoothctl --agent NoInputNoOutput
sleep 2
bluetoothctl discoverable on
sleep 2
python3 /usr/share/misc/rpi_server.py