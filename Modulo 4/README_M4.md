# Bootcamp_fundamentos_de_python_M4.
Proyecto: Construye una Pokédex.

## Introducción.
Este proyecto es una aplicación interactiva desarrollada en Python que simula el funcionamiento de una Pokédex, utilizando datos en tiempo real obtenidos desde la PokéAPI, 
el objetivo es presentar información relevante de cada Pokémon, como tipo, habilidades, descripción y su imagen de forma accesible, el código fue desarrollado como parte del proceso formativo en mi bootcamp 
con el propósito de aplicar conceptos fundamentales como el consumo de APIs, manejo de datos estructurados en JSON, y diseño centrado en el usuario.

## Proceso de desarrollo.
El desarrollo de esta Pokédex se llevó a cabo en etapas progresivas, cada una enfocada en consolidar habilidades específicas:

1. Definición del objetivo.
- Construir una herramienta que permitiera consultar información de algun Pokémon en tiempo real, con salida en español y visualización de imágenes, todo desde una interfaz sencilla.

2. Consumo de la PokéAPI. 
- Se utiliza la biblioteca requests para realizar peticiones HTTP a la PokéAPI, interpretar respuestas en formato JSON y extraer datos relevantes como nombre, tipo, habilidades y descripción.

4. Localización del contenido.  
- Para mejorar la experiencia del usuario hispanohablante, se implementó un sistema de traducción de términos clave, esto incluyó la creación de diccionarios personalizados para mapear tipos, habilidades y descripciones al español.

5. Visualización de imágenes en memoria.  
- Se integró el uso de BytesIO para manejar imágenes directamente desde la URL sin necesidad de guardarlas en disco, con Pillow, se logró mostrar la imagen del Pokémon.

6. Diseño modular y manejo de errores.  
- El código se estructuró en funciones independientes para facilitar su mantenimiento y escalabilidad, se incorporó manejo de excepciones para cubrir casos como nombres inválidos, errores de conexión o respuestas incompletas.

7. Pruebas y validación.  
- Se realizaron pruebas manuales con diferentes entradas (nombres, IDs, errores intencionales) para validar la robustez del sistema y asegurar una experiencia fluida.

## Bibliotecas necesarias.
Para ejecutar el proyecto, asegúrate de tener instaladas las siguientes bibliotecas:
- requests 
- pillow

## Ejemplo de busqueda.
[![Captura-de-pantalla-2025-08-02-113623.png](https://i.postimg.cc/WbJKRnKz/Captura-de-pantalla-2025-08-02-113623.png)](https://postimg.cc/zV8pKnqY)

## Reflexiones del bootcamp.
Este proyecto marcó un punto clave en mi proceso formativo ya que a través del desarrollo de la Pokédex, pude aplicar de forma práctica conceptos que antes solo conocía en teoría, algunas de las reflexiones más importantes que me llevo de este módulo son:
- La importancia de entender el flujo de datos.
  Aprender a consumir una API y transformar su respuesta en algo útil para el usuario me enseñó a pensar en términos de entrada, procesamiento y salida, esto cambió mi forma de abordar problemas de programación.

- El valor de la experiencia del usuario. 
  Traducir los datos al español y presentar la información de forma clara me hizo consciente de que el código no solo debe funcionar, sino también ser accesible y comprensible para quien lo usa.

- El poder de trabajar con datos en tiempo real. 
  Usar una API pública me permitió ver cómo se puede construir software que interactúe con el mundo exterior, y cómo manejar la incertidumbre que eso implica (errores, formatos cambiantes, etc.).

- La utilidad de herramientas como BytesIO y Pillow. 
  Manejar imágenes en memoria fue un reto técnico que me ayudó a entender mejor cómo funciona el manejo de archivos en Python, y cómo optimizar recursos sin depender del sistema de archivos.

- La importancia de modularidad y manejo de errores.  
  Estructurar el código en funciones reutilizables y anticipar fallos me dio una base sólida para proyectos más complejos, aprendí que escribir código limpio y robusto es tan importante como hacerlo funcionar.
