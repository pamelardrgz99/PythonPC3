class Producto:
    def __init__(self, nombre, precio, anio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.anio = anio
        self.categoria = categoria

    def __str__(self):
        return f"producto {self.nombre} con Precio {self.precio} del Anio {self.anio} y con Categoría {self.categoria}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_anio(self, anio):
        filtrados = [producto for producto in self.productos if producto.anio == anio]
        return filtrados

    def buscar_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos if nombre in producto.nombre]
        return encontrados

# Crear objetos
producto1 = Producto("filtro de aire", 25, 2023, "Filtros")
producto2 = Producto("aceite de motor", 45, 2024, "Aceites")
producto3 = Producto("bateria", 1000, 2023, "Baterías")

catalogo = Catalogo()

# Agregar producto
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

# Mostrar todos los productos en el catálogo
print("Lista completa de productos en el catalogo:")
catalogo.mostrar_productos()

# Filtrar productos por año
print("\nProductos del anio 2023:")
productos_2023 = catalogo.filtrar_por_anio(2023)
for producto in productos_2023:
    print(producto)

# Buscar productos por nombre
print("\nBúsqueda de productos con 'bateria' en el nombre:")
productos_bateria= catalogo.buscar_por_nombre("bateria")
for producto in productos_bateria:
    print(producto)
