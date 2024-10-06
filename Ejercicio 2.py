while True:
    try:
        # Ingreso de las calificaciones
        grades_input = input("Ingrese una lista de calificaciones separadas por comas: ")

        #Dividir las calificaciones
        grades_str_list = grades_input.split(",")

        # Convierte cada calificación en un número decimal (float) y luego a entero
        grades = []
        for grade in grades_str_list:
            grade = float(grade)
            grade=int(grade)
            grades.append(grade)
        
        # Verificar que las calificaciones son validas
        print("Las calificaciones son:", grades)
        break

    except ValueError:
        print("Error: Por favor, ingrese solo números válidos separados por comas.")