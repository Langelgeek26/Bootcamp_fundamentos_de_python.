# Bootcamp_fundamentos_de_python_M2.
Proyecto: Verificación de longitud y cuadrante de coordenadas.

## Introducción.
Este proyecto surge como parte de mi aprendizaje en el bootcamp, donde he reforzado habilidades esenciales en programación con Python, a través de la implementación de dos programas, busco aplicar los conceptos fundamentales como la validación de datos, estructuras de control y manejo de excepciones, el primer programa permite verificar la longitud de una palabra ingresada por el usuario, asegurando que cumpla con el rango establecido y el segundo programa determina el cuadrante en el que se encuentra un punto en el plano cartesiano, a partir de sus coordenadas X y Y, cada uno de estos desafíos me ha llevado a pensar de manera lógica y estructurada, mejorando mis habilidades en la resolución de problemas y escritura de código limpio.

## Proceso de desarrollo.
El desarrollo de este proyecto siguió un enfoque estructurado para garantizar funcionalidad y eficiencia en los programas. 
Las etapas principales fueron las siguientes:

### 1. Planificación y análisis:
- Definición de los dos problemas a resolver:
  - Verificar la longitud de una palabra ingresada por el usuario.
  - Determinar el cuadrante de un punto en el plano cartesiano según sus coordenadas X e Y.

### 2. Diseño del algoritmo:
- **Para la verificación de palabras:**
  - Se estableció un bucle para solicitar una palabra hasta que cumpla los requisitos.
  - Se utilizó `isalpha()` para validar que la entrada solo contenga letras.
  - Se determinó la longitud de la palabra y se implementaron mensajes de retroalimentación si no cumplía los criterios.

- **Para la determinación del cuadrante:**
  - Se implementó un bucle para solicitar coordenadas y validar que no sean cero.
  - Se usaron condicionales para evaluar la posición del punto en el plano cartesiano.
  - Se estructuraron mensajes para indicar claramente el cuadrante correspondiente.

### 3. Implementación del código:
- Creación de funciones independientes (`verificar_longitud_palabra()` y `determinar_cuadrante()`) para modularizar el código y facilitar su reutilización.
- Uso de `try-except` en la función `obtener_coordenada()` para manejar errores en la entrada de coordenadas.
- Aplicación de estructuras de control (`while`, `if-elif-else`) para garantizar que el usuario ingrese datos válidos antes de proceder con el cálculo.

### 4. Pruebas y depuración:
- Se probaron diferentes escenarios, incluyendo:
  - Palabras con caracteres inválidos (números, espacios).
  - Palabras fuera del rango esperado.
  - Coordenadas con valores cero o entradas no numéricas.
- Se corrigieron errores en las validaciones para mejorar la experiencia del usuario.

## Reflexiones sobre el Bootcamp.
El desarrollo de estos programas me ha permitido consolidar mi conocimiento en Python y mejorar mis habilidades de resolución de problemas. 
Algunas de las reflexiones clave que nos ha dejado el proceso son:

### 1. **Importancia de la validación de datos.**
Uno de los principales aprendizajes ha sido la necesidad de validar adecuadamente la entrada del usuario.

### 2. **Pensamiento estructurado y planificación:**
Aprendi que escribir código sin un plan previo puede llevar a errores y soluciones poco eficientes.

### 3. **Manejo de errores y experiencia del usuario:**
Este proyecto me hizo reflexionar sobre cómo interactúa el usuario con nuestros programas.

### 4. **Estructuras de control y modularización:**
Antes del bootcamp, muchas veces escribía código de manera desordenada, sin pensar en su reutilización, pero ahora al crear funciones separadas para cada parte del programa, mejore mi capacidad para estructurar código de forma modular, lo que facilita futuras modificaciones o ampliaciones.

### 5. **Iteración y mejora continua:**
La programación no es solo escribir código una vez y dejarlo así, durante el desarrollo, pase por múltiples iteraciones, refinando funciones y probando casos límite.

### 6. **Aplicación práctica del conocimiento:**
Este proyecto ha sido un excelente ejercicio para aplicar conceptos que antes solo veía en teoría, la importancia de condicionales, bucles y manejo de errores se ha vuelto mucho más clara en la práctica.

En conclusión, este bootcamp me ha dado una perspectiva mucho más profunda sobre el proceso de desarrollo de software, no solo he mejorado mis habilidades técnicas en Python, sino también mi capacidad para estructurar soluciones, pensar en la experiencia del usuario y trabajar de manera eficiente.

## Instalacion y uso.
Para ejecutar este codigo, solo necesitas tener Python instalado en tu sistema, luego puedes correr el script y seguir las instrucciones en la pantalla.
