
########### making a dedicated server for atm.py
####  modules
import socket


command="select* from bank;"
import mysql.connector
#establishing the connection
conn = mysql.connector.connect(user='root', passwd='suryasahoo', host="localhost", database='surya_table')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
#Executing an MYSQL function using the execute() method
cursor.execute(command)
# Fetch a single row using fetchone() method.
data = cursor.fetchall()
data=list(data)
for k in data:
    i=list(k)
    i.insert(1,k[-1])
    i.pop()
    data[data.index(k)]=i
print("all data present in server: ")
for i in data:
    print(i)
#Closing the connection
conn.close()
print("\n ############################")

### making a server place
skt=socket.socket()
skt.bind(("localhost",10590))
skt.listen(10)
print("ready to connect ;)")


######## function to accept multiple client
def operation(skt):
    dts=""
    c, addr = skt.accept()
    print("connected to ",addr)
    dt=c.recv(1024).decode("utf-8")
    print("recieved",dt,"from ",addr)
    dt=dt.split()
    found=False
    for i in data:
      if i[1]==dt[0] and i[2]==dt[1]:
        found=True
        for j in i:
            print(j)
            j=str(j)
            dts+=j+" "
        print(dts)
        c.send(bytes(dts,"utf-8"))
    else:
      c.send(bytes("False","utf-8"))
    c.close() 


    
while True: 
  operation(skt)# Close the connection with the client 
