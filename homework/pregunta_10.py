"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_10():
    """
    Retorne una lista de tuplas que contengan, por cada fila, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    file_path = "files/input/data.csv"  # Ruta del archivo

    result = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")  # Asumiendo que los datos están separados por tabulaciones
            if len(columns) >= 5:
                letter = columns[0]  # Primera columna (letra)
                count_col4 = len(columns[3].split(","))  # Cantidad de elementos en la columna 4
                count_col5 = len(columns[4].split(","))  # Cantidad de elementos en la columna 5

                result.append((letter, count_col4, count_col5))

    return result

# Llamada a la función
print(pregunta_10())

