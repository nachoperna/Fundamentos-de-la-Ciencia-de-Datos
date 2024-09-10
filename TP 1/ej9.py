# Crear una clase Rectángulo con atributos de ancho y alto, y métodos para calcular su área y perímetro.

class Rectangulo:

    def __init__(self, x, y) -> None:
        self.ancho = x
        self.alto = y
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetero(self):
        return (self.ancho + self.alto) * 2
    
    def __str__(self) -> str:
        return f"\n-Alto: {self.alto} \n-Ancho: {self.ancho} \n-Area: {self.area()} \n-Perimetro: {self.perimetero()}"
    
r = Rectangulo(int(input("- Ancho: ")), int(input("- Alto: ")))

print(r)

