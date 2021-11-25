<<<<<<< Updated upstream

import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 1500        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'dining hall up at localhost:500')
    data = s.recv(1024)

print('Received:', repr(data))
=======
# import socket programming library
import socket
import json
import pickle
with open("menu.json", "r") as menu_json:
    data1 = json.load(menu_json)
# import thread module
data2 = pickle.dumps(data1)
data3 = 5
from _thread import *
import threading

print_lock = threading.Lock()

# thread function
def threaded(c):
    while True:
        
        #here the data is received
        message_dining = c.recv(1024)
        #data is displayed
        print(message_dining.decode("ascii"))

        if not message_dining:
            print('closing connection')
            # lock released on exit
            print_lock.release()
            break
        data1 = {
            "brand": "chevrolet",
            "model": "Mustang",
            "year": 1964
        }
        message_kitchen = "this is the message sent from kitchen"
        message1 = message_kitchen + json.dumps(data1)
        
        #data sent back to dining
        c.send(message1.encode("ascii"))

    # connection closed
    c.close()


def Main():
    host = "localhost"

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5) #no of connections
    print("kitchen is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()
        # lock acquired by client
        print_lock.acquire()
        # print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()


>>>>>>> Stashed changes
