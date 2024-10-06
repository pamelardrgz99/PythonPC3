while True:
    try:
        #Ingresar la fraccion solicitada
        fraction = input("Ingrese la fracción de combustible (X/Y): ")

        x_str, y_str = fraction.split("/")

        # Verificar que los valores ingresados sean enteros
        if not x_str.isdigit() or not y_str.isdigit():
            raise ValueError("Error dado que solo se permiten números enteros")

        x = int(x_str)
        y = int(y_str)

        # Verificar que Y es diferente de 0
        if y == 0:
            raise ZeroDivisionError("Error, ZeroDivisionError")
        
        # Verificar que X/Y es menor a 1
        if x > y:
            raise ValueError("Error, Volver a preguntar al usuario")
        
        # Calculo el porcentaje de combustible
        percentage = (x / y) * 100
        rounded_percentage = round(percentage)
        
        # Determina el estado del tanque
        if rounded_percentage < 1:
            print("E")
        elif rounded_percentage > 99:
            print("F")
        else:
            print(f"{rounded_percentage}%")
        break
    
    except ValueError as error_valor:
        print(f"{error_valor}")
    except ZeroDivisionError as error_zero:
        print(f"{error_zero}")
