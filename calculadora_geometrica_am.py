pi = 3.1416

# Controla cuando termina el programa
salir = False

# Menu - se repite hasta que el usuario decida salir
while salir == False:

    print("                 ")
    print("CALCULADORA GEOMETRICA AM")
    print("                 ")
    print("---FIGURAS 2D---")
    print("1. Triangulo")
    print("2. Circulo")
    print("3. Rectangulo")
    print("4. Triangulo rectangulo")
    print("5. Rombo")
    print("---FIGURAS 3D---")
    print("6. Cubo")
    print("7. Esfera")
    print("8. Cilindro")
    print("9. Piramide")
    print("                 ")
    print("0. Deseo salir...")
    print("                 ")

    # El usuario escoge figura
    try:
        opcion = int(input("Elige un numero para calcular la figura de preferencia: "))
    except ValueError:
        print("EHHH ingresa un caracter numerico, intentalo nuevamente...")
        opcion = 20

    # Calculo del triangulo
    if opcion == 1:

        valido = True

        try:
            base = float(input("Ingresa el numero de la base: "))
            if base <= 0:
                print("La base no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un numero valido")
            valido = False

        try:
            altura = float(input("Ingresa el numero de la altura: "))
            if altura <= 0:
                print("La altura no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un numero valido")
            valido = False

        try:
            lado1 = float(input("Ingresa un numero para el lado 1: "))
            if lado1 <= 0:
                print("El lado no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un numero valido")
            valido = False

        try:
            lado2 = float(input("Ingresa un numero para el lado 2: "))
            if lado2 <= 0:
                print("El lado no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un numero valido")
            valido = False

        try:
            lado3 = float(input("Ingresa un numero para el lado 3: "))
            if lado3 <= 0:
                print("El lado no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un numero valido")
            valido = False

        try:
            angulo1 = float(input("Ingresa un numero para el angulo 1: "))
            if angulo1 <= 0:
                print("El angulo no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un numero valido")
            valido = False

        try:
            angulo2 = float(input("Ingresa un numero para el angulo 2: "))
            if angulo2 <= 0:
                print("El angulo no puede ser cero o negativo")
                valido = False
            elif angulo1 + angulo2 >= 180:
                print("Los angulos no pueden sumar 180 o mas")
                valido = False
        except ValueError:
            print("Ingresa un numero valido")
            valido = False

        if valido == True:
            area = (base * altura) / 2
            perimetro = lado1 + lado2 + lado3
            angulo3 = 180 - angulo1 - angulo2
            print(f"Area: {area}")
            print(f"Perimetro: {perimetro}")
            print(f"Angulo faltante: {angulo3}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del circulo
    elif opcion == 2:

        valido = True

        try:
            radio = float(input("Ingresa el radio: "))
            if radio <= 0:
                print("El radio no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            area = pi * radio ** 2
            perimetro = 2 * pi * radio
            print(f"Area: {area}")
            print(f"Perimetro: {perimetro}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del rectangulo
    elif opcion == 3:

        valido = True

        try:
            base = float(input("Ingresa un numero para calcular la base: "))
            if base <= 0:
                print("La base no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        try:
            altura = float(input("Ingresa un numero para calcular la altura: "))
            if altura <= 0:
                print("La altura no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            area = base * altura
            perimetro = 2 * (base + altura)
            print(f"Area: {area}")
            print(f"Perimetro: {perimetro}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del triangulo rectangulo
    elif opcion == 4:

        valido = True

        try:
            base = float(input("Ingresa un numero para calcular la base: "))
            if base <= 0:
                print("La base no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        try:
            altura = float(input("Ingresa un numero para calcular la altura: "))
            if altura <= 0:
                print("La altura no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        try:
            angulo1 = float(input("Ingresa un numero para calcular el angulo 1: "))
            if angulo1 <= 0:
                print("El angulo no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        try:
            angulo2 = float(input("Ingresa un numero para calcular el angulo 2: "))
            if angulo2 <= 0:
                print("El angulo no puede ser cero o negativo")
                valido = False
            elif angulo1 + angulo2 >= 180:
                print("Los angulos no pueden sumar 180 o mas")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            area = (base * altura) / 2
            hipotenusa = (base ** 2 + altura ** 2) ** 0.5
            angulo3 = 180 - angulo1 - angulo2
            print(f"Area: {area}")
            print(f"Hipotenusa: {hipotenusa}")
            print(f"Angulo faltante: {angulo3}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del rombo
    elif opcion == 5:

        valido = True

        try:
            diagonal1 = float(input("Ingresa un numero para la diagonal 1: "))
            if diagonal1 <= 0:
                print("La diagonal no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        try:
            diagonal2 = float(input("Ingresa un numero para la diagonal 2: "))
            if diagonal2 <= 0:
                print("La diagonal no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            area = (diagonal1 * diagonal2) / 2
            perimetro = 2 * (diagonal1 ** 2 + diagonal2 ** 2) ** 0.5
            print(f"Area: {area}")
            print(f"Perimetro: {perimetro}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del cubo
    elif opcion == 6:

        valido = True

        try:
            lado = float(input("Ingresa un numero para calcular el lado: "))
            if lado <= 0:
                print("El lado no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            area = 6 * lado ** 2
            volumen = lado ** 3
            print(f"Area: {area}")
            print(f"Volumen: {volumen}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo de la esfera
    elif opcion == 7:

        valido = True

        try:
            radio = float(input("Ingresa un numero para calcular el radio: "))
            if radio <= 0:
                print("El radio no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            area = 4 * pi * radio ** 2
            volumen = (4/3) * pi * radio ** 3
            print(f"Area: {area}")
            print(f"Volumen: {volumen}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del cilindro
    elif opcion == 8:

        valido = True

        try:
            radio = float(input("Ingresa un numero para calcular el radio: "))
            if radio <= 0:
                print("El radio no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        try:
            altura = float(input("Ingresa un numero para calcular la altura: "))
            if altura <= 0:
                print("La altura no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            area = 2 * pi * radio * (radio + altura)
            volumen = pi * radio ** 2 * altura
            print(f"Area: {area}")
            print(f"Volumen: {volumen}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo de la piramide
    elif opcion == 9:

        valido = True

        try:
            base = float(input("Ingresa un numero para calcular la base: "))
            if base <= 0:
                print("La base no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        try:
            altura = float(input("Ingresa un numero para calcular la altura: "))
            if altura <= 0:
                print("La altura no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            area = base ** 2 + 2 * base * altura
            volumen = (base ** 2 * altura) / 3
            print(f"Area: {area}")
            print(f"Volumen: {volumen}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Salir del programa
    elif opcion == 0:
        print("Saliendo, espero verte pronto...")
        salir = True

    # Si el usuario escribe un numero invalido
    else:
        print("Ingresa un valor numerico valido")
        