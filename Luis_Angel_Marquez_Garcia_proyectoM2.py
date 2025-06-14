def verificar_longitud_palabra():
    while True:  # Aqui se ejecutará un bucle infinito hasta que se cumpla la condición de solicitada.
        palabra = input("Ingrese una palabra sin espacios ni números: ").strip()  

        if not palabra.isalpha():  # Se verifica si la palabra contiene caracteres que no sean letras.
            print("Error: La palabra solo debe contener letras.")
            continue  # Si la palabra no es válida, vuelve a solicitar su ingreso.

        longitud = len(palabra)

        if 4 <= longitud <= 8:
            print("La palabra es correcta.")
            break  # Se finaliza el bucle cuando se ha ingresado una palabra válida.
        elif longitud < 4:
            print(f"Hacen falta letras, la palabra solo tiene {longitud} letras, inténtalo de nuevo.")
        else:
            print(f"Sobran letras, la palabra solo tiene {longitud} letras, inténtalo de nuevo.")

verificar_longitud_palabra()