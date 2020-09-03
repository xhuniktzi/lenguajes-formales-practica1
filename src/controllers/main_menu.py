# Controlador menu Principal

from views import main_menu
from controllers import load_files, ctrl_cursos, count_creditos, graphviz


def exec():
    database = list()
    value_select = 0
    while value_select != 5:
        main_menu.render()
        try:
            value_select = int(input())
            pass
        except ValueError:
            print('¡Valor invalido!')
            continue
        else:
            # Cargar archivo csv
            if value_select == 1:
                load_files.exec(database)
                pass
            # Gestionar cursos
            if value_select == 2:
                ctrl_cursos.exec(database)
                pass
            # Conteo de creditos
            if value_select == 3:
                count_creditos.exec(database)
                pass
            # Mapa de cursos
            if value_select == 4:
                graphviz.exec(database)
                pass
            pass
        pass
    pass
