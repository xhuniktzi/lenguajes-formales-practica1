# Manejadores de bajo nivel para la base de datos

from models.Opcionalidad import Opcionalidad
from models.Estado import Estado
from models.Curso import Curso


def core_create(database, curso):
    if type(curso) != Curso:
        raise TypeError
    if type(database) != list:
        raise TypeError

    if type(curso.codigo) != int:
        raise TypeError
    elif type(curso.nombre) != str:
        raise TypeError
    elif type(curso.codigo_requisitos) != list:
        raise TypeError
    elif type(curso.opcionalidad) != Opcionalidad:
        raise TypeError
    elif type(curso.semestre) != int:
        raise TypeError
    elif type(curso.creditos) != int:
        raise TypeError
    elif type(curso.estado) != Estado:
        raise TypeError

    database.append(curso)
    return curso


def core_read(database, id_curso=None):
    list_return = list()

    if id_curso == None:
        list_return = database
        return tuple(list_return)
    else:
        for obj in database:
            if obj.codigo == id_curso:
                list_return.append(obj)
                pass
            pass
        pass
    return tuple(list_return)


def core_update(database, curso, id_curso):
    list_return = list()

    if type(curso) != Curso:
        raise TypeError
    if type(database) != list:
        raise TypeError
    if type(id_curso) != int:
        raise TypeError

    if type(curso.codigo) != int:
        raise TypeError
    elif type(curso.nombre) != str:
        raise TypeError
    elif type(curso.codigo_requisitos) != list:
        raise TypeError
    elif type(curso.opcionalidad) != Opcionalidad:
        raise TypeError
    elif type(curso.semestre) != int:
        raise TypeError
    elif type(curso.creditos) != int:
        raise TypeError
    elif type(curso.estado) != Estado:
        raise TypeError

    for obj in database:
        if obj.codigo == id_curso:
            obj.codigo = curso.codigo
            obj.nombre = curso.nombre
            obj.codigo_requisitos = curso.codigo_requisitos
            obj.opcionalidad = curso.opcionalidad
            obj.semestre = curso.semestre
            obj.creditos = curso.creditos
            obj.estado = curso.estado
            list_return.append(curso)
            pass
        pass

    return tuple(list_return)


def core_delete(database, id_curso):
    list_return = list()

    if type(database) != list:
        raise TypeError
    if type(id_curso) != int:
        raise TypeError

    for obj in database:
        if obj.codigo == id_curso:
            database.remove(obj)
            list_return.append(obj)
            pass
        pass
    return tuple(list_return)
