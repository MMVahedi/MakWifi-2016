from socket import *
sn='192.168.43.132'
sp=11780
cs=socket(AF_INET,SOCK_STREAM)
cs.connect((sn,sp))
a=raw_input()
str=a
cs.send(str)
ms=cs.recv(1024)
cs.close()
