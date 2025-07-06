# Bootcamp_fundamentos_de_python_M2.
Proyecto: Simulación de la Máquina de Galton.

## Introducción.
Este proyecto es una simulación visual de la Máquina de Galton, un experimento clásico de la estadística que ilustra cómo decisiones aleatorias pueden generar una distribución normal, este código fue desarrollado como parte del proceso formativo en mi bootcamp.

## Proceso de desarrollo.
1. Lógica de simulación:
- Utilicé Python y la librería estándar random para simular el comportamiento de una canica al atravesar múltiples niveles.
- Cada canica atraviesa n_niveles en los que toma una decisión aleatoria: ir a la derecha o a la izquierda.
- La cantidad de veces que una canica "elige" la derecha determina en qué contenedor final caerá.
- Repetí esta simulación n_canicas veces para obtener una distribución completa.

2. Visualización de resultados.
- Usé matplotlib.pyplot para graficar un histograma con los resultados finales.
- A cada barra le añadí una etiqueta con el número de canicas, para facilitar la lectura de los datos.
- Personalicé tipografía, colores y estilo para obtener una visualización clara, estética y comprensible.

3. Parámetros.
- n_canicas = 3000    # Número total de canicas lanzadas.
- n_niveles = 12      # Número de decisiones binarias (niveles).
  
## Reflexiones del Bootcamp.
Este ejercicio fue mucho más que programar una simulación, algunas de las lecciones más importantes que me dejó fueron:
- Pensamiento lógico y estructurado: Aprendí a descomponer un problema complejo en pequeñas funciones reutilizables y comprensibles.
- Importancia de visualizar los datos: Noté cómo una simple gráfica puede transformar números en entendimiento visual inmediato.
- Confianza en mis habilidades técnicas: Ver cómo una idea se convierte en código funcional refuerza mi seguridad como desarrollador.
- Iteración y mejora constante: Validar resultados, ajustar parámetros y experimentar con el código me enseñó a mejorar mis soluciones paso a paso.
- Crecimiento personal en el bootcamp: He ganado disciplina, resiliencia y el deseo de seguir aprendiendo cada día. La experiencia ha sido desafiante, pero también profundamente enriquecedora.
