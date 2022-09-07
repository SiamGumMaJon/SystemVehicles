

import socket
import time
# from apps.gpstracking.splittext import ddmtodd
serverip = '127.0.0.1'
port = 2000

def sendmasage(message):
    data = message
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((serverip,port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Data form server',data_server)
    server.close()

with open('apps\gpstracking\GPS.txt', encoding='utf8') as f:
        for line in f:
            time.sleep(.2)
            print (line)
            sendmasage(line)
            print(line.strip())
            
    # while True:
    # lines = len(f.readlines())
    # print('Total Number of lines:', lines)
    # line = f.readline()
    #     time.sleep(3)
    #     if not line:
    #         break
    #     print(line.strip())
        

# while True:
# 	data = input('Enter Message: ')
# 	server = socket.socket()
# 	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# 	server.connect((serverip,port))
# 	server.send(data.encode('utf-8'))

# 	data_server = server.recv(1024).decode('utf-8')
# 	print('Data form server',data_server)
# 	server.close()
