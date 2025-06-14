from flask import request, jsonify
from . import routes  # Importa el blueprint
# Importar la instancia de fb_poster desde app.py
from app import fb_poster
import random
import os

@routes.route('/post_group', methods=['POST'])
def post_group():
    data = request.get_json()
    group_url = data.get('group_url')
    message_type = data.get('message_type', 'custom')  # Por defecto, mensaje personalizado
    message_index = data.get('message_index', 0)
    custom_message = data.get('custom_message', '')
    image_path = data.get('image_path')

    if not fb_poster.driver:
        return jsonify({'error': 'Debes iniciar sesión primero'}), 400

    if not group_url:
        return jsonify({'error': 'La URL del grupo es obligatoria'}), 400

    message = ""
    if message_type == 'predefined':
        if message_index < 0 or message_index >= len(fb_poster.message_bank):
            return jsonify({'error': 'Índice de mensaje predefinido no válido'}), 400
        message = fb_poster.message_bank[message_index]
    elif message_type == 'custom':
        if not custom_message:
            return jsonify({'error': 'El mensaje personalizado es obligatorio'}), 400
        message = custom_message
    else:
        return jsonify({'error': 'Tipo de mensaje no válido'}), 400

    # Validar si la imagen existe
    if image_path and not os.path.exists(image_path):
        return jsonify({'error': 'La ruta de la imagen no es válida'}), 400

    try:
        fb_poster.post_to_group(group_url, message, image_path)
        return jsonify({'message': 'Publicación exitosa'}), 200
    except Exception as e:
        return jsonify({'error': f'Error al publicar en el grupo: {str(e)}'}), 500