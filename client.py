import socket

# Package that allows two processes to happen at once
import threading

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()
    
# connect to the server on local machine
server_binding = ("localhost", 8888)
cs.connect(server_binding)

# receive data from server: Welcome to Blueprint
data_from_server = cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message)
cs.send(input("Response here: ").encode())

# receive data from server: How are you
data_from_server = cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message)
cs.send(input("Response here: ").encode())

# close the client sockets
cs.close()
exit()