import socket
from _thread import *

class prot_server():
    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 2000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen(3)
        print("Жду клиентов")
        while True:
            client, client_address = self.sock.accept()
            print(f"Клиент {client_address} подключён")
            start_new_thread(self.fille_send, (client, client_address))

    def accept(self, client, client_addres):
        while True:
            data_bytes = client.recv(1024)
            data = data_bytes.decode()
            print(f"Сообщение от: {client_addres}", data)
            data = input(f"Напишите сообщение этому клиенту {client_addres}:")
            data_bytes = data.encode()
            client.sendall(data_bytes)

    def fille_send(self, client, client_addres):
        filename = "server.docx"
        file = open(filename, "rb")
        file2 = open("test3.txt", "w")
        while True:
            file_data = file.read(4096)
            client.send(file_data)
            file2.write(str(file_data))
            if not file_data:
                break
        file.close()
        file2.close()
        print("file sended")

    def fille_accept(self, client, client_addres):
        filename = "test.docx"
        file = open(filename, "wb")
        file2 = open("test.txt", "w")
        while True:
            file_data = client.recv(4096)
            file2.write(str(file_data))
            file.write(file_data)
            if not file_data:
                break
        file.close()
        file2.close()
        print("file downloaded")


if __name__ == '__main__':
    a = prot_server()