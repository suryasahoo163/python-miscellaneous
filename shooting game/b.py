import socket
import pickle
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",1100))
k=s.recv(1024)
k=pickle.loads(k)
print(k)