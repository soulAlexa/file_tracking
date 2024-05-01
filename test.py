from pywinauto import *
import os
import win32com.client as win32
import time

# def open_fil():
#     fill = open("test____.txt", "r")
#     str_original = fill.readline()
#     str_dell = fill.readline()
#     str_add = fill.readline()
#     fill.close()
#     return str_original, str_dell, str_add
#
# def test_dell(str_original, str_chan):
#     i = 0
#     T = False
#     while True:
#         if i > len(str_original) or i > len(str_chan):
#             break
#         if str_original[i] == str_chan[i]:
#             i += 1
#             continue
#         T = True
#         j = i
#         while T:
#             if str_original[j] == str_chan[j]:
#                 T = False
#                 print(i, j-i)
#                 i = j
#             j += 1
#
#         # test_dell(str_original[i:], str_chan[i:])
#         i += 1


if __name__ == '__main__':
    # str_original, str_dell, str_add = open_fil()
    # test_dell(str_original, str_dell)

    # app = Application(backend="uia")
    # app.start("notepad.exe")
    # app.Notepad.edit1.SetText("skdjfns")
    #
    program_path = r"C:/Program Files/Microsoft Office/root/Office16/WINWORD.exe"
    file_path = r"server.docx"
    app = Application(backend="uia").start(r'{} "{}"'.format(program_path, file_path))
    dlg = app.window(title="server.docx - Word")
    # h1 = dlg.wrapper_object()
    # print(h1)
    # dlg.menu_select("File->Save")
    time.sleep(5)
    dlg.SaveButton.click()
    app.kill()
    # app.ServerWord.menu_select("File->SaveAs")
    # app.SaveAs.ComboBox5.select("UTF-8")
    # app.SaveAs.edit1.set_text("Example-utf8.docx")
    # app.SaveAs.Save.click()
    # dlg = app['server.docx-WordDialog']
    # dlg2 = app['server. - fghfgh']
    # print(dlg2)
    # app.connect(path=program_path)
    # app.Word.edit1.SetText("pfsdksdjbn")


    # word = win32.D
