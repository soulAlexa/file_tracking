import socket


class prot_client():
    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 2000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        print(111111111)
        self.management()
        print("3234234")

    def management(self):
        while True:
            data_recv = self.sock.recv(1024)
            data_recv = data_recv.decode()
            print("Получено сообщение: ", data_recv)
            data_send = "Диалог"
            data_send = data_send.encode()
            self.sock.sendall(data_send)
            self.fille_accept()

    def accept(self):
        while True:
            data = input("Напишите сообщение: ")
            data_bytes = data.encode()
            self.sock.sendall(data_bytes)
            data_bytes = self.sock.recv(1024)
            data = data_bytes.decode()
            print("Получено сообщение: ", data)

    def fille_accept(self):
        filename = "test_client2.docx"
        file = open(filename, "wb")
        size_fill = 0
        size = 0
        while True:
            if size_fill == 0:
                f = self.sock.recv(8)
                size_fill = int.from_bytes(f, 'big')
                continue
            size += 4096
            if size > size_fill:
                file_data = self.sock.recv(size - size_fill)
                file.write(file_data)
                file.close()
                print("fille accepted")
                break
            else:
                file_data = self.sock.recv(4096)
            file.write(file_data)

    def fille_send(self):
        filename = "server.docx"
        file = open(filename, "rb")
        byte_len = (len(file.read())).to_bytes(8, 'big')
        self.sock.sendall(byte_len)
        file.seek(0)
        while True:
            file_data = file.read(4096)
            self.sock.send(file_data)
            if not file_data:
                break
        print("file sended")


if __name__ == '__main__':
    a = prot_client()