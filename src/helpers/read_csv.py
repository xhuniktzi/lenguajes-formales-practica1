# Lector de archivos csv desde el disco duro

import csv


def read_csv(url_csv):
    return_list = list()
    with open(url_csv, newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            return_dict = {
                'codigo': row[0],
                'nombre': row[1],
                'codigo_requisitos': row[2],
                'opcionalidad': row[3],
                'semestre': row[4],
                'creditos': row[5],
                'estado': row[6]
            }
            return_list.append(return_dict)
            pass
        pass
    return tuple(return_list)
