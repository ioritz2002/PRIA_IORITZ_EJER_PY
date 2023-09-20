#!/usr/bin/env python3

frutas = {'platano': 1.35, 'manzana': 0.80, 'pera':0.85, 'naranja': 0.70}

nom_fruta = input("¿Que fruta buscas?\n")
num_fruta = 0
precio = 0.0

if nom_fruta in frutas:
    num_fruta = int(input("¿Cuantas unidades quieres?\n"))
    precio = frutas[nom_fruta] * num_fruta

    print("El precio de " + str(num_fruta) + " de kilos de " + nom_fruta +" cuesta " + str(precio))
    pass
else:
    print("No tenemos la fruta que busca\n")
