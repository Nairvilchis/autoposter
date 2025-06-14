from flask import Flask
from routes import selenium_nodes  # Importa el blueprint
from selenium_utils import SeleniumManager
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
app.register_blueprint(selenium_nodes)  # Registra el blueprint

# Inicializa el SeleniumManager en modo headless
selenium_manager = SeleniumManager(headless=True)

@app.route('/')
def hello_world():
    return '¡Hola, mundo desde Flask!'

if __name__ == '__main__':
    app.run(debug=True)