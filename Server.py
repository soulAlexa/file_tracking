import socket
from _thread import *
import socketserver
import threading
from ast import literal_eval

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
            start_new_thread(self.management, (client, client_address))

    def authorization_con(self, client, client_address):#добавить шифрование
        while True:
            data_recv = client.recv(1024)
            data_recv = data_recv.decode()
            s = literal_eval(data_recv)
            user, password = s[0], s[1]
            print(user, password)
            #serch db
            if user == 'root' and password == '11111111':
                data_send = 1
                data_send = data_send.to_bytes(2, "little", signed=True)
                client.sendall(data_send)
                break
            else:
                data_send = -1
                data_send = data_send.to_bytes(2, "little", signed=True)
                client.sendall(data_send)
                exit_thread()

    def management(self, client, client_address):#добавить шифрование
        self.authorization_con(client, client_address)
        while True:
            data_send = "Выберите интересующую вас функцию: \n1)Диалог \n2)Отправить файл  \n3)Получить файл"
            data_send = data_send.encode()
            client.sendall(data_send)
            data_bytes = client.recv(1024)
            data = data_bytes.decode()
            print(f"Сообщение от: {client_address}", data)
            if data == "Диалог":
                self.accept(client, client_address)
                break

    def accept(self, client, client_address):#добавить шифрование
        while True:
            data_bytes = client.recv(1024)
            data = data_bytes.decode()
            print(f"Сообщение от: {client_address}", data)
            if data == "stop":
                break
            data = input(f"Напишите сообщение этому клиенту {client_address}:")
            data_bytes = data.encode()
            client.sendall(data_bytes)

    def fille_send(self, client, client_addres):#добавить шифрование
        filename = "server.docx"
        file = open(filename, "rb")
        byte_len = (len(file.read())).to_bytes(8, 'big')
        client.sendall(byte_len)
        file.seek(0)
        while True:
            file_data = file.read(4096)
            client.send(file_data)
            if not file_data:
                break
        print("file sended")

    def fille_accept(self, client, client_addres):#добавить шифрование
        filename = "test_ser2.docx"
        file = open(filename, "wb")
        size_fill = 0
        size = 0
        while True:
            if size_fill == 0:
                f = client.recv(8)
                size_fill = int.from_bytes(f, 'big')
                continue
            size += 4096
            if size > size_fill:
                file_data = client.recv(size - size_fill)
                file.write(file_data)
                file.close()
                print("fille accepted")
                break
            else:
                file_data = client.recv(4096)
            file.write(file_data)


if __name__ == '__main__':
    a = prot_server()

# class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
#
#     def handle(self):
#         data = str(self.request.recv(1024), 'ascii')
#         cur_thread = threading.current_thread()
#         response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
#         self.request.sendall(response)
#         print()
#
# class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
#     pass
#
# def client(ip, port, message):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.connect((ip, port))
#         sock.sendall(bytes(message, 'ascii'))
#         response = str(sock.recv(1024), 'ascii')
#         print("Received: {}".format(response))
#         print(ip, port)
#
# if __name__ == "__main__":
#     # Port 0 means to select an arbitrary unused port
#     HOST, PORT = "localhost", 2000
#
#     server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
#     with server:
#         ip, port = server.server_address
#
#         # Start a thread with the server -- that thread will then start one
#         # more thread for each request
#         server_thread = threading.Thread(target=server.serve_forever)
#         # Exit the server thread when the main thread terminates
#         server_thread.daemon = True
#         server_thread.start()
#         print("Server loop running in thread:", server_thread.name)
#
#         client(ip, port, "Hello World 1")
#         client(ip, port, "Hello World 2")
#         client(ip, port, "Hello World 3")
#         while True:
#             server.socket.listen(10)
#         # server.shutdown()