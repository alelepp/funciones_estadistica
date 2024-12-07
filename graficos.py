# Gráfico de torta para los 10 tipos espectrales más frecuentes
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    frequencies,  # Las frecuencias calculadas en la Pregunta 1
    labels=top_10_types_list,  # Las 10 categorías más frecuentes
    autopct='%1.1f%%',  # Mostrar porcentajes
    colors=plt.cm.tab10.colors,  # Colores de la paleta Tab10
    startangle=90  # Comienza desde arriba
)
ax.set_title('Distribución de los 10 Tipos Espectrales Más Frecuentes', fontsize=14)
plt.show()
