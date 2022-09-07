from datetime import datetime
import time

import socket
arred = lambda x,n : x*(10**n)//1/(10**n)

def ddmtodd(lat,pole,long,equator):
    pole = pole.lower()
    equator = equator.lower()
    
    lat_dd = float(lat[0][-7:])/60
    lat_dd = lat_dd + float(lat[0][:-7])
    long_dd = float(long[0][-7:])/60
    long_dd = long_dd + float(long[0][:-7])
    if pole == 's':
        lat_dd = lat_dd*(-1)
    if equator == 'w':
        long_dd = long_dd*(-1)
    return [arred(lat_dd,4),arred(long_dd,4)]

def knottokm(knots):
    km = float(knots)*1.85
    return int(arred(km,0))

serverip = '127.0.0.1'
port = 2000
while True:
	f = open("GPSrecieve.txt", "a")
	# print (f'-'*50)
	timestart = datetime.now()
	# print (f'start : {datetime.now()}')
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.bind((serverip,port))
	server.listen(5)
	print('waiting for client....')
	client, addr = server.accept()
	# print (str(addr))
	data = client.recv(10240).decode('utf-8')
	# print (data)
	
	client.send('We received your Message! '.encode('utf-8'))
	client.close()
	timestop = datetime.now()
	# print (f'end : {datetime.now()}')
	# print (f'usetime : {timestop-timestart}')
	print (f'start: ,{datetime.now()},connectfrom: ,{str(addr)},data: ,{data},usetime: ,{timestop-timestart}')
	f.write(f'{data}')
	f.close()
	value = data.split(',')
	a=6 # เพิ่ม index หลัง split ต่างกัน
	Device = value[1+a]
	time = value[3+a]
	latitude = value[5+a].split()
	pole = value[6+a]
	longitude = value[7+a].split()
	equator = value[8+a]
	speed = value[9+a]
	date = value [11+a]
	status = value[12+a]
    # print (type(int(Device)))
	print(ddmtodd(latitude,pole,longitude,equator))
	print(knottokm(speed))
