# Controlador menu carga de archivos

from views import load_files
from helpers.read_csv import read_csv
from helpers.database import create
from models.Curso import Curso
from models.Opcionalidad import Opcionalidad
from models.Estado import Estado


def exec(database):
    load_files.render()
    string_url_csv = input()
    file_csv = read_csv(string_url_csv)
    for element in file_csv:
        new_curso = Curso()
        new_curso.codigo = int(element['codigo'])
        new_curso.nombre = element['nombre']
        new_curso.codigo_requisitos = parse_requisitos(
            element['codigo_requisitos'])
        new_curso.opcionalidad = parse_opcionalidad(element['opcionalidad'])
        new_curso.semestre = element['semestre']
        new_curso.creditos = element['creditos']
        new_curso.estado = parse_estado(element['estado'])

        create(database, new_curso)
        pass
    pass


def parse_requisitos(string_requisitos):
    list_requisitos = string_requisitos.split(';')
    return list_requisitos


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
