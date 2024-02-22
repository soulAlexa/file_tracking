import socket


class prot_client():
    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 2000
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        self.accept()

    def accept(self):
        print(111)
