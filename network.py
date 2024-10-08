import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.41.16"
        #self.server = "192.168.141.246"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.info = self.connect()

    def getInfo(self):
        return self.info

    # client connets to server and receive info from server
    # клиент запрашивает подключении к серверу и считывает инфу от сервера
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    # client sends info to server and receive data from server
    # клиент отправляет данные на сервер и получает данные с сервера
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)


