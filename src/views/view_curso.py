# Vista mostrar curso

def render(curso):
    print('Codigo: ' + str(curso.codigo))
    print('Nombre: ' + curso.nombre)
    print('pre-requisitos: ' + str(curso.codigo_requisitos))
    print('Opcionalidad: ' + curso.opcionalidad.name)
    print('Semestre: ' + str(curso.semestre))
    print('Creditos: ' + str(curso.creditos))
    print('Estado: ' + curso.estado.name)
    pass
