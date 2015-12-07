import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('',8091))
server.listen(1)
client,addr = server.accept()

print addr
import cv2
import numpy
cap = cv2.VideoCapture(0)
import time
server.settimeout(10)
client.settimeout(10)
while True:

    ret, frame = cap.read()
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()
    client.sendall( str(len(stringData)).ljust(16))
    client.sendall( stringData )
    print frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
"""
send = open("/media/prashanth/General/Video profile/1031210023_PrashanthDVS.wmv","rb").read()
count=0
print len(send)
client.sendall(str(len(send)))

client.sendall(send)
"""    

client .close()
                
