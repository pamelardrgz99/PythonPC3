class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)

    def info(self):
        area = self.calcular_area()
        print(f"Círculo de radio {self.radio} y área {area:.2f}")

# Crear dos objetos de tipo CIRCULO
circulo1 = CIRCULO(5)
circulo2 = CIRCULO(10)

# Mostrar los resultados
circulo1.info()
circulo2.info()