import socket


port=1235
player_id="connecting"

skt=socket.socket()

skt.connect(("localhost",port))

def send(msg):
    global skt
    skt.send(msg.encode())
def rcv():
    global skt
    return skt.recv(1024).decode()



