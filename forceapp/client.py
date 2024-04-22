import bluetooth
import time

laptop_address = "4C:79:6E:89:2A:E1"
rfcomm_channel = 8
wait = 0.1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((laptop_address, rfcomm_channel))

number_to_send = 0
try:
    while(1):
        sock.send(str(number_to_send))
        number_to_send+=1
        time.sleep(wait)
except:
    print("Closing socket.")
    sock.close()

print("Closing socket.")
sock.close()
