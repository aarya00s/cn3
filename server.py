# This file is used for sending the file over socket
import os
import socket
import time
import random
from security import encrypt
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 22222))
sock.listen(5)
print( sock.getsockname())
client, addr = sock.accept()

fname = "heat.mp4"
fsize = os.path.getsize(fname)

client.send(fname.encode())
client.send(str(fsize).encode())
with open(fname, "rb") as file:
    flag1 = 0
    start_time = time.time()
    while flag1 <= fsize:
        data = file.read(1024)
        if not (data):
            break
        enc_data = encrypt(data)
        client.sendall(enc_data)
        flag1 += len(data)

    end_time = time.time()

print("sec", end_time - start_time)
sock.close()
