#!/bin/sh

ip addr add 192.168.0.13/24 dev end0
ip link set dev end0 up