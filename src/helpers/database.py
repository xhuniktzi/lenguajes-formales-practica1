# Manejador de alto nivel para la base de datos

from helpers.core_db import core_create, core_read, core_update
from errors.CursoRefError import CursoRefError


def create(database, curso):
    flag = bool()
    list_read = core_read(database)
    for element in list_read:
        if element.codigo == curso.codigo:
            flag = True
            pass
        pass

    if flag:
        core_update(database, curso, curso.codigo)
        pass
    else:
        core_create(database, curso)
        pass
    pass


def update(database, curso, id_curso):
    list_read = core_read(database)

    for element in list_read:
        for i in range(0, len(element.codigo_requisitos)):
            if element.codigo_requisitos[i] == id_curso:
                element.codigo_requisitos[i] = curso.codigo
                pass
            pass
        pass

    core_update(database, curso, id_curso)
    pass


def delete(database, id_curso):
    list_read = core_read(database)

    for element in list_read:
        for i in range(0, len(element.codigo_requisitos)):
            if element.codigo_requisitos[i] == id_curso:
                raise CursoRefError
            pass
    pass


def read(database, query):
    list_read = core_read(database)
    pass
