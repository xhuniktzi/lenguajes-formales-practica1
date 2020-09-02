# Lector de archivos csv desde el disco duro

import csv
from models.Curso import Curso
from models.Estado import Estado
from models.Opcionalidad import Opcionalidad
from helpers.parsers import *


def read_csv(url_csv):
    return_list = list()
    with open(url_csv, newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            new_curso = Curso()
            new_curso.codigo = int(row[0])
            new_curso.nombre = row[1]
            new_curso.codigo_requisitos = parse_requisitos(row[2])
            new_curso.opcionalidad = parse_opcionalidad(row[3])
            new_curso.semestre = int(row[4])
            new_curso.creditos = int(row[5])
            new_curso.estado = parse_estado(row[6])
            return_list.append(new_curso)
            pass
        pass
    return tuple(return_list)
