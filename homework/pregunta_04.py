"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    file_path = "files/input/data.csv"  # Ruta del archivo

    month_count = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")  # Asumiendo que los datos están separados por tabulaciones
            if len(columns) >= 3:
                date = columns[2]  # Tercera columna (fecha)
                month = date.split("-")[1]  # Extraer el mes
                month_count[month] = month_count.get(month, 0) + 1

    return sorted(month_count.items())

print(pregunta_04())

