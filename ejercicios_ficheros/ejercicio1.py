#!/usr/bin/env python3

def write_file(num):
    file = open("tabla-" + str(num) + ".txt", "w")
    
    for i in range(1, 10 + 1):
        file.write(str(num) + "X" + str(i) + "=" + str(int(num)*i) + "\n")

    file.close()
    
def read_file(num):
    file = open("tabla-" + str(num) + ".txt", "r")
    
    result = file.readlines()

    for i in range(len(result)):
        print(result[i] + "\n")

    file.close()


def write_file_xml(num):
    file = open("tabla-" + str(num) + ".xml", "w")

    file.write("<tabla>")
    
    for i in range(1, 10 + 1):
        file.write("<item>" + str(num) + "X" + str(i) + "=" + str(int(num)*i) + "</item>" + "\n")

    file.write("</tabla>")
    file.close()
#TODO falta desarrollar que lea XMLs
def read_file_xml(num):
    file = open("tabla-" + str(num) + ".xml", "r")
    
    result = file.readlines()

    for i in range(len(result)):
        print(result[i] + "\n")

    file.close()


#TODO falta desarrollar que lea y escriba JSONs

num: int = int(input("Introduce un numero entre 1 y 10\n"))

print("1. crear archivo\n")
print("2. leer archivo\n")

opcion = int(input("que opcion quieres ejecutar?\n"))

if opcion == 1:
    write_file_xml(num)
elif opcion == 2:
    read_file_xml(num)


