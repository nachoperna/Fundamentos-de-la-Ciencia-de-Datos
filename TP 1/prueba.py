"""

Ejemplo 1 - Python Scripting

Este archivo es un ejemplo de un script de Python que se puede ejecutar desde la terminal.


Fundamentos de Ciencia de Datos
Ingeniería de Sistemas - Facultad de Ciencias Exactas - UNICEN

"""

# los imports se colocan siempre arriba
import numpy as np

# las funciones, clases y demás recursos se colocan debajo de los imports
def saludar(persona):
    print(f"Hola {persona}!")

# la lógica principal del script se suele colcoar debajo de las funciones
if __name__ == "__main__":
    saludar("Mundo")