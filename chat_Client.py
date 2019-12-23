import time, socket, sys
print("\n Welcome to chat room")
print("Initialising.....")
time.sleep(1)

#step 1
s=socket.socket() #creating a socket
shost=socket.gethostname()
ip=socket.gethostbyname(shost)
print(shost, "( " ,ip, " )\n")  #printing the host and ip address
host=input(str("enter the server address to connect"))

name=input(str("enter your name..."))

port=1234

print("\n Trying to connect ",host)

time.sleep(1)

s.connect((host, port))

print("Connected.....\n")

s.send(name.encode()) #to send the client's name

s_name=s.recv(1024) #to receive the server name

s_name=s_name.decode()

print(s_name, " has joined in chatroom") #to print who has joined

#chat process

while True:
   message=s.recv(1024)
   message=message.decode()
   print(s_name , ":", message)
   message=input(str("Me :  "))
   if message == 'bye':
    server.close()
   s.send(message.encode())

