from flask import jsonify
from . import routes  # Importa el blueprint
# Importar la instancia de fb_poster desde app.py
from app import fb_poster

@routes.route('/get_groups', methods=['GET'])
def get_groups():
    if not fb_poster.driver:
        return jsonify({'error': 'Debes iniciar sesión primero'}), 400

    group_urls = fb_poster.get_groups()
    return jsonify({'groups': group_urls}), 200