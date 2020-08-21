from models.Estado import Estado
from models.Opcionalidad import Opcionalidad


class Curso:
    __codigo = 0
    __nombre = ''
    __codigo_requisitos = []
    __opcionalidad = Opcionalidad.opcional
    __semestre = 0
    __creditos = 0
    __estado = Estado.pendiente
