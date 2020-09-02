# Controlador conteo de creditos

from views import count_creditos
from controllers import cursos_aprobados


def exec(database):
    value_select = 0
    while value_select != 6:
        count_creditos.render()
        try:
            value_select = int(input())
            pass
        except ValueError:
            print('¡Valor invalido!')
            continue
        else:
            # Creditos cursos aprobados
            if value_select == 1:
                cursos_aprobados.exec(database)
                pass
            # Creditos cursos cursando
            if value_select == 2:
                print('Opcion 2')
                pass
            # Creditos cursos pendientes
            if value_select == 3:
                print('Opcion 3')
                pass
            # Creditos cursos obligatorios
            if value_select == 4:
                print('Opcion 4')
                pass
            # Creditos cursos semestre
            if value_select == 5:
                print('Opcion 5')
                pass
            pass
        pass
    pass
