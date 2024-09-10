# Crear una función que devuelva la suma de dos números.

import numpy

num1 = int(input("- Numero 1: "))
num2 = int(input("- Numero 2: "))

def suma(num1, num2):
    return num1 + num2

resultado = suma(num1, num2)

print("La suma de " + str(num1) + " y " + str(num2) + " es: " + str(resultado))