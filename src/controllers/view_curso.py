# Controlador mostrar curso

from helpers.database import read
from views import view_curso


def exec(database):
    print('Ingresa el codigo del curso a mostrar: ')
    code_curso = int(input())
    curso = read(database, codigo=code_curso)
    try:
        view_curso.render(curso[0])
        pass
    except IndexError:
        print('No hay coincidencias')
    pass
