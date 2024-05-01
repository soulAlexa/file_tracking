# import difflib
# from difflib import Differ
# filename = "server.docx"
# file = open(filename, "rb")
# file2 = open("test_client2.docx", "rb")
# i = 0
# mass = []
# mass2 = []
# while True:
#     file_data = file.readline()
#     if not file_data:
#         break
#     i += 1
#     mass.append(file_data)
# print(i)
# i = 0
# while True:
#     file_data = file2.readline()
#     if not file_data:
#         break
#     i += 1
#     mass2.append(file_data)
# print(i)
#
# # differ = Differ()
# # diff = list(differ.compare(mass, mass2))
# diff = difflib.diff_bytes(difflib.unified_diff, mass, mass2, fromfile=b'before.py', tofile=b'after.py')
# # print(len(diff))
# for line in diff:
#     print(line)
# from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
# from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget, QListView
# import sys
# from PyQt5 import QtCore
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
#         # logger.add("file_X.log", retention="10 days", format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")
#
#         self.setGeometry(800, 300, 600, 400)
#         self.setWindowIcon(QIcon('icon.png'))
#         self._set_face()
#
#     def _set_face(self):
#         title = "Файловая система"
#         self.setWindowTitle(title)
#         self.vie = QListView()
#         entries = ['one', 'two', 'three']
#         model = QStandardItemModel()
#         self.vie.setModel(model)
#         for i in entries:
#             item = QStandardItem(i)
#             model.appendRow(item)
#         self.vie.clicked.connect(self.activ_prot)
#         v1 = QVBoxLayout()
#         self._b1 = QPushButton("Get_File")
#         self._b1.clicked.connect(self.activ_prot)
#         self._b2 = QPushButton("Push_File")
#         self._b2.clicked.connect(self.activ_prot)
#         self._b3 = QPushButton("Push_New_File")
#         self._b3.clicked.connect(self.activ_prot)
#         v1.addWidget(self._b1)
#         v1.addWidget(self._b2)
#         v1.addWidget(self._b3)
#         v1.addWidget(self.vie)
#         w = QWidget()
#         w.setLayout(v1)
#         self.setCentralWidget(w)
#
#     def activ_prot(self):
#         current_index = self.vie.currentIndex()
#         item = current_index.data(QtCore.Qt.DisplayRole)
#         print(item)
#
#
#
#
# if __name__ == '__main__':
#     # a = prot_client()
#
#     app = QApplication(sys.argv)
#
#     with open('style1.qss', 'r') as f:
#         style = f.read()
#
#     app.setStyleSheet(style)
#     window = Main_Window()
#     window.show()
#     app.exec()

import os
from os.path import isdir


def parse_folder(path):
    files = ""
    for file in os.listdir(path):
        # if isdir(path + '/' + file):
        #     files.extend(parse_folder(path + '/' + file))
        # else:
        files += file + ","
    return files


print(parse_folder(r"C:\Test_for_fill_track"))
