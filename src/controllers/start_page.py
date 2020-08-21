# Controlador pantalla de Inicio

from views import start_page
from helpers.clear_screen import clear_screen


def exec():
    clear_screen()
    start_page.render()
    input()
    pass
