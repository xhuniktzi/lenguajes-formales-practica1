# Controlador añadir cursos

from helpers.parsers import parse_estado, parse_opcionalidad, parse_requisitos
from helpers.database import create
from models.Curso import Curso


def exec(database):
    new_curso = Curso()

    print('*** Registrar un nuevo curso ***\n')
    print('-> Si el codigo del curso ya existe, actualizara el curso con los nuevos datos\n')

    print('Ingrese el codigo del curso: ', end='')
    new_curso.codigo = int(input())
    print('Ingrese el nombre del curso: ', end='')
    new_curso.nombre = input()
    print('Ingresa los pre-requisitos del curso (separados con ";"): ', end='')
    new_curso.codigo_requisitos = parse_requisitos(input())
    print('Ingresa la opcionalidad (0: opcional, 1: obligatorio): ', end='')
    new_curso.opcionalidad = parse_opcionalidad(input())
    print('Ingresa el semestre al que corresponde: ', end='')
    new_curso.semestre = int(input())
    print('Ingresa el numero de creditos correspondiente: ', end='')
    new_curso.creditos = int(input())
    print('Ingresa el estado (0: aprobado, 1: cursando, -1: pendiente): ', end='')
    new_curso.estado = parse_estado(input())
    create(database, new_curso)
    pass
