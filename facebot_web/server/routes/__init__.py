from flask import Blueprint

selenium_nodes = Blueprint('selenium_nodes', __name__)

from . import selenium_nodes