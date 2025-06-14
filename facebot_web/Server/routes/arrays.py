from flask import request, jsonify
from . import routes  # Importa el blueprint

# Diccionario para almacenar los arreglos (podríamos usar una base de datos en el futuro)
# Por ahora, lo almacenaremos en memoria
data_arrays = {}

@routes.route('/manage_array', methods=['POST'])
def manage_array():
    data = request.get_json()
    array_type = data.get('array_type')
    action = data.get('action')
    array_name = data.get('array_name')
    elements = data.get('elements')

    if not array_type or not action or not array_name or elements is None:
        return jsonify({'error': 'Faltan parámetros obligatorios'}), 400

    if array_type not in ['text', 'image']:
        return jsonify({'error': 'Tipo de arreglo no válido'}), 400

    if action not in ['create', 'add', 'replace']:
        return jsonify({'error': 'Acción no válida'}), 400

    if action == 'create':
        if array_name in data_arrays:
            return jsonify({'error': f'El arreglo "{array_name}" ya existe'}), 400
        data_arrays[array_name] = elements
        return jsonify({'message': f'Arreglo "{array_name}" creado exitosamente'}), 201

    elif action == 'add':
        if array_name not in data_arrays:
            return jsonify({'error': f'El arreglo "{array_name}" no existe'}), 404
        if not isinstance(data_arrays[array_name], list):
             return jsonify({'error': f'"{array_name}" no es un arreglo válido'}), 400
        data_arrays[array_name].extend(elements)
        return jsonify({'message': f'Elementos añadidos al arreglo "{array_name}"'}), 200

    elif action == 'replace':
        if array_name not in data_arrays:
            return jsonify({'error': f'El arreglo "{array_name}" no existe'}), 404
        if not isinstance(data_arrays[array_name], list):
             return jsonify({'error': f'"{array_name}" no es un arreglo válido'}), 400
        data_arrays[array_name] = elements
        return jsonify({'message': f'Arreglo "{array_name}" reemplazado exitosamente'}), 200

    return jsonify({'error': 'Acción no implementada'}), 501