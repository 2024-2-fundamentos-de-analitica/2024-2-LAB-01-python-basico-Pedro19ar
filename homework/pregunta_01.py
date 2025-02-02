"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob
import fileinput

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = []
    # Leer líneas de archivos especificados o de la entrada estándar (stdin)
    for line in fileinput.input(files="files\input\data.csv"):
        data.append(int(line.split()[1]))  # strip() elimina los saltos de línea al final de cada línea
    return sum(data)


print(pregunta_01())