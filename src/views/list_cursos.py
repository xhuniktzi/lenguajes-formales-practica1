# Vista listar cursos

def render(list_data):
    table_style = '{0} {1:6s} {0} {2:36s} {0} {3:24s} {0} {4:12s} {0} {5:8s} {0} {6:8s} {0} {7:9s} {0}'

    format_head = table_style.format(
        '|',
        'Codigo',
        'Nombre',
        'Pre-requisitos',
        'Opcionalidad',
        'Semestre',
        'Creditos',
        'Estado'
    )

    print(format_head)
    print('-'*128)

    for element in list_data:
        format_row = table_style.format(
            '|',
            str(element.codigo),
            element.nombre,
            str(element.codigo_requisitos),
            element.opcionalidad.name,
            str(element.semestre),
            str(element.creditos),
            element.estado.name
        )
        print(format_row)
        pass
    pass
