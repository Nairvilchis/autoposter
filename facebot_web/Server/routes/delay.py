from flask import request, jsonify
from . import routes  # Importa el blueprint
import time

@routes.route('/delay', methods=['POST'])
def delay():
    data = request.get_json()
    delay_time = data.get('delay_time')

    if not delay_time or not isinstance(delay_time, (int, float)):
        return jsonify({'error': 'El tiempo de espera debe ser un número'}), 400

    try:
        time.sleep(delay_time)
        return jsonify({'message': f'Espera de {delay_time} segundos completada'}), 200
    except Exception as e:
        return jsonify({'error': f'Error durante la espera: {str(e)}'}), 500