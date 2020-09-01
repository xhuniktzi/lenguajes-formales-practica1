# Controlador menu carga de archivos

from views import load_files
from helpers.read_csv import read_csv
from helpers.database import create


def exec(database):
    load_files.render()
    string_url_csv = input()
    file_csv = read_csv(string_url_csv)
    for element in file_csv:
        create(database, element)
        pass
    pass
