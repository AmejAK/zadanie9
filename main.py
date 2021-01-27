try:
    with open("plik_1.txt", 'r') as file_1:
        with open("plik_2.txt", 'w') as file_2:
            for linia in file_1:
                print(linia)
                file_2.write(linia)
except IOError as ioe:
    print("Bład".format(ioe))
