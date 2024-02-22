import socket

class prot_server():
    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 2000
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        sock.listen(2)
        self.accept()

    def accept(self):
        print(111)

if __name__ == '__main__':
    a = prot_server()