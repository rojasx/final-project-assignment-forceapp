#!/bin/sh
# Configure bluetooth settings
bluetoothctl agent off
sleep 1
bluetoothctl agent NoInputNoOutput
sleep 1
bluetoothctl pairable on
sleep 1
bluetoothctl discoverable on
sleep 1

# Run the app
python3 /usr/share/misc/rpi_server.py