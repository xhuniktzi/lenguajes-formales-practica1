# Manipuladores de datos

from models.Curso import Curso
from models.Estado import Estado
from models.Opcionalidad import Opcionalidad


def parse_requisitos(string_requisitos):
    list_requisitos = string_requisitos.split(';')
    list_return = list()
    if list_requisitos[0] != '':
        for element in list_requisitos:
            list_return.append(int(element))
            pass
        pass
    return list_return


def parse_opcionalidad(string_opt):
    if string_opt == '0':
        return Opcionalidad.opcional
    elif string_opt == '1':
        return Opcionalidad.obligatorio
    pass


def parse_estado(string_estado):
    if string_estado == '0':
        return Estado.aprobado
    elif string_estado == '1':
        return Estado.cursando
    elif string_estado == '-1':
        return Estado.pendiente
    pass
