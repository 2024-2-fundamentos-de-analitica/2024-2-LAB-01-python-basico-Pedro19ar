"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]
    """
    file_path = "files/input/data.csv"  # Ruta del archivo

    # Diccionario para almacenar letras únicas y ordenadas asociadas a cada valor de la columna 2
    value_to_letters = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")  # Asumiendo que los datos están separados por tabulaciones
            if len(columns) >= 2:
                letter = columns[0]  # Primera columna (letra)
                value = int(columns[1])  # Segunda columna (valor numérico)
                
                if value not in value_to_letters:
                    value_to_letters[value] = set()  # Usamos un conjunto para evitar duplicados
                
                value_to_letters[value].add(letter)

    # Construir la lista de tuplas con el valor de la columna 2 y la lista ordenada de letras únicas
    result = [(value, sorted(list(letters))) for value, letters in sorted(value_to_letters.items())]

    return result

# Llamada a la función
print(pregunta_08())

