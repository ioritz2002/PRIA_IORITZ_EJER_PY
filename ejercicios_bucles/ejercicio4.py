#!/usr/bin/env python3

num = int(input("Introduce un numero entero positivo\n"))
text = " "
while num >= 0:
    text = text + str(num) + ","
    num = num - 1

print(text)