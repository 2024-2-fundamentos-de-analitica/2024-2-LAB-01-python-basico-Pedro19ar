"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """
    file_path = "files/input/data.csv"  # Ruta del archivo

    # Diccionario para contar la cantidad de registros en que aparece cada clave
    key_count = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")  # Asumiendo que los datos están separados por tabulaciones
            if len(columns) >= 5:
                key_value_pairs = columns[4].split(",")  # Extraer los pares clave-valor
                
                for pair in key_value_pairs:
                    key, _ = pair.split(":")  # Extraer solo la clave
                    
                    key_count[key] = key_count.get(key, 0) + 1

    # Ordenar el diccionario por clave
    result = dict(sorted(key_count.items()))

    return result

# Llamada a la función
print(pregunta_09())

