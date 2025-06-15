# 1.- Longitud de una frase:

def verificar_longitud_palabra():
    while True:  # Aqui se ejecutará un bucle infinito hasta que se cumpla la condición de solicitada.
        palabra = input("Ingrese una palabra sin espacios ni números: ").strip()  
        
        # Verificación de caracteres.
        if not palabra.isalpha():  # Se verifica si la palabra contiene caracteres que no sean letras.
            print("Error: La palabra solo debe contener letras.")  
            continue  # Si la palabra no es válida, vuelve a solicitar su ingreso.

        longitud = len(palabra)

        # Comprobación de la longitud.
        if 4 <= longitud <= 8:  
            print("La palabra es correcta.")
            break  # Finaliza el bucle cuando la palabra es válida.
        elif longitud < 4:  
            print(f"Hacen falta letras, la palabra solo tiene {longitud} letras, inténtalo de nuevo.")
        else:  
            print(f"Sobran letras, la palabra solo tiene {longitud} letras, inténtalo de nuevo.")

# Llamada a la función para ejecutar la verificación.
verificar_longitud_palabra()





#2.- Encuentra el cuadrante:

# Función para obtener una coordenada ingresada por el usuario.
def obtener_coordenada(mensaje):
    while True:  # Aqui se ejecutará un bucle infinito hasta que se cumpla la condición de solicitada.
        try:
            valor = int(input(mensaje))  # Aqui se solicita un número entero.
            if valor != 0:  # El if se asegura que el valor ingresado no sea 0.
                return valor
            else:
                print("Las coordenadas no pueden ser 0. Inténtalo de nuevo.")
        except ValueError:  # Manejo de errores en caso de que el usuario no ingrese un número válido.
            print("Por favor, ingrese solo números enteros.")

# Función para determinar el cuadrante.
def determinar_cuadrante(x, y):
    if x > 0 and y > 0:
        return f"El punto ({x}, {y}) se encuentra en el cuadrante I."
    if x < 0 and y > 0:
        return f"El punto ({x}, {y}) se encuentra en el cuadrante II."
    if x < 0 and y < 0:
        return f"El punto ({x}, {y}) se encuentra en el cuadrante III."
    return f"El punto ({x}, {y}) se encuentra en el cuadrante IV."

# Se solicitan las coordenadas X y Y al usuario.
x = obtener_coordenada("Ingrese X: ")
y = obtener_coordenada("Ingrese Y: ")

print(determinar_cuadrante(x, y))
