import socket
import pickle


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="192.168.50.158"
port=163
server.bind((ip,port))
server.listen(2)

print("waiting")

file=0
connection=[]
while True:
    con,add=server.accept()
    print("connected to ",add)
    if con not in connection:
        connection.append(con)
    if len(connection)>=2:
        break
print("connected device are\n",connection)

running=True
p1=p2=0
playerDict=[None,None]
while running:
    # print("loop running")
    for i in range(len(connection)):
       #######send and recieve PROPERTIES OF PLAYERS    
        try:
            
            val=connection[i].recv(1024*5)
            val=pickle.loads(val)
            playerDict[i]=val
            
        except:
            pass
            
    for i in range(len(playerDict)):
        try:
            if i==0:
                connection[i].send(pickle.dumps(playerDict[1]))
            elif i==1:
                connection[i].send(pickle.dumps(playerDict[0]))
        except:
            pass
            # print("cant send")
    
  
