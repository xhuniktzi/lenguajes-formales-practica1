# Controlador contador cursos pendientes

from helpers.database import read
from models.Estado import Estado
from models.Opcionalidad import Opcionalidad
from views import list_cursos


def exec(database):
    data_cursos = read(database, estado=Estado.pendiente,
                       opcionalidad=Opcionalidad.obligatorio)
    count_creditos = int()

    for element in data_cursos:
        count_creditos += element.creditos
        pass

    list_cursos.render(data_cursos)
    print('\nCreditos de cursos pendientes: ' + str(count_creditos))
    pass
