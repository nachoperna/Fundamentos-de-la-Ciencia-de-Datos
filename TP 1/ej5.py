# Escribir una función que determine si un número es par o impar.

num = int(input("Numero: "))

def es_par(num):
    return num%2 == 0

if (es_par(num)):
    resultado = "PAR"
else:
    resultado = "IMPAR"

print("El numero es " + resultado)