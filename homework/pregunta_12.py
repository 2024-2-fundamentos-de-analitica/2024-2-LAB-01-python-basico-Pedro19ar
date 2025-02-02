"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contenga como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    file_path = "files/input/data.csv"  # Ruta del archivo

    # Diccionario para almacenar la suma de valores de la columna 5 por cada letra de la columna 1
    letter_sums = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")  # Asumiendo que los datos están separados por tabulaciones
            if len(columns) >= 5:
                letter = columns[0]  # Primera columna (letra)
                key_value_pairs = columns[4].split(",")  # Quinta columna (pares clave-valor)

                # Sumar los valores de la columna 5
                total_value = sum(int(pair.split(":")[1]) for pair in key_value_pairs)

                letter_sums[letter] = letter_sums.get(letter, 0) + total_value

    # Ordenar el diccionario por clave alfabéticamente
    result = dict(sorted(letter_sums.items()))

    return result

# Llamada a la función
print(pregunta_12())

