# Funcion que maneja el graphviz

from graphviz import Digraph
from tempfile import NamedTemporaryFile
from helpers.database import read
from models.Estado import Estado
from models.Opcionalidad import Opcionalidad


def render_graph(database):
    temp = NamedTemporaryFile('w+')
    dot = Digraph('Pensum de estudios')
    dot.format = 'svg'
    dot.graph_attr['rankdir'] = 'LR'
    dot.node_attr['shape'] = 'rectangle'

    for element in read(database):
        for depends in element.codigo_requisitos:
            dot.edge(str(depends), str(element.codigo))
            pass
        if element.estado == Estado.aprobado:
            dot.node(str(element.codigo), element.nombre,
                     style='filled', color='#8eaadb')
            pass
        elif element.estado == Estado.cursando:
            dot.node(str(element.codigo), element.nombre,
                     style='filled', color='#92d050')
            pass
        elif element.estado == Estado.pendiente:
            dot.node(str(element.codigo), element.nombre,
                     style='filled', color='#bfbfbf')
            pass
        else:
            dot.node(str(element.codigo), element.nombre)
            pass
        pass

    dot.render(temp.name, view=True)
    pass
