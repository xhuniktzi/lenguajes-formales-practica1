# Controlador contador cursos aprobados

from helpers.database import read
from models.Estado import Estado
from views import list_cursos


def exec(database):
    data_cursos = read(database, estado=Estado.aprobado)
    count_creditos = int()

    for element in data_cursos:
        count_creditos += element.creditos
        pass

    list_cursos.render(data_cursos)
    print('\nCreditos aprobados: ' + str(count_creditos))
    pass
