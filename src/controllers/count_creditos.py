# Controlador conteo de creditos

from views import count_creditos
from controllers import count_aprobados, count_cursando, count_pendientes, count_obligatorios, count_semestre


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
                count_aprobados.exec(database)
                pass
            # Creditos cursos cursando
            if value_select == 2:
                count_cursando.exec(database)
                pass
            # Creditos cursos pendientes
            if value_select == 3:
                count_pendientes.exec(database)
                pass
            # Creditos cursos obligatorios
            if value_select == 4:
                count_obligatorios.exec(database)
                pass
            # Creditos cursos semestre
            if value_select == 5:
                count_semestre.exec(database)
                pass
            pass
        pass
    pass
