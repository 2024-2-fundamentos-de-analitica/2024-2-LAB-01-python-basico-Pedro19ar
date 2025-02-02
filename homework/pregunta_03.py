"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob
import fileinput

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
        # Inicializar un diccionario para almacenar la suma de la segunda columna para cada letra
    letter_sums = {}

    # Abrir y leer el archivo línea por línea
    with open("files\input\data.csv", 'r') as file:
        for line in file:
            # Dividir la línea en columnas
            columns = line.strip().split('\t')
            letter = columns[0]  # Primera columna (letra)
            number = int(columns[1])  # Segunda columna (número)
            
            # Actualizar la suma para la letra
            if letter in letter_sums:
                letter_sums[letter] += number
            else:
                letter_sums[letter] = number

    # Convertir el diccionario a una lista de tuplas ordenada alfabéticamente
    result = sorted(letter_sums.items())

    return result


print(pregunta_03())
