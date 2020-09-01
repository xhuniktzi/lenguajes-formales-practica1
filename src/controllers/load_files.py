# Controlador menu carga de archivos

from views import load_files
from helpers.read_csv import read_csv
from helpers.database import create
from models.Curso import Curso
from models.Opcionalidad import Opcionalidad
from models.Estado import Estado


def exec(database):
    load_files.render()
    string_url_csv = input()
    file_csv = read_csv(string_url_csv)
    for element in file_csv:
        print(element.codigo_requisitos)
        create(database, element)
        pass
    pass
