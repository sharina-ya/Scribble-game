import socket
from _thread import *
import sys

server = "192.168.41.16"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

currentPlayer = 0

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started\nWaiting for connection")


def read_position(s):
    s = s.split(",")
    return int(s[0]), int(s[1])

def make_position(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0, 0),(100, 100)]
def threaded_client(conn, player):
    global currentPlayer
    conn.send(str.encode(make_position(pos[player])))
    reply = ""

    while True:
        try:
            data = read_position(conn.recv(2024).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(str.encode(make_position(reply)))
        except:
            break
    currentPlayer -= 1
    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1