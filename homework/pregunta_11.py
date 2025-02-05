"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabéticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    file_path = "files/input/data.csv"  # Ruta del archivo

    # Diccionario para almacenar la suma de la columna 2 por cada letra en la columna 4
    letter_sums = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")  # Asumiendo que los datos están separados por tabulaciones
            if len(columns) >= 4:
                value = int(columns[1])  # Segunda columna (valor numérico)
                letters = columns[3].split(",")  # Cuarta columna (lista de letras)

                for letter in letters:
                    letter_sums[letter] = letter_sums.get(letter, 0) + value

    # Ordenar el diccionario por clave alfabéticamente
    result = dict(sorted(letter_sums.items()))
    return result

# Llamada a la función
print(pregunta_11())

