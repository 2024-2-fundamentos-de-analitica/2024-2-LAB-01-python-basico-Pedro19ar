"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor después del carácter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado más
    pequeño y el valor asociado más grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """
    file_path = "files/input/data.csv"  # Ruta del archivo

    # Diccionario para almacenar los valores asociados a cada clave
    key_values = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")  # Asumiendo que los datos están separados por tabulaciones
            if len(columns) >= 5:
                key_value_pairs = columns[4].split(",")  # Extraer los pares clave-valor
                
                for pair in key_value_pairs:
                    key, value = pair.split(":")  # Separar clave y valor
                    value = int(value)  # Convertir el valor a entero
                    
                    if key not in key_values:
                        key_values[key] = []
                    
                    key_values[key].append(value)

    # Construir la lista de tuplas con la clave, valor mínimo y valor máximo
    result = [(key, min(values), max(values)) for key, values in sorted(key_values.items())]

    return result

# Llamada a la función
print(pregunta_06())

