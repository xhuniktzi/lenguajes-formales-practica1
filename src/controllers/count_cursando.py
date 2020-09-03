# Controlador contador cursos cursando

from helpers.database import read
from models.Estado import Estado
from views import list_cursos


def exec(database):
    data_cursos = read(database, estado=Estado.cursando)
    count_creditos = int()

    for element in data_cursos:
        count_creditos += element.creditos
        pass

    list_cursos.render(data_cursos)
    print('\nCreditos de cursos cursando actualmente: ' + str(count_creditos))
    pass
