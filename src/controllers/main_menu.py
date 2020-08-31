# Controlador menu Principal

from views import main_menu
from helpers.clear_screen import clear_screen
from controllers import load_files


def exec():
    database = list()
    value_select = 0
    while value_select != 5:
        main_menu.render()
        try:
            value_select = int(input())
            clear_screen()
            pass
        except ValueError:
            clear_screen()
            print('¡Valor invalido!')
            continue
        else:
            if value_select == 1:
                load_files.exec(database)
                pass
            if value_select == 2:
                print('Opcion 2')
                pass
            if value_select == 3:
                print('Opcion 3')
                pass
            if value_select == 4:
                print('Opcion 4')
                pass
            pass
        pass
    pass
