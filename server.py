
import time, socket, sys
print("\n Welcome to chat room")
print("Initialising.....")
time.sleep(1)

#step 1
s=socket.socket() #creating a socket
host=socket.gethostname()
ip=socket.gethostbyname(host) #used to  the current IP address of the system
port=1234

#step 2
s.bind((host, port)) #binding the host and port

print(host, "(" ,ip, " )\n") #printing the host and ip address

name=input(str("enter your name..."))

#step 3
s.listen(1) #port should listen for connecting to the server
print("\n Waiting for incoming connection...")

conn, addr=s.accept() #when there is any connection, it will accept and get the address

print("\n Received connection from ", addr[0],  addr[1]) #should print which connection has been accepted

s_name=conn.recv(1024) #to get the name of the connector and this will be received in bytes format

s_name=s_name.decode() #decode the bytes into string

print(s_name," has connected to the chatroom")

conn.send(name.encode()) #sending your name to client

#chatting process

while True:
    message=input(str("Me:  "))
    conn.send(message.encode())
    message=conn.recv(1024)  #received message
    message=message.decode()
    print(s_name, ":", message)


