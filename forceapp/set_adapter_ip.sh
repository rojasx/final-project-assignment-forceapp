#!/bin/sh

# sudo ip addr add 10.99.99.23/24 dev adapter1
sudo ip addr add 192.168.0.130/24 dev adapter1
sudo ip link set dev adapter1 up