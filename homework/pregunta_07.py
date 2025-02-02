"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
    """
    file_path = "files/input/data.csv"  # Ruta del archivo

    # Diccionario para almacenar las letras asociadas a cada valor de la columna 2
    value_to_letters = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")  # Asumiendo que los datos están separados por tabulaciones
            if len(columns) >= 2:
                letter = columns[0]  # Primera columna (letra)
                value = int(columns[1])  # Segunda columna (valor numérico)
                
                if value not in value_to_letters:
                    value_to_letters[value] = []
                
                value_to_letters[value].append(letter)

    # Construir la lista de tuplas con el valor de la columna 2 y la lista de letras asociadas
    result = sorted(value_to_letters.items())

    return result

# Llamada a la función
print(pregunta_07())

