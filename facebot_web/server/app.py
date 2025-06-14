from flask import Flask
from server.routes import selenium_nodes  # Importa el blueprint
from server.selenium_utils import SeleniumManager

app = Flask(__name__)
app.register_blueprint(selenium_nodes)  # Registra el blueprint

# Inicializa el SeleniumManager en modo headless
selenium_manager = SeleniumManager(headless=True)

@app.route('/')
def hello_world():
    return '¡Hola, mundo desde Flask!'

if __name__ == '__main__':
    app.run(debug=True)