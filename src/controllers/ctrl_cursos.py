# Controlador gestion de cursos

from views import ctrl_cursos
from controllers import list_cursos, view_curso, add_cursos, edit_cursos, delete_cursos


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
                view_curso.exec(database)
                pass
            # Agregar cursos
            if value_select == 3:
                add_cursos.exec(database)
                pass
            # Editar cursos
            if value_select == 4:
                edit_cursos.exec(database)
                pass
            # Eliminar cursos
            if value_select == 5:
                delete_cursos.exec(database)
                pass
            pass
        pass
    pass
