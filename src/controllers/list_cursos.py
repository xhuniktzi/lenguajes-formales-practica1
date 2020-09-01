# Controlador listar cursos

from helpers.database import read
from views import list_cursos


def exec(database):
    ls_cursos = read(database)
    list_cursos.render(ls_cursos)
    pass
