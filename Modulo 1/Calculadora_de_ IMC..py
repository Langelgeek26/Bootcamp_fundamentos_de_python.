# Esta funcion garantiza que el usuario ingrese el tipo de dato correcto y no deje espacios vacios.

def Datos (prompt, tipo=str):
    while True:
        valor = input(prompt)
        if not valor:
            print("Ingrese sus datos por favor: ")
            continue
        try:
            return tipo(valor)
        except ValueError:
            print("Intentelo nuevamente: ")

# En este bloque de codigo se le pide al usuario ingresar su informacion correctamente respetando el tipo de dato que se le solicita.

Nombre = Datos ("Ingrese su nombre: ")
Apellido_P = Datos ("Ingrese su apellido paterno: ")
Apellido_M = Datos ("Ingrese su apellido materno: ")
Edad = Datos ("Ingrese su edad: ", int)
Peso = Datos ("Ingrese su peso: ",  int)
Estatura = Datos ("Ingrese su estatura: ", float )

# En esta linea de codigo se realiza el calculo del IMC conforme a los datos ingresados por el usuario.

IMC = Peso / (Estatura ** 2)

# Este bloque de condicionales arroja la categoria correspondiente al usuario conforme a sus resultados.

if IMC >= 17 and IMC <= 18.9:
    Categoria = "Usted presenta un peso bajo"
elif IMC >= 18.50 and IMC <= 24.99:
    Categoria = "Usted presenta un peso normal"
elif IMC >= 25.00 and IMC <= 29.99:
    Categoria = "Usted presenta sobrepeso"
elif IMC >= 30.00 and IMC <= 34.99:
    Categoria = "Usted presenta obesidad leve"
elif IMC >= 35.00 and IMC <= 39.99:
    Categoria = "Usted presenta obesidad media"
else:
    Categoria = "Usted presenta obesidad morbida"

# En este bloque de codigo se organizan los datos del usuario de manera estructurada permitiendo visualizar su informacion y rersultados obtenidos.

print("\n--- Datos del usuario ---")
print(f"Nombre completo: {Nombre} {Apellido_P} {Apellido_M}")
print(f"Edad: {Edad} años")
print(f"Peso: {Peso} kg")
print(f"Estatura: {Estatura} m")
print(f"Indice de Masa Corporal (IMC): {IMC:.2f}")
print(f"Clasificacion IMC: {Categoria}")
