"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob
import fileinput

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    data = []
    # Leer líneas de archivos especificados o de la entrada estándar (stdin)
    for line in fileinput.input(files="files\input\data.csv"):
        data.append(line.split()[0])  # strip() elimina los saltos de línea al final de cada línea
    
    cuenta = []
    for i in data:
        cuenta.append((i, data.count(i)))
    sin = set(cuenta)
    return sorted(sin)


print(pregunta_02())
