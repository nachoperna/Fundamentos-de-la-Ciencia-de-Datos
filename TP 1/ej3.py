# Escribir un programa que calcule el área de un círculo dado su radio.

import numpy

radio = int(input("Introduzca el radio del circulo: "))

def area(radio):
    return numpy.pi * pow(radio, 2)

resultado = area(radio)

print("El area del circulo es: ", resultado)
