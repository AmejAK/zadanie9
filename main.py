try:
    with open("plik_1.txt", 'r') as file1:
        with open("plik_2.txt", 'w') as file2:
            for lin in file1:
                file2.write(lin)
except IOError as ioe:
    print("Bład".format(ioe))