# Controlador menu Principal

from views import main_menu
from controllers import load_files


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
                print('Opcion 2')
                pass
            # Conteo de creditos
            if value_select == 3:
                print('Opcion 3')
                pass
            # Mapa de cursos
            if value_select == 4:
                print('Opcion 4')
                pass
            pass
        pass
    pass
