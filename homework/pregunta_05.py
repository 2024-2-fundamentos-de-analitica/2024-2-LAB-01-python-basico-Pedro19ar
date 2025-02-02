"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor máximo y mínimo de la columna 2
    por cada letra de la columna 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    file_path = "files/input/data.csv"  # Ruta del archivo

    # Diccionario para almacenar los valores de la columna 2 por cada letra de la columna 1
    letter_values = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")  # Asumiendo que los datos están separados por tabulaciones
            if len(columns) >= 2:
                letter = columns[0]  # Primera columna (letra)
                value = int(columns[1])  # Segunda columna (valor numérico)
                
                if letter not in letter_values:
                    letter_values[letter] = []

                letter_values[letter].append(value)

    # Construir la lista de tuplas con la letra, valor máximo y valor mínimo
    result = [(letter, max(values), min(values)) for letter, values in sorted(letter_values.items())]

    return result

# Llamada a la función
print(pregunta_05())

