
from socket import *
a=raw_input()
sp=12619
ss=socket(AF_INET,SOCK_STREAM)
ss.bind(('',sp))
ss.listen(1)
while True:
    f=open(a,"a")
    sp+=1
    cs,addr=ss.accept()
    data=cs.recv(1024)
    if len(data)==1:
        f.write(data)
    if len(data)==2:
        if data==".0":
            print "ê"
    f.close()
    cs.send(data)
    cs.close()

