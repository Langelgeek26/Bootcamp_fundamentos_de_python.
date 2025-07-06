import random
import matplotlib.pyplot as plt

# Función para simular el recorrido de las canicas.
def simular_canicas(n_canicas, n_niveles):
    resultados = [0] * (n_niveles + 1)  # Lista de contadores para cada contenedor.

    for _ in range(n_canicas):
        derecha = 0
        for _ in range(n_niveles):
            if random.random() > 0.5:
                derecha += 1
        resultados[derecha] += 1  # El número de veces que cayó a la derecha indica la posición final.

    return resultados

# Función para graficar el histograma.
def graficar_histograma(resultados):
    posiciones = list(range(len(resultados)))
    plt.bar(posiciones, resultados, color='grey', edgecolor='black')

    for i, cantidad in enumerate(resultados):
        plt.text(i, cantidad + max(resultados) * 0.01, str(cantidad),
                 ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.xlabel('Distribucion de canicas', fontname='Comic Sans MS')
    plt.ylabel('Cantidad de canicas', fontname='Comic Sans MS')
    plt.title('Simulación de Máquina de Galton', fontname='Comic Sans MS')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Ejecución del programa.
n_canicas = 3000
n_niveles = 12
resultados = simular_canicas(n_canicas, n_niveles)
graficar_histograma(resultados)
