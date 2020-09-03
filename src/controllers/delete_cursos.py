# Controlador eliminar cursos

from helpers.database import delete, read
from errors.CursoRefError import CursoRefError


def exec(database):
    print('*** Eliminar cursos ***')
    print('Ingresa el codigo del curso a eliminar')
    code = int(input())
    try:
        if len(read(database, codigo=code)) != 0:
            delete(database, code)
            pass
        else:
            print('No existe este curso')
            pass
        pass
    except CursoRefError:
        print('Este curso es dependencia de otro, no se puede borrar')
        pass
    pass
