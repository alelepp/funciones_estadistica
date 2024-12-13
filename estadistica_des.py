# Función para calcular el promedio (media)
def calcular_media(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma / len(lista)

# Función para calcular la mediana sin modificar la lista original
def calcular_mediana(lista):
    lista_ordenada = lista[:]  # Crear una copia de la lista original
    n = len(lista_ordenada)
    for i in range(n):  # Ordenar la lista manualmente (burbuja)
        for j in range(0, n - i - 1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    mitad = n // 2
    if n % 2 == 0:  # Si el número de elementos es par
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:  # Si el número de elementos es impar
        return lista_ordenada[mitad]

# Función para calcular la moda
def calcular_moda(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    max_frecuencia = 0
    modas = []
    for elemento, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            modas = [elemento]
        elif frecuencia == max_frecuencia:
            modas.append(elemento)
    if len(modas) == 1:  # Si solo hay una moda
        return modas[0]
    return modas  # Si hay varias modas, devolver la lista

# Función para calcular la varianza
def calcular_varianza(lista):
    media = calcular_media(lista)
    suma_cuadrados = 0
    for elemento in lista:
        suma_cuadrados += (elemento - media) ** 2
    return suma_cuadrados / len(lista)

# Función para calcular la desviación estándar
def calcular_desviacion_estandar(lista):
    varianza = calcular_varianza(lista)
    return varianza ** 0.5

# Función para calcular la desviación absoluta media
def calcular_absoluta_media(lista):
    media = calcular_media(lista)
    suma_desviaciones = 0
    for elemento in lista:
        suma_desviaciones += abs(elemento - media)
    return suma_desviaciones / len(lista)

# Función para calcular el rango intercuartil (IQR)
def calcular_rango_intercuartil(lista):
    lista_ordenada = lista[:]  # Crear una copia de la lista original
    n = len(lista_ordenada)
    for i in range(n):  # Ordenar la lista manualmente (burbuja)
        for j in range(0, n - i - 1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    mitad = n // 2
    if n % 2 == 0:
        q1 = calcular_mediana(lista_ordenada[:mitad])
        q3 = calcular_mediana(lista_ordenada[mitad:])
    else:
        q1 = calcular_mediana(lista_ordenada[:mitad])
        q3 = calcular_mediana(lista_ordenada[mitad + 1:])
    return q3 - q1

# Función para calcular el MAD (Median Absolute Deviation)
def calcular_mad(lista):
    mediana = calcular_mediana(lista)
    desviaciones_absolutas = [abs(elemento - mediana) for elemento in lista]
    return calcular_mediana(desviaciones_absolutas)
