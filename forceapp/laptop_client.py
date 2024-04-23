import socket
import subprocess

# Constants
rfcomm_channel = 8
wait = 0.1

# Get the address of rpi
rpi_address = subprocess.check_output("bluetoothctl paired-devices | grep 'raspberrypi4' | awk '{print $2}'", shell=True).decode('utf-8').strip()
if not rpi_address:
    print("Could not find a paired force-sense device.")
    exit(0)
print(f"Using rpi address: {rpi_address}")

# Make connection
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect((rpi_address, rfcomm_channel))
print("Connected to RaspberryPi.")

# Do handshake
client.send("start".encode('utf-8'))

try:
    while True:
        data = client.recv(1024).decode('utf-8')
        print(f"            \rWeight: {data}", end="")
except Exception as e:
    print(f"Caught Exception: {e}.")
    print("Closing socket.")
    client.close()