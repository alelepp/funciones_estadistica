# Función para calcular la moda
def calcular_moda(lista):
    frecuencias = {}
    for elemento in lista:
        frecuencias[elemento] = frecuencias.get(elemento, 0) + 1
    moda = max(frecuencias, key=frecuencias.get)
    return moda

# Función para calcular la media
def calcular_media(lista):
    return sum(lista) / len(lista)

# Función para calcular la mediana
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    mitad = n // 2
    if n % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        return lista_ordenada[mitad]
