import socket
import pickle
dt=[1,2,3,"3","5",["sdfas",["sdfasf"]]]
dt=pickle.dumps(dt)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",1100))
s.listen(2)
a,b=s.accept()
a.send(dt)