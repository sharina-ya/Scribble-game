import socket
from _thread import *

server = "192.168.41.16"
#server = "192.168.141.246"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
currentPlayer = 0

#start info abaout players
#начальная информация об игроках
info = [(0, 0, "", "b"), (0, 0, "", "b")]

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started\nWaiting for connection")


#converts recieved data into tuple
#преобразовывает полученную информацию в кортеж
def read_info(s):
    s = s.split(",")
    return (s[0]), (s[1]), (s[2]), (s[3])

#converts data into string (to send it to another server)
#преобразовывает нужную информацию в строку, которую потом отправим на другой сервер
def make_info(tup):
    return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2]) + "," + str(tup[3])

#working with clients info
#работаем с информацией клиентов
def threaded_client(conn, player):
    global currentPlayer
    conn.send(str.encode(make_info(info[player])))
    reply = ""

    while True:
        try:
            #recieving data from client and update it's information
            #принимаем информацию от клиента и обновляем ее
            data = read_info(conn.recv(2024).decode())
            info[player] = data

            if not data:
                print("Disconnected")
                info[player] = (0, 0, "", "b")
                break
            else:
                #если инфо получено от того, кто угадывает
                #if info was received from the one who guessing
                if player == 1:
                    info[0] = (info[0][0], info[0][1], data[2], info[0][3])
                    reply = info[0]
                else:
                    reply = info[1]
                    
                print("Received: ", data)
                print("Sending: ", reply)
            
            conn.sendall(str.encode(make_info(reply)))
            
        except:
            break

    currentPlayer -= 1
    print("Lost connection")
    conn.close()

while True:
    #getting new connection from client
    #принимает подключение клиента
    conn, addr = s.accept()
    print("Connected to:", addr)

    #starting new thread
    #создаем новый поток
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
