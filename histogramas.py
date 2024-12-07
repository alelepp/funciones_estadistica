import math

# Filtrar las estrellas con tipo espectral K0III
estrellas_k0iii = data[data['SpType'] == 'K0III']

# Convertir la columna B-V a lista de números (después de eliminar NaN)
b_v_colores = estrellas_k0iii['B-V'].dropna().astype(float).tolist()

# Calcular el número de bins usando la regla de Freedman-Diaconis
q1, q3 = calcular_cuartiles(b_v_colores)
iqr = q3 - q1  # Rango intercuartílico
bin_width = 2 * iqr / (len(b_v_colores) ** (1 / 3))
num_bins = math.ceil((max(b_v_colores) - min(b_v_colores)) / bin_width)

# Calcular estadísticas para el histograma
promedio = calcular_media(b_v_colores)
mediana = calcular_mediana(b_v_colores)
desviacion_estandar = calcular_desviacion_estandar(b_v_colores)

# Crear el histograma
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(b_v_colores, bins=num_bins, color='gray', edgecolor='black')

# Marcar las estadísticas en el histograma
ax.axvline(promedio, color='black', linestyle='-', label=f'Promedio = {promedio:.3f}')
ax.axvline(mediana, color='red', linestyle='--', label=f'Mediana = {mediana:.3f}')
ax.axvline(promedio - desviacion_estandar, color='green', linestyle=':', label=f'-1 STD = {promedio - desviacion_estandar:.3f}')
ax.axvline(promedio + desviacion_estandar, color='green', linestyle=':', label=f'+1 STD = {promedio + desviacion_estandar:.3f}')
ax.axvline(q1, color='blue', linestyle=':', label=f'Q1 = {q1:.3f}')
ax.axvline(q3, color='blue', linestyle=':', label=f'Q3 = {q3:.3f}')

# Etiquetas y título
ax.set_title('Histograma de Colores B-V para Estrellas K0III', fontsize=14)
ax.set_xlabel('B-V', fontsize=12)
ax.set_ylabel('Frecuencia', fontsize=12)
ax.legend()
plt.show()
