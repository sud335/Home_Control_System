import cv2
import numpy
import socket
import re
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(20)
client.connect(('localhost',8091))

while True:
    length = client.recv(16)
    print length
    stringData = ''
    count = int(length)
    while count>0:
        print count
        data= client.recv(int(count))
        if data:
            stringData+=data
            count=count-len(data)
    print len(stringData)
    if not data :
        break
    #stringData=data

    data = numpy.fromstring(stringData, dtype='uint8')
    print data
    decimg=cv2.imdecode(data,1)
    print decimg
    cv2.imshow('SERVER',decimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
client.close()
