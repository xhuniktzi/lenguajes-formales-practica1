# Controlador eliminar cursos

from helpers.database import delete


def exec(database):
    print('*** Eliminar cursos ***')
    print('Ingresa el codigo del curso a eliminar')
    code = int(input())
    delete(database, code)
    pass
