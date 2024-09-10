# Crear una lista de 5 frutas y escribir un bucle que las imprima una por una.

frutas = {}

def inic(frutas):
    for i in range (5):
        frutas[i] = input("Fruta " + str((i+1)) + ": ")

inic(frutas)

def show(frutas):
    for i in range(5):
        print("Fruta " + str((i+1)) + ": " + frutas[i])

print("--------------")
show(frutas)