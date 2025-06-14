from flask import request, jsonify
from . import routes  # Importa el blueprint
# Importar la instancia de fb_poster desde app.py
from app import fb_poster

@routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    login_type = data.get('login_type')
    cookies_file = data.get('cookies_file')

    if not fb_poster.driver:
        fb_poster.setup_driver()  # Asegúrate de que el driver esté inicializado

    if login_type == 'cookies':
        if cookies_file:
            fb_poster.cookies_file = cookies_file
        success = fb_poster.load_cookies()
    elif login_type == 'manual':
        success = fb_poster.manual_login()
    else:
        return jsonify({'error': 'Tipo de inicio de sesión no válido'}), 400

    if success:
        return jsonify({'message': 'Inicio de sesión exitoso'}), 200
    else:
        return jsonify({'error': 'Inicio de sesión fallido'}), 400