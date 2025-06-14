from flask import Blueprint

selenium_nodes = Blueprint('selenium_nodes', __name__)

from . import selenium_nodes  # Importa las rutas de los nodos Selenium