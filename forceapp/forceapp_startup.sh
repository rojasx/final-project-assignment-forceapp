#!/bin/sh
bluetoothctl --agent NoInputNoOutput

bluetoothctl discoverable on

python3 /usr/share/misc/rpi_server.py