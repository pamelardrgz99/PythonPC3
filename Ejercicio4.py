class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        # Llama al constructor de la clase base (RECTANGULO) con largo y ancho iguales
        super().__init__(lado, lado)

# Crear los dos objetos
rectangulo = RECTANGULO(4, 10)
cuadrado = CUADRADO(4)

# Mostrar el área de cada figura
print(f"Rectángulo de largo {rectangulo.largo} y ancho {rectangulo.ancho} con un área de {rectangulo.calcular_area()}")
print(f"Cuadrado de lado {cuadrado.largo} con un área de {cuadrado.calcular_area()}")
