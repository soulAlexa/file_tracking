filename = "test_ser2.docx"
file = open(filename, "rb")
file2 = open("test.txt", "w")
while True:
    file_data = file.read(36)
    file2.write(str(file_data))
    file2.write("\n")
    if not file_data:
        break
