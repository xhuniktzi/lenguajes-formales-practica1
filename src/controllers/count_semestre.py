# Controlador contador cursos semestre

from helpers.database import read
from views import list_cursos


def exec(database):
    print('Ingrese el numero de semestre')
    num_semestre = int(input())
    data_cursos = read(database, semestre=num_semestre)
    count_creditos = int()
    for element in data_cursos:
        count_creditos += element.creditos
        pass

    list_cursos.render(data_cursos)
    print('\nCreditos de cursos cursando actualmente: ' + str(count_creditos))
    pass
