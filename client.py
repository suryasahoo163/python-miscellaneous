import socket


skt=socket.socket()

    
def connect():
    print("connecting")
    while True:
        try:
            skt.connect(("localhost",19009))
            connected=True
            break
        except:
            connected=False
    print("connected")
def send_msg(msg):
    try:
        skt.send(bytes(msg,"utf-8"))
    except:
        connect()
    skt.close()
def rcv():
    try:
        rc=skt.recv(1024).decode()
    except:
        connect()
    if rc:
        return rc
    skt.close()

connect()
while True:
    r=rcv()
    if r :
        print(r)
skt.close()
