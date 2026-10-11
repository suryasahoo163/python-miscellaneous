
########### making a dedicated server for atm.py
####  modules
import socket
import pickle
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

print(data)

for k in data:

   data[data.index(k)]=list(k)

print("all data present in server: ")

for i in data:
    print(i)


#Closing the connection

print("\n ###############################")

### making a server place
port=163
skt=socket.socket()
skt.bind(("localhost",port))
skt.listen(10)
print("ready to connect ;)")


######## function to accept multiple client
def change_balance(addr,c):
   lst=c.recv(1024)
   d=pickle.loads(lst)
   if d[0]==0:
        cursor.execute(f'update bank set balance={d[1]} where id={d[-1]}')
   




def operation(skt):
    dts=""
    c, addr = skt.accept()
    
    print("connected to ",addr)
    dt=c.recv(1024).decode("utf-8")
    print("recieved",dt,"from ",addr)
    dt=dt.split()
    found=False
    change_balance(addr,c)
    for i in data:
      if i[-1]==dt[0] and i[1]==dt[-1]:
        found=True
    
        print(i)
        link=pickle.dumps(i)
    
        c.send(link)
    else:
      c.send(bytes("False","utf-8"))
   

   
while True: 
  operation(skt)# Close the connection with the client
conn.close()
