import socket



skt=socket.socket()
skt.bind(("localhost",19009))
skt.listen(10)
con,add=skt.accept()
while True:
    
    
    i=input("enter msg:")
    con.send(bytes(i,"utf-8"))
    rcv=con.recv(1024)
    if len(rcv.decode())>0:
        print(rcv.decode())
skt.close()
