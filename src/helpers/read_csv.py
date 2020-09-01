# Lector de archivos csv desde el disco duro

import csv
from models.Curso import Curso
from models.Estado import Estado
from models.Opcionalidad import Opcionalidad


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


def parse_requisitos(string_requisitos):
    list_requisitos = string_requisitos.split(';')
    list_return = list()
    if list_requisitos[0] != '':
        for element in list_requisitos:
            list_return.append(int(element))
            pass
        pass
    return list_return


def parse_opcionalidad(string_opt):
    if string_opt == '0':
        return Opcionalidad.opcional
    elif string_opt == '1':
        return Opcionalidad.obligatorio
    pass


def parse_estado(string_estado):
    if string_estado == '0':
        return Estado.aprobado
    elif string_estado == '1':
        return Estado.cursando
    elif string_estado == '-1':
        return Estado.pendiente
    pass
