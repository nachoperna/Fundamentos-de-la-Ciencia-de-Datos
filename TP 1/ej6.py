# Crear un diccionario con nombres de estudiantes y sus notas. Imprimir el promedio de esas notas.

diccionario = []

def carga_dic(diccionario, alumno):
    diccionario.append(alumno)

def carga_alumno():
    nombre = input("Nombre del alumno: ")
    nota = int(input("Nota del alumno: "))
    return (nombre,nota) #se puede simplificar en una sola linea

def promedio(diccionario):
    suma = 0
    for alumno in diccionario:
        suma += alumno[1]
    return suma/len(diccionario)

def buscar(diccionario, buscado):
    for alumno in diccionario:
        if (buscado in alumno):
            return alumno
    return False

def menu(diccionario):
    opcion = 0
    while (opcion != 4):
        print("\n")
        print("1. Cargar alumno.")
        print("2. Buscar alumno.")
        print("3. Ver promedio de notas.")
        print("4. Salir.")
        opcion = int(input("- Opcion: "))

        if (opcion == 1):
            carga_dic(diccionario, carga_alumno())

        elif(opcion == 2):
            nombre = input("\nNombre del alumno a buscar: ")
            alum = buscar(diccionario, nombre)
            if alum != False:
                print("\n- Alumno: " + alum[0] + " / Nota: " + str(alum[1]) + " -")
            else:
                print("\n- Alumno no encontrado. -")
                
        elif(opcion == 3):
            print("\n- El promedio de las notas es: " + str(promedio(diccionario)) + " -")

menu(diccionario)