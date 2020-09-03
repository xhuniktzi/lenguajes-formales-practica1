# Controlador de graphviz

from helpers.database import read
from helpers.view_graph import render_graph


def exec(database):
    if len(read(database)) != 0:
        render_graph(database)
        pass
    else:
        print('No hay items registrados')
        pass
    pass
