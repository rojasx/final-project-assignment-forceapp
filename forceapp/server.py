import socket

my_address = '4C:79:6E:89:2A:E1'
rfcomm_channel = 8

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((my_address, rfcomm_channel))
server.listen(1)
client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if data:
            print(f"Message: {data.decode('utf-8')}", end="\r")
except OSError as e:
    pass
except KeyboardInterrupt:
    print("Closing socket.")
    client.close()
    server.close()

print("Closing socket.")
client.close()
server.close()