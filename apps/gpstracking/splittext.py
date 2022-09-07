text = '*HQ,9172555780,V1,004046,A,1354.4093,N,10040.0614,E,0.00,82,100722,fbfffbff,520,01,8020,39095#'
text2 = "start: ,2022-07-10 07:43:21.961675,connectfrom: ,('49.230.75.104', 55050),data: ,*HQ,9172555780,V1,004317,A,1354.4088,N,10040.0619,E,0.00,82,100722,fbfffbff,520,01,8020,39095#,usetime: ,0:00:15.717142"
# print(text1)
value = text2.split(',')
a=6 # เพิ่ม index หลัง split
print (value)
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
arred = lambda x,n : x*(10**n)//1/(10**n)


# with open('apps\gpstracking\GPS.txt', encoding='utf8') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line.strip())



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
    km = knots*1.85
    return int(arred(km,0))


print(ddmtodd(latitude,pole,longitude,equator))
print(knottokm(33))