# Controlador editar cursos

from helpers.database import update, read
from models.Curso import Curso
from helpers.parsers import parse_requisitos, parse_opcionalidad, parse_estado


def exec(database):
    new_curso = Curso()

    print('*** Editar curso ***')
    print('Ingresa el codigo del curso a editar: ', end='')
    code = int(input())
    curso = read(database, codigo=code)[0]

    print('Ingresa el codigo, actual: (' + str(curso.codigo) + ') ', end='')
    curso_codigo = int(input() or curso.codigo)
    new_curso.codigo = curso_codigo

    print('Ingresa el nombre, actual: (' + curso.nombre + ') ', end='')
    curso_nombre = input() or curso.nombre
    new_curso.nombre = curso_nombre

    print('Ingresa los pre-requisitos, separados con ";", actual: (' +
          str(curso.codigo_requisitos) + ') ', end='')
    curso_prerequisitos = parse_requisitos(input()) or curso.codigo_requisitos
    new_curso.codigo_requisitos = curso_prerequisitos

    print('Ingresa la opcionalidad, (0: opcional, 1: obligatorio), actual: (' +
          curso.opcionalidad.name + ') ', end='')
    curso_opt = parse_opcionalidad(input()) or curso.opcionalidad
    new_curso.opcionalidad = curso_opt

    print('Ingresa el semestre, actual: (' + str(curso.semestre) + ') ', end='')
    curso_semestre = int(input() or curso.semestre)
    new_curso.semestre = curso_semestre

    print('Ingrese los creditos, actual: (' + str(curso.creditos) + ') ', end='')
    curso_creditos = int(input() or curso.creditos)
    new_curso.creditos = curso_creditos

    print('Ingrese el estado, (0: aprobado, 1: cursando, -1: pendiente), actual: (' +
          curso.estado.name + ') ', end='')
    curso_estado = parse_estado(input()) or curso.estado
    new_curso.estado = curso_estado

    update(database, new_curso, code)
    pass
