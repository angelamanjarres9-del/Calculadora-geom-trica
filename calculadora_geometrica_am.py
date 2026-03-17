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

        print("                 ")
        print("--- TRIANGULO ---")
        print("¿Que deseas calcular?")
        print("1. Area")
        print("2. Perimetro")
        print("3. Angulo faltante")
        print("4. Todo")

        try:
            calculo = int(input("Elige una opcion: "))
        except ValueError:
            print("Opcion invalida")
            calculo = 0

        valido = True

        if calculo == 1 or calculo == 4:
            try:
                base = float(input("Base del triangulo: "))
                if base <= 0:
                    print("La base no puede ser cero o negativa")
                    valido = False
            except ValueError:
                print("Ingresa un numero valido")
                valido = False

            try:
                altura = float(input("Altura del triangulo: "))
                if altura <= 0:
                    print("La altura no puede ser cero o negativa")
                    valido = False
            except ValueError:
                print("Ingresa un numero valido")
                valido = False

        if calculo == 2 or calculo == 4:
            try:
                lado1 = float(input("Lado 1 del triangulo: "))
                if lado1 <= 0:
                    print("El lado no puede ser cero o negativo")
                    valido = False
            except ValueError:
                print("Ingresa un numero valido")
                valido = False

            try:
                lado2 = float(input("Lado 2 del triangulo: "))
                if lado2 <= 0:
                    print("El lado no puede ser cero o negativo")
                    valido = False
            except ValueError:
                print("Ingresa un numero valido")
                valido = False

            try:
                lado3 = float(input("Lado 3 del triangulo: "))
                if lado3 <= 0:
                    print("El lado no puede ser cero o negativo")
                    valido = False
            except ValueError:
                print("Ingresa un numero valido")
                valido = False

        if calculo == 3 or calculo == 4:
            try:
                angulo1 = float(input("Angulo 1 del triangulo (en grados): "))
                if angulo1 <= 0:
                    print("El angulo no puede ser cero o negativo")
                    valido = False
            except ValueError:
                print("Ingresa un numero valido")
                valido = False

            try:
                angulo2 = float(input("Angulo 2 del triangulo (en grados): "))
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
            if calculo == 1 or calculo == 4:
                # Formula area: (base x altura) / 2
                area = (base * altura) / 2
                print(f"Area: {area}")
            if calculo == 2 or calculo == 4:
                # Formula perimetro: suma de los 3 lados
                perimetro = lado1 + lado2 + lado3
                print(f"Perimetro: {perimetro}")
            if calculo == 3 or calculo == 4:
                # Formula angulo faltante: 180 - angulo1 - angulo2
                angulo3 = 180 - angulo1 - angulo2
                print(f"Angulo faltante: {angulo3} grados")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del circulo
    elif opcion == 2:

        print("                 ")
        print("--- CIRCULO ---")
        print("¿Que deseas calcular?")
        print("1. Area")
        print("2. Perimetro")
        print("3. Todo")

        try:
            calculo = int(input("Elige una opcion: "))
        except ValueError:
            print("Opcion invalida")
            calculo = 0

        valido = True

        try:
            radio = float(input("Radio del circulo: "))
            if radio <= 0:
                print("El radio no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            if calculo == 1 or calculo == 3:
                # Formula area: pi x radio²
                area = pi * radio ** 2
                print(f"Area: {area}")
            if calculo == 2 or calculo == 3:
                # Formula perimetro: 2 x pi x radio
                perimetro = 2 * pi * radio
                print(f"Perimetro: {perimetro}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del rectangulo
    elif opcion == 3:

        print("                 ")
        print("--- RECTANGULO ---")
        print("¿Que deseas calcular?")
        print("1. Area")
        print("2. Perimetro")
        print("3. Todo")

        try:
            calculo = int(input("Elige una opcion: "))
        except ValueError:
            print("Opcion invalida")
            calculo = 0

        valido = True

        try:
            base = float(input("Base del rectangulo: "))
            if base <= 0:
                print("La base no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        try:
            altura = float(input("Altura del rectangulo: "))
            if altura <= 0:
                print("La altura no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            if calculo == 1 or calculo == 3:
                # Formula area: base x altura
                area = base * altura
                print(f"Area: {area}")
            if calculo == 2 or calculo == 3:
                # Formula perimetro: 2 x (base + altura)
                perimetro = 2 * (base + altura)
                print(f"Perimetro: {perimetro}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del triangulo rectangulo
    elif opcion == 4:

        print("                 ")
        print("--- TRIANGULO RECTANGULO ---")
        print("¿Que deseas calcular?")
        print("1. Area")
        print("2. Hipotenusa")
        print("3. Angulo faltante")
        print("4. Todo")

        try:
            calculo = int(input("Elige una opcion: "))
        except ValueError:
            print("Opcion invalida")
            calculo = 0

        valido = True

        if calculo == 1 or calculo == 2 or calculo == 4:
            try:
                base = float(input("Base del triangulo rectangulo: "))
                if base <= 0:
                    print("La base no puede ser cero o negativa")
                    valido = False
            except ValueError:
                print("Ingresa un valor numerico")
                valido = False

            try:
                altura = float(input("Altura del triangulo rectangulo: "))
                if altura <= 0:
                    print("La altura no puede ser cero o negativa")
                    valido = False
            except ValueError:
                print("Ingresa un valor numerico")
                valido = False

        if calculo == 3 or calculo == 4:
            try:
                angulo1 = float(input("Angulo 1 (en grados): "))
                if angulo1 <= 0:
                    print("El angulo no puede ser cero o negativo")
                    valido = False
            except ValueError:
                print("Ingresa un valor numerico")
                valido = False

            try:
                angulo2 = float(input("Angulo 2 (en grados): "))
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
            if calculo == 1 or calculo == 4:
                # Formula area: (base x altura) / 2
                area = (base * altura) / 2
                print(f"Area: {area}")
            if calculo == 2 or calculo == 4:
                # Formula hipotenusa: raiz(base² + altura²)
                hipotenusa = (base ** 2 + altura ** 2) ** 0.5
                print(f"Hipotenusa: {hipotenusa}")
            if calculo == 3 or calculo == 4:
                # Formula angulo faltante: 180 - angulo1 - angulo2
                angulo3 = 180 - angulo1 - angulo2
                print(f"Angulo faltante: {angulo3} grados")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del rombo
    elif opcion == 5:

        print("                 ")
        print("--- ROMBO ---")
        print("¿Que deseas calcular?")
        print("1. Area")
        print("2. Perimetro")
        print("3. Todo")

        try:
            calculo = int(input("Elige una opcion: "))
        except ValueError:
            print("Opcion invalida")
            calculo = 0

        valido = True

        try:
            diagonal1 = float(input("Diagonal mayor del rombo: "))
            if diagonal1 <= 0:
                print("La diagonal no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        try:
            diagonal2 = float(input("Diagonal menor del rombo: "))
            if diagonal2 <= 0:
                print("La diagonal no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            if calculo == 1 or calculo == 3:
                # Formula area: (diagonal1 x diagonal2) / 2
                area = (diagonal1 * diagonal2) / 2
                print(f"Area: {area}")
            if calculo == 2 or calculo == 3:
                # Formula perimetro: 2 x raiz(diagonal1² + diagonal2²)
                perimetro = 2 * (diagonal1 ** 2 + diagonal2 ** 2) ** 0.5
                print(f"Perimetro: {perimetro}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del cubo
    elif opcion == 6:

        print("                 ")
        print("--- CUBO ---")
        print("¿Que deseas calcular?")
        print("1. Area total")
        print("2. Volumen")
        print("3. Todo")

        try:
            calculo = int(input("Elige una opcion: "))
        except ValueError:
            print("Opcion invalida")
            calculo = 0

        valido = True

        try:
            arista = float(input("Longitud de la arista del cubo: "))
            if arista <= 0:
                print("La arista no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            if calculo == 1 or calculo == 3:
                # Formula area total: 6 x arista²
                area = 6 * arista ** 2
                print(f"Area total: {area}")
            if calculo == 2 or calculo == 3:
                # Formula volumen: arista³
                volumen = arista ** 3
                print(f"Volumen: {volumen}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo de la esfera
    elif opcion == 7:

        print("                 ")
        print("--- ESFERA ---")
        print("¿Que deseas calcular?")
        print("1. Area total")
        print("2. Volumen")
        print("3. Todo")

        try:
            calculo = int(input("Elige una opcion: "))
        except ValueError:
            print("Opcion invalida")
            calculo = 0

        valido = True

        try:
            radio = float(input("Radio de la esfera: "))
            if radio <= 0:
                print("El radio no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            if calculo == 1 or calculo == 3:
                # Formula area: 4 x pi x radio²
                area = 4 * pi * radio ** 2
                print(f"Area total: {area}")
            if calculo == 2 or calculo == 3:
                # Formula volumen: (4/3) x pi x radio³
                volumen = (4/3) * pi * radio ** 3
                print(f"Volumen: {volumen}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo del cilindro
    elif opcion == 8:

        print("                 ")
        print("--- CILINDRO ---")
        print("¿Que deseas calcular?")
        print("1. Area total")
        print("2. Volumen")
        print("3. Todo")

        try:
            calculo = int(input("Elige una opcion: "))
        except ValueError:
            print("Opcion invalida")
            calculo = 0

        valido = True

        try:
            radio = float(input("Radio de la base del cilindro: "))
            if radio <= 0:
                print("El radio no puede ser cero o negativo")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        try:
            altura = float(input("Altura del cilindro: "))
            if altura <= 0:
                print("La altura no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            if calculo == 1 or calculo == 3:
                # Formula area: 2 x pi x radio x (radio + altura)
                area = 2 * pi * radio * (radio + altura)
                print(f"Area total: {area}")
            if calculo == 2 or calculo == 3:
                # Formula volumen: pi x radio² x altura
                volumen = pi * radio ** 2 * altura
                print(f"Volumen: {volumen}")
        else:
            print("No se pudo calcular por datos invalidos")

        continuar = input("Deseas calcular otra figura? (si/no): ")
        if continuar == "no":
            print("Saliendo...")
            salir = True

    # Calculo de la piramide
    elif opcion == 9:

        print("                 ")
        print("--- PIRAMIDE ---")
        print("¿Que deseas calcular?")
        print("1. Area total")
        print("2. Volumen")
        print("3. Todo")

        try:
            calculo = int(input("Elige una opcion: "))
        except ValueError:
            print("Opcion invalida")
            calculo = 0

        valido = True

        try:
            base = float(input("Lado de la base de la piramide: "))
            if base <= 0:
                print("La base no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        try:
            altura = float(input("Altura de la piramide: "))
            if altura <= 0:
                print("La altura no puede ser cero o negativa")
                valido = False
        except ValueError:
            print("Ingresa un valor numerico")
            valido = False

        if valido == True:
            if calculo == 1 or calculo == 3:
                # Formula area total: base² + 2 x base x altura
                area = base ** 2 + 2 * base * altura
                print(f"Area total: {area}")
            if calculo == 2 or calculo == 3:
                # Formula volumen: (base² x altura) / 3
                volumen = (base ** 2 * altura) / 3
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