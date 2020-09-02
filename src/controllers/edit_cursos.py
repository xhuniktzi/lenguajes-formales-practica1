# Controlador editar cursos

from helpers.database import update, read
from models.Curso import Curso
from helpers.parsers import parse_requisitos, parse_opcionalidad, parse_requisitos


def exec(database):
    new_curso = Curso()

    print('*** Editar curso ***')
    print('Ingresa el codigo del curso a editar: ', end='')
    code = int(input())
    curso = read(database, codigo=code)[0]

    print('Ingresa el codigo, actual: (' + str(curso.codigo) + ') ', end='')
    curso_codigo = int(input() or curso.codigo)
    new_curso.codigo = curso_codigo

    print('Ingresa el nombre, actual: (' + curso.nombre + ')', end='')
    curso_nombre = input() or curso.nombre
    new_curso.nombre = curso_nombre

    print('Ingresa los pre-requisitos, separados con ";", actual: (' +
          str(curso.codigo_requisitos) + ')', end='')
    curso_prerequisitos = parse_requisitos(input()) or curso.codigo_requisitos
    new_curso.codigo_requisitos = curso_prerequisitos

    print('Ingresa la opcionalidad, (0: opcional, 1: obligatorio), actual: (' +
          curso.opcionalidad.name + ')', end='')
    curso_opt = parse_opcionalidad(input())
    new_curso.opcionalidad = curso_opt

    print('Ingresa el semestre, actual: (' + curso.semestre + ')', end='')
    curso_semestre = int(input())

    pass
