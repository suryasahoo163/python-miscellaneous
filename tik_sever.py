
import socket


####### identifires
connected_clients=[]
paired_clients=[]



############   server setup
id=1
port=1235
skt=socket.socket()
skt.bind(("localhost",port))
skt.listen(10)

def operation(skt):
    global id
    myid=id
    con,addr=skt.accept()
    print(f"connected to {addr} and id:{id}")
    qr=con.recv(1024).decode()
    if qr=="id":
        con.send(f"{id}".encode())
        connected_clients.append(id)
        id+=1
        print(connected_clients)
    for i in paired_clients:
        if myid == i[1]:
            oppenent_id=i[0]
        else:
            oppenent_id=i[1]
        print("sending")
        con.send(f"{oppenent_id}".encode())

########## making object of players and status

class player:
    
    
    

    

#####################       mainloop          ##################
while True:
    for i in range(0,(len(connected_clients)),2):
        try:
            if [connected_clients[i],connected_clients[i+1]] not in paired_clients:
                paired_clients.append([connected_clients[i],connected_clients[i+1]])
                print(paired_clients)
                
        except:
            pass
    operation(skt)
