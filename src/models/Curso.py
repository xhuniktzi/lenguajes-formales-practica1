from models.Estado import Estado
from models.Opcionalidad import Opcionalidad


class Curso:
    codigo = int()
    nombre = str()
    codigo_requisitos = list()
    opcionalidad = Opcionalidad.opcional
    semestre = int()
    creditos = int()
    estado = Estado.pendiente
    pass
