# Manejador de alto nivel para la base de datos

from helpers.core_db import core_create, core_read, core_update, core_delete
from errors.CursoRefError import CursoRefError
from models.Estado import Estado
from models.Opcionalidad import Opcionalidad


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

    core_delete(database, id_curso)
    pass


def read(database,
         codigo=None,
         semestre=None,
         opcionalidad=None,
         creditos=None,
         estado=None):

    if type(codigo) != int and codigo != None:
        raise TypeError
    elif type(semestre) != int and semestre != None:
        raise TypeError
    elif type(opcionalidad) != Opcionalidad and opcionalidad != None:
        raise TypeError
    elif type(creditos) != int and creditos != None:
        raise TypeError
    elif type(estado) != Estado and estado != None:
        raise TypeError

    list_read = core_read(database)

    list_return = list()

    for element in list_read:
        flag = True
        if element.codigo != codigo and codigo != None:
            flag = False
            pass
        if element.semestre != semestre and semestre != None:
            flag = False
            pass
        if element.opcionalidad != opcionalidad and opcionalidad != None:
            flag = False
            pass
        if element.creditos != creditos and creditos != None:
            flag = False
            pass
        if element.estado != estado and estado != None:
            flag = False
            pass

        if flag:
            list_return.append(element)
            pass
        pass

    return tuple(list_return)
