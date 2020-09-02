# Controlador eliminar cursos

from helpers.database import delete
from errors.CursoRefError import CursoRefError


def exec(database):
    print('*** Eliminar cursos ***')
    print('Ingresa el codigo del curso a eliminar')
    code = int(input())
    try:
        delete(database, code)
        pass
    except CursoRefError:
        print('Este curso es dependencia de otro, no se puede borrar')
        pass
    pass
