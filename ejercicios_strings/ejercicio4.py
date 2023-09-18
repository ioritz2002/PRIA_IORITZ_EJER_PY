#!/usr/bin/env python3

import re

def valid_phone(phone,regex):
    if re.fullmatch(regex, phone):
        return True
    return False

def no_prefix(phone):
    splited_number = phone.split("-")
    no_prefix_phone = splited_number[1]
    return no_prefix_phone


validation_regex = "^[+][0-9]{2}-[0-9]{9}-[0-9]{2}$"
pattern = re.compile(validation_regex)


complete_phone_num = input('Introduce el numero de telefono\n')

if valid_phone(complete_phone_num,pattern):
    print(no_prefix(complete_phone_num))
else:
    print("El numero de telefono es erroneo")
