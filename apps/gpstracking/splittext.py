text = '*HQ,9172555780,V1,004046,A,1354.4093,N,10040.0614,E,0.00,82,100722,fbfffbff,520,01,8020,39095#'
# print(text1)
value = text.split(',')
# print (value)
Device = value[1]
time = value[3]
latitude = value[5].split()
pole = value[6]
longitude = value[7].split()
equator = value[8]
speed = value[9]
date = value [11]
status = value[12]
print (type(int(Device)))
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
    km = knots*1.85
    
    return int(arred(km,0))

print(ddmtodd(latitude,pole,longitude,equator))
print(knottokm(33))