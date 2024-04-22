import socket
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget
import sys
from _thread import *

class prot_client():
    def __init__(self, window):
        HOST = '127.0.0.1'
        PORT = 2000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        # self.authorization_con()
        self.management()
        print("3234234")

    def authorization_con(self):#добавить шифрование
        data_send = str((window._login.text(), window._passw.text()))
        print(data_send)
        data_send = data_send.encode()
        self.sock.sendall(data_send)
        data_recv = self.sock.recv(2)
        data_recv = int.from_bytes(data_recv, 'little', signed=True)
        if data_recv:
            return True
        else:
            return False

    def management(self):#добавить шифрование
        if self.authorization_con():
            pass
        else:
            exit_thread()
        while True:
            data_recv = self.sock.recv(1024)
            data_recv = data_recv.decode()
            print("Получено сообщение: ", data_recv)
            data_send = "Диалог"
            data_send = data_send.encode()
            self.sock.sendall(data_send)
            self.accept()
            print(123123)

    def accept(self):#добавить шифрование
        while True:
            data = input("Напишите сообщение: ")
            data_bytes = data.encode()
            self.sock.sendall(data_bytes)
            data_bytes = self.sock.recv(1024)
            data = data_bytes.decode()
            print("Получено сообщение: ", data)

    def fille_accept(self):#добавить шифрование
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

    def fille_send(self):#добавить шифрование
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


class Login_Window(QMainWindow):
    _login : QLineEdit
    _passw : QLineEdit
    _b1 : QPushButton
    # _db_name : QLineEdit

    def __init__(self):
        super().__init__()

        # logger.add("file_X.log", retention="10 days", format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")

        self.setGeometry(800, 300, 250, 200)
        self.setWindowIcon(QIcon('icon.png'))
        self._set_face()

    def _set_face(self):
        title = "Вход"
        self.setWindowTitle(title)

        v1 = QVBoxLayout()
        self._login = QLineEdit('root')
        self._passw = QLineEdit('11111111')
        self._passw.setEchoMode(QLineEdit.Password)
        # self._db_name = QLineEdit('mydata')
        self._b1 = QPushButton("Connect")
        self._b1.clicked.connect(self.activ_prot)

        v1.addWidget(self._login)
        v1.addWidget(self._passw)
        # v1.addWidget(self._db_name)
        v1.addWidget(self._b1)

        w = QWidget()
        w.setLayout(v1)
        self.setCentralWidget(w)

    def activ_prot(self):
        start_new_thread(prot_client, (self, ))
        print(222222222222222222222)
        # window.hide()
        # a = prot_client(self)



if __name__ == '__main__':
    # a = prot_client()

    app = QApplication(sys.argv)

    with open('style1.qss', 'r') as f:
        style = f.read()

    app.setStyleSheet(style)
    window = Login_Window()
    window.show()
    app.exec()