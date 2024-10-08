import socket
from _thread import *
import sys

# server = "192.168.41.16"
server = "192.168.141.246"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

currentPlayer = 0

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started\nWaiting for connection")


# считывает координаты рисование
def read_position(s):
    s = s.split(",")
    return (s[0]), (s[1])

# преобразовывает координаты в формат
def make_position(tup):
    return str(tup[0]) + "," + str(tup[1])

# позиции игроков по дефолту
pos = [(0, 0),(100, 100)]

# цикл работы клиентов
# потоки и тд
def threaded_client(conn, player):
    global currentPlayer
    conn.send(str.encode(make_position(pos[player])))
    reply = ""

    while True:
        try:



            # считывание координат в виду стоки
            data = read_position(conn.recv(2024).decode())
            pos[player] = data
            # обновление координат


            if not data:
                # не получаем инфы
                print("Disconnected")
                break
            else:
                # определение от кого получили инфу о координатах
                if player == 1:
                    # отправка от клиента 2
                    reply = pos[0]
                else:
                    reply = pos[1]
                # получил отправил для ориентации
                print("Received: ", data)
                print("Sending: ", reply)
            # кодировка ???
            conn.sendall(str.encode(make_position(reply)))


        except:
            break
    # при прырывании цикла отключается один из клиентов
    currentPlayer -= 1
    # потеря соединение и закрытие
    print("Lost connection")
    conn.close()

while True:
    # принимает подключение клиента s - soket
    conn, addr = s.accept()
    print("Connected to:", addr)

    # новый поток
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
