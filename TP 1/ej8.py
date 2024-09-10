# Crear una función que reciba una cadena y devuelva True si es un palíndromo. 
# Recordar que un palíndromo es aquella palabra que, espejada, se sigue leyendo igual (por ejemplo, neuquen).

def palindromo(pal):
    i = 0
    j = len(pal) - 1
    while (i != j):
        if (pal[i] == pal[j]):
            i+=1
            j-=1
        else:
            return False
    return True

def menu():
    opcion = 0
    while opcion != 2:
        print("\n1. Palindromear \n2. Salir")
        opcion = int(input("- Opcion: "))
        
        if opcion == 1:
            palabra = input("\n- Palabra: ")
            print(palindromo(palabra))

menu()