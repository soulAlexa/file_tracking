import socket


class prot_client():
    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 2000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        print(111111111)
        self.fille_accept()
        print("3234234")

    def accept(self):
        while True:
            data = input("Напишите сообщение: ")
            data_bytes = data.encode()  # (str to bytes)
            self.sock.sendall(data_bytes)  # Send
            data_bytes = self.sock.recv(1024)  # Receive
            data = data_bytes.decode()  # (bytes to str)
            print("Получено сообщение: ", data)

    def fille_accept(self):
        filename = "test.docx"
        file = open(filename, "wb")
        file2 = open("test2.txt", "w")
        while True:
            file_data = self.sock.recv(4096)
            if not file_data:
                print("22222222222222")
                break
            file2.write(str(file_data))
            file.write(file_data)

        file2.close()
        file.close()
        print("file downloaded")

    def fille_send(self):
        filename = "server.docx"
        file = open(filename, "rb")
        while True:
            file_data = file.read(4096)
            self.sock.send(file_data)
            if not file_data:
                break
        print("file sended")


if __name__ == '__main__':
    a = prot_client()