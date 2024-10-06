
def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        return a / b
    except TypeError:
        return "Error: Tipo de dato no valido"
    except ZeroDivisionError:
        return "Error: No es posible dividir entre 0"
