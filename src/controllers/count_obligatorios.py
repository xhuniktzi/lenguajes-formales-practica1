# Controlador contador cursos obligatorios

from helpers.database import read
from models.Opcionalidad import Opcionalidad
from views import list_cursos


def exec(database):
    print('Ingresa el semestre hasta el que se mostraran los creditos')
    num_semestres = int(input())
    count_creditos = int()
    ls_cursos = list()
    for n_semestre in range(num_semestres+1):
        data_cursos = read(
            database, opcionalidad=Opcionalidad.obligatorio, semestre=n_semestre)
        for element in data_cursos:
            count_creditos += element.creditos
            ls_cursos.append(element)
            pass
        pass

    list_cursos.render(ls_cursos)
    print('\nCreditos de cursos obligatorios: ' + str(count_creditos))
    pass
