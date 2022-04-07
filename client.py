# This file will be used for recieving files over socket connection.
import os
import socket
import time
from security import decrypt

host = input("p2p: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((host, 22222))
    print("server connected")
except:
    print("disabbled")
    exit(0)

f_name = sock.recv(100).decode()
f_size = sock.recv(100).decode()
with open("./cn/"+f_name, "wb") as file:
    flag1 = 0
    initial = time.time()
    try:
        while flag1 <= int(float(f_size)):
            data = sock.recv(1464)
            if not (data):
                break
            decode = decrypt(data)
            file.write(decode)
            flag1 += len(decode)
    except ValueError as e:
        print  ("")
 
    final = time.time()

print("File transfer", final - initial)

sock.close()
