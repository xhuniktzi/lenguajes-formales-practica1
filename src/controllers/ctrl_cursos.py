# Controlador gestion de cursos

from views import ctrl_cursos
from controllers import list_cursos


def exec(database):
    value_select = 0
    while value_select != 6:
        ctrl_cursos.render()
        try:
            value_select = int(input())
            pass
        except ValueError:
            print('¡Valor invalido!')
            continue
        else:
            # Listar cursos
            if value_select == 1:
                list_cursos.exec(database)
                pass
            # Mostrar cursos
            if value_select == 2:
                print('Opcion 2')
                pass
            # Agregar cursos
            if value_select == 3:
                print('Opcion 3')
                pass
            # Editar cursos
            if value_select == 4:
                print('Opcion 4')
                pass
            # Eliminar cursos
            if value_select == 5:
                print('Opcion 5')
                pass
            pass
        pass
    pass
