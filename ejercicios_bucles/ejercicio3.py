#!/usr/bin/env python3

usr_intr_num = int(input('Introduce un numero entero\n'))

i: int = 0

while(i < usr_intr_num):
    if i%2 != 0:
        print(i)
    i = i + 1