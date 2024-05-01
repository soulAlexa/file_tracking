# import socket
# from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
# from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget, QListView
# import sys
# from _thread import *
# from PyQt5 import QtCore
#
# class Login_Window(QMainWindow):
#     _login : QLineEdit
#     _passw : QLineEdit
#     _b1 : QPushButton
#
#     def __init__(self):
#         super().__init__()
#         # logger.add("file_X.log", retention="10 days", format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")
#         self.setGeometry(800, 300, 250, 200)
#         self.setWindowIcon(QIcon('icon.png'))
#         self._set_face()
#
#     def _set_face(self):
#         title = "Вход"
#         self.setWindowTitle(title)
#         v1 = QVBoxLayout()
#         self._login = QLineEdit('root')
#         self._passw = QLineEdit('11111111')
#         self._passw.setEchoMode(QLineEdit.Password)
#         self._b1 = QPushButton("Connect")
#         self._b1.clicked.connect(self.activ_prot)
#         v1.addWidget(self._login)
#         v1.addWidget(self._passw)
#         v1.addWidget(self._b1)
#         w = QWidget()
#         w.setLayout(v1)
#         self.setCentralWidget(w)
#
#     def activ_prot(self):
#         # _window2 = Main_Window()
#         start_new_thread(prot_client, (self, ))
#         # window.hide()
#         print(222222222222222222222)
#         # a = prot_client(self)
#
#
# class Main_Window(QMainWindow):
#     _b1: QPushButton
#     _b2: QPushButton
#     _b3: QPushButton
#
#     def __init__(self):
#         super().__init__()
#
#         self.setGeometry(800, 300, 600, 400)
#         self.setWindowIcon(QIcon('icon.png'))
#         self._set_face()
#
#
#     def _set_face(self):
#         title = "Файловая система"
#         self.setWindowTitle(title)
#         self.vie = QListView()
#         # self.vie.clicked.connect(self.activ_prot)
#         v1 = QVBoxLayout()
#         self._b1 = QPushButton("Get_File")
#         self._b2 = QPushButton("Push_File")
#         self._b3 = QPushButton("Push_New_File")
#         self._b1.clicked.connect(prot_client.fille_accept)
#         self._b2.clicked.connect(self.activ_prot)
#         # self._b3.clicked.connect(self.activ_prot)
#         v1.addWidget(self._b1)
#         v1.addWidget(self._b2)
#         v1.addWidget(self._b3)
#         v1.addWidget(self.vie)
#         w = QWidget()
#         w.setLayout(v1)
#         self.setCentralWidget(w)
#
#     def _set_list(self, fille_list):
#         entries = list(fille_list.split(","))
#         print(entries)
#         model = QStandardItemModel()
#         self.vie.setModel(model)
#         for i in entries:
#             item = QStandardItem(i)
#             model.appendRow(item)
#
#
#     def activ_prot(self):
#         current_index = self.vie.currentIndex()
#         item = current_index.data(QtCore.Qt.DisplayRole)
#         print(item)
#         return item
#
#
#
# class prot_client():
#     def __init__(self, window):
#         HOST = '127.0.0.1'
#         PORT = 2000
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.sock.connect((HOST, PORT))
#         # self.authorization_con()
#         self.management()
#         print("3234234")
#
#     def authorization_con(self):#добавить шифрование
#         data_send = str((window._login.text(), window._passw.text()))
#         # print(data_send)
#         data_send = data_send.encode()
#         self.sock.sendall(data_send)
#         data_recv = self.sock.recv(2)
#         data_recv = int.from_bytes(data_recv, 'little', signed=True)
#         print(data_recv)
#         if data_recv > 0:
#             return True
#         else:
#             return False
#
#     def management(self):#добавить шифрование
#         if self.authorization_con():
#             window.hide()
#             window2.show()
#         else:
#             exit_thread()
#         data_recv = self.sock.recv(1024)
#         data_recv = data_recv.decode()
#         window2._set_list(data_recv)
#         # window2._b1.clicked.connect(self.accept)
#         while True:
#             window2._b1.clicked.connect(self.fille_accept)
#             window2._b2.clicked.connect(self.fille_send)
#             # window2._b3.clicked.connect(self.accept)
#             # data_recv = self.sock.recv(1024)
#             # data_recv = data_recv.decode()
#             # print("Получено сообщение: ", data_recv)
#             # data_send = "Диалог"
#             # data_send = data_send.encode()
#             # self.sock.sendall(data_send)
#             # self.accept()
#             # print(123123)
#
#     def accept(self):#добавить шифрование
#
#         while True:
#             data = input("Напишите сообщение: ")
#             data_bytes = data.encode()
#             self.sock.sendall(data_bytes)
#             data_bytes = self.sock.recv(1024)
#             data = data_bytes.decode()
#             print("Получено сообщение: ", data)
#
#     def fille_accept(self):#добавить шифрование
#         data_send = f"Get_File,{window2.activ_prot()}"
#         print(data_send)
#         data_send = data_send.encode()
#         self.sock.sendall(data_send)
#         filename = window2.activ_prot()
#         file = open(filename, "wb")
#         size_fill = 0
#         size = 0
#         while True:
#             if size_fill == 0:
#                 f = self.sock.recv(8)
#                 size_fill = int.from_bytes(f, 'big')
#                 continue
#             size += 4096
#             if size > size_fill:
#                 file_data = self.sock.recv(size - size_fill)
#                 file.write(file_data)
#                 file.close()
#                 print("fille accepted")
#                 break
#             else:
#                 file_data = self.sock.recv(4096)
#             file.write(file_data)
#
#     def fille_send(self):#добавить шифрование
#         filename = "server.docx"
#         file = open(filename, "rb")
#         byte_len = (len(file.read())).to_bytes(8, 'big')
#         self.sock.sendall(byte_len)
#         file.seek(0)
#         while True:
#             file_data = file.read(4096)
#             self.sock.send(file_data)
#             if not file_data:
#                 break
#         print("file sended")
#
#
#
#
#
#
# if __name__ == '__main__':
#     # a = prot_client()
#     app = QApplication(sys.argv)
#     with open('style1.qss', 'r') as f:
#         style = f.read()
#     app.setStyleSheet(style)
#     window2 = Main_Window()
#     window2.show()
#     window2.hide()
#     window = Login_Window()
#     window.show()
#     app.exec()


import socket
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget, QListView
import sys
from _thread import *
from PyQt5 import QtCore
from pywinauto import *
import time



class Main_Window(QMainWindow):
    _b1: QPushButton
    _b2: QPushButton
    _b3: QPushButton

    def __init__(self):
        super().__init__()

        self.setGeometry(800, 300, 600, 400)
        self.setWindowIcon(QIcon('icon.png'))
        HOST = '127.0.0.1'
        PORT = 2000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        self._window = self.Login_Window(self)
        self._window.show()
        self._window._b0.clicked.connect(self.management)
        # self._set_face()
        title = "Файловая система"
        self.setWindowTitle(title)
        self.vie = QListView()
        # self.vie.clicked.connect(self.activ_prot)
        v1 = QVBoxLayout()
        self._b1 = QPushButton("Get_File")
        self._b2 = QPushButton("Push_File")
        self._b3 = QPushButton("Push_New_File")
        self._b1.clicked.connect(self.fille_accept)
        self._b2.clicked.connect(self.activ_prot)
        # self._b3.clicked.connect(self.activ_prot)
        v1.addWidget(self._b1)
        v1.addWidget(self._b2)
        v1.addWidget(self._b3)
        v1.addWidget(self.vie)
        w = QWidget()
        w.setLayout(v1)
        self.setCentralWidget(w)

    class Login_Window(QMainWindow):
        _login: QLineEdit
        _passw: QLineEdit
        _b0: QPushButton

        def __init__(self, parent):
            super().__init__(parent=parent)
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
            self._b0 = QPushButton("Connect")
            # self._b0.clicked.connect(self.activ_prot)
            v1.addWidget(self._login)
            v1.addWidget(self._passw)
            v1.addWidget(self._b0)
            w = QWidget()
            w.setLayout(v1)
            self.setCentralWidget(w)

    def authorization_con(self):  # добавить шифрование
        data_send = str((self._window._login.text(), self._window._passw.text()))
        # print(data_send)
        data_send = data_send.encode()
        self.sock.sendall(data_send)
        data_recv = self.sock.recv(2)
        data_recv = int.from_bytes(data_recv, 'little', signed=True)
        print(data_recv)
        if data_recv > 0:
            return True
        else:
            return False

    def management(self):  # добавить шифрование
        if self.authorization_con():
            self._window.close()
            self.show()
        else:
            return
        data_recv = self.sock.recv(1024)
        data_recv = data_recv.decode()
        self._set_list(data_recv)

    def accept(self):  # добавить шифрование
        while True:
            data = input("Напишите сообщение: ")
            data_bytes = data.encode()
            self.sock.sendall(data_bytes)
            data_bytes = self.sock.recv(1024)
            data = data_bytes.decode()
            print("Получено сообщение: ", data)

    def fille_accept(self):  # добавить шифрование
        data_send = f"Get_File,{self.activ_prot()}"
        print(data_send)
        data_send = data_send.encode()
        self.sock.sendall(data_send)
        filename = self.activ_prot()
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
                start_new_thread(self.see_you, (filename, ))
                break
            else:
                file_data = self.sock.recv(4096)
            file.write(file_data)

    def fille_send(self):  # добавить шифрование
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
    # def _set_face(self):
    #     title = "Файловая система"
    #     self.setWindowTitle(title)
    #     self.vie = QListView()
    #     # self.vie.clicked.connect(self.activ_prot)
    #     v1 = QVBoxLayout()
    #     self._b1 = QPushButton("Get_File")
    #     self._b2 = QPushButton("Push_File")
    #     self._b3 = QPushButton("Push_New_File")
    #     self._b1.clicked.connect()
    #     self._b2.clicked.connect(self.activ_prot)
    #     # self._b3.clicked.connect(self.activ_prot)
    #     v1.addWidget(self._b1)
    #     v1.addWidget(self._b2)
    #     v1.addWidget(self._b3)
    #     v1.addWidget(self.vie)
    #     w = QWidget()
    #     w.setLayout(v1)
    #     self.setCentralWidget(w)

    def _set_list(self, fille_list):
        entries = list(fille_list.split(","))
        print(entries)
        model = QStandardItemModel()
        self.vie.setModel(model)
        for i in entries:
            item = QStandardItem(i)
            model.appendRow(item)

    def activ_prot(self):
        current_index = self.vie.currentIndex()
        item = current_index.data(QtCore.Qt.DisplayRole)
        print(item)
        return item

    def see_you(self, fill_name):
        program_path = r"C:/Program Files/Microsoft Office/root/Office16/WINWORD.exe"
        file_path = f"{fill_name}"
        appl = Application(backend="uia").start(r'{} "{}"'.format(program_path, file_path))
        dlg = appl.window(title=f"{fill_name} - Word")
        while True:
            time.sleep(10)
            dlg.SaveButton.click()
            if self._b3.clicked:
                appl.kill()
                break


# class prot_client():
#     def __init__(self, window):
#         HOST = '127.0.0.1'
#         PORT = 2000
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.sock.connect((HOST, PORT))
#         # self.authorization_con()
#         self.management()
#         print("3234234")
#
#     def authorization_con(self):#добавить шифрование
#         data_send = str((window._login.text(), window._passw.text()))
#         # print(data_send)
#         data_send = data_send.encode()
#         self.sock.sendall(data_send)
#         data_recv = self.sock.recv(2)
#         data_recv = int.from_bytes(data_recv, 'little', signed=True)
#         print(data_recv)
#         if data_recv > 0:
#             return True
#         else:
#             return False
#
#     def management(self):#добавить шифрование
#         if self.authorization_con():
#             window.hide()
#             window2.show()
#         else:
#             exit_thread()
#         data_recv = self.sock.recv(1024)
#         data_recv = data_recv.decode()
#         window2._set_list(data_recv)
#         # window2._b1.clicked.connect(self.accept)
#         while True:
#             window2._b1.clicked.connect(self.fille_accept)
#             window2._b2.clicked.connect(self.fille_send)
#             # window2._b3.clicked.connect(self.accept)
#             # data_recv = self.sock.recv(1024)
#             # data_recv = data_recv.decode()
#             # print("Получено сообщение: ", data_recv)
#             # data_send = "Диалог"
#             # data_send = data_send.encode()
#             # self.sock.sendall(data_send)
#             # self.accept()
#             # print(123123)
#
#     def accept(self):#добавить шифрование
#
#         while True:
#             data = input("Напишите сообщение: ")
#             data_bytes = data.encode()
#             self.sock.sendall(data_bytes)
#             data_bytes = self.sock.recv(1024)
#             data = data_bytes.decode()
#             print("Получено сообщение: ", data)
#
#     def fille_accept(self):#добавить шифрование
#         data_send = f"Get_File,{window2.activ_prot()}"
#         print(data_send)
#         data_send = data_send.encode()
#         self.sock.sendall(data_send)
#         filename = window2.activ_prot()
#         file = open(filename, "wb")
#         size_fill = 0
#         size = 0
#         while True:
#             if size_fill == 0:
#                 f = self.sock.recv(8)
#                 size_fill = int.from_bytes(f, 'big')
#                 continue
#             size += 4096
#             if size > size_fill:
#                 file_data = self.sock.recv(size - size_fill)
#                 file.write(file_data)
#                 file.close()
#                 print("fille accepted")
#                 break
#             else:
#                 file_data = self.sock.recv(4096)
#             file.write(file_data)
#
#     def fille_send(self):#добавить шифрование
#         filename = "server.docx"
#         file = open(filename, "rb")
#         byte_len = (len(file.read())).to_bytes(8, 'big')
#         self.sock.sendall(byte_len)
#         file.seek(0)
#         while True:
#             file_data = file.read(4096)
#             self.sock.send(file_data)
#             if not file_data:
#                 break
#         print("file sended")



if __name__ == '__main__':
    # a = prot_client()
    app = QApplication(sys.argv)
    with open('style1.qss', 'r') as f:
        style = f.read()
    app.setStyleSheet(style)

    window2 = Main_Window()
    # window.show()
    # window2 = Main_Window(window)
    window2.show()
    window2.hide()
    app.exec()