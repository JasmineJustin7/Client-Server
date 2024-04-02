import threading
import sqlite3
import hashlib
import socket

conn = sqlite3.connect("test_databases.db")

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ("localhost", 8888)
ss.bind(server_binding)
ss.listen()

def start_connection(c): # take client as parameter
    msg = "Welcome! Enter your username: "
    c.send(msg.encode())
    
    username = c.recv(1024).decode()
    print("[S]: Data received from client: " + username)
    
    """my_cursor = conn.connect()
    my_cursor.execute("SELECT * from users")
    my_result = my_cursor.fetchall() """
    
    msg = "Enter password: " # prompt user to enter password
    c.send(msg.encode())
    
    password = c.recv(1024).decode()
    print("[S]: Data received from client: " + password)
    
    print("You're in!")


while True:
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()
    
    # close the server socket
    ss.close()
    exit()


