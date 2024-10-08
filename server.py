import sys
import socket
from _thread import *
from PyQt5 import QtWidgets, QtCore


port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
currentPlayer = 0
info = [(0, 0, "", "b"), (0, 0, "", "b")]


def start_server(ip):
    global currentPlayer
    try:
        s.bind((ip, port))
    except socket.error as e:
        print(str(e))
    s.listen(2)
    print("Server started\nWaiting for connection")

    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)
        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1


def read_info(s):
    s = s.split(",")
    return (s[0]), (s[1]), (s[2]), (s[3])


def make_info(tup):
    return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2]) + "," + str(tup[3])


def threaded_client(conn, player):
    global currentPlayer
    conn.send(str.encode(make_info(info[player])))
    reply = ""
    while True:
        try:
            data = read_info(conn.recv(2024).decode())
            info[player] = data
            if not data:
                print("Disconnected")
                info[player] = (0, 0, "", "b")
                break
            else:
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


class ServerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Сервер')
        self.setGeometry(100, 100, 300, 150)

        self.setStyleSheet("background-color: pink;")

        self.ipInput = QtWidgets.QLineEdit(self)
        self.ipInput.setPlaceholderText("Введите IP")
        self.ipInput.setGeometry(50, 30, 200, 30)

        self.startButton = QtWidgets.QPushButton('Запустить сервер', self)
        self.startButton.setGeometry(50, 80, 200, 30)
        self.startButton.clicked.connect(self.start_server)

    def start_server(self):
        ip = self.ipInput.text()
        self.startButton.setEnabled(False)
        start_new_thread(start_server, (ip,))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ServerApp()
    ex.show()
    sys.exit(app.exec_())
