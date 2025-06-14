from flask import request, jsonify
from . import selenium_nodes
from server.selenium_utils import SeleniumManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Obtener la instancia del SeleniumManager
selenium_manager = SeleniumManager()

@selenium_nodes.route('/navigate', methods=['POST'])
def navigate():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'La URL es obligatoria'}), 400

    try:
        selenium_manager.navigate(url)
        return jsonify({'message': f'Navegando a {url}'}), 200
    except Exception as e:
        return jsonify({'error': f'Error al navegar a la URL: {str(e)}'}), 500

@selenium_nodes.route('/find_element', methods=['POST'])
def find_element():
    data = request.get_json()
    selector = data.get('selector')
    selector_type = data.get('selector_type')
    timeout = data.get('timeout', 10)

    if not selector or not selector_type:
        return jsonify({'error': 'El selector y el tipo de selector son obligatorios'}), 400

    if selector_type not in ['CSS', 'XPATH']:
        return jsonify({'error': 'Tipo de selector no válido (debe ser CSS o XPATH)'}), 400

    try:
        by = By.CSS_SELECTOR if selector_type == 'CSS' else By.XPATH
        element = WebDriverWait(selenium_manager.driver, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
        # Para simplificar, no devolvemos el elemento directamente
        # En su lugar, devolvemos un identificador único del elemento
        element_id = str(id(element))
        return jsonify({'message': f'Elemento encontrado con ID {element_id}'}), 200
    except Exception as e:
        return jsonify({'error': f'Error al encontrar el elemento: {str(e)}'}), 500

@selenium_nodes.route('/click_element', methods=['POST'])
def click_element():
    data = request.get_json()
    element_id = data.get('element_id')

    if not element_id:
        return jsonify({'error': 'El ID del elemento es obligatorio'}), 400

    try:
        # Aquí, en una implementación real, buscarías el elemento usando el element_id
        # Por simplicidad, este ejemplo no implementa la búsqueda del elemento
        # Asumimos que el elemento existe y está disponible

        #element = selenium_manager.driver.find_element(By.ID, element_id)
        #element.click()
        return jsonify({'message': f'Elemento con ID {element_id} clickeado'}), 200
    except Exception as e:
        return jsonify({'error': f'Error al hacer clic en el elemento: {str(e)}'}), 500

@selenium_nodes.route('/enter_text', methods=['POST'])
def enter_text():
    data = request.get_json()
    element_id = data.get('element_id')
    text = data.get('text')
    clear = data.get('clear', True)

    if not element_id or not text:
        return jsonify({'error': 'El ID del elemento y el texto son obligatorios'}), 400

    try:
        # Aquí, en una implementación real, buscarías el elemento usando el element_id
        # Por simplicidad, este ejemplo no implementa la búsqueda del elemento
        # Asumimos que el elemento existe y está disponible
        #element = selenium_manager.driver.find_element(By.ID, element_id)
        #if clear:
        #    element.clear()
        #element.send_keys(text)
        return jsonify({'message': f'Texto ingresado en el elemento con ID {element_id}'}), 200
    except Exception as e:
        return jsonify({'error': f'Error al ingresar el texto: {str(e)}'}), 500

@selenium_nodes.route('/get_text', methods=['POST'])
def get_text():
    data = request.get_json()
    element_id = data.get('element_id')

    if not element_id:
        return jsonify({'error': 'El ID del elemento es obligatorio'}), 400

    try:
        # Aquí, en una implementación real, buscarías el elemento usando el element_id
        # Por simplicidad, este ejemplo no implementa la búsqueda del elemento
        # Asumimos que el elemento existe y está disponible
        #element = selenium_manager.driver.find_element(By.ID, element_id)
        #text = element.text
        return jsonify({'message': f'Texto obtenido del elemento con ID {element_id}'}), 200
    except Exception as e:
        return jsonify({'error': f'Error al obtener el texto del elemento: {str(e)}'}), 500
    
@selenium_nodes.route('/get_attribute', methods=['POST'])
def get_attribute():
    data = request.get_json()
    element_id = data.get('element_id')
    attribute_name = data.get('attribute_name')

    if not element_id or not attribute_name:
        return jsonify({'error': 'El ID del elemento y el nombre del atributo son obligatorios'}), 400

    try:
        # Aquí, en una implementación real, buscarías el elemento usando el element_id
        # Por simplicidad, este ejemplo no implementa la búsqueda del elemento
        # Asumimos que el elemento existe y está disponible
        #element = selenium_manager.driver.find_element(By.ID, element_id)
        #attribute_value = element.get_attribute(attribute_name)
        return jsonify({'message': f'Atributo obtenido del elemento con ID {element_id}'}), 200
    except Exception as e:
        return jsonify({'error': f'Error al obtener el atributo del elemento: {str(e)}'}), 500

@selenium_nodes.route('/execute_javascript', methods=['POST'])
def execute_javascript():
    data = request.get_json()
    script = data.get('script')

    if not script:
        return jsonify({'error': 'El código Javascript es obligatorio'}), 400

    try:
        #result = selenium_manager.driver.execute_script(script)
        return jsonify({'message': f'Javascript ejecutado correctamente'}), 200
    except Exception as e:
        return jsonify({'error': f'Error al ejecutar el Javascript: {str(e)}'}), 500

@selenium_nodes.route('/upload_file', methods=['POST'])
def upload_file():
    data = request.get_json()
    element_id = data.get('element_id')
    file_path = data.get('file_path')

    if not element_id or not file_path:
        return jsonify({'error': 'El ID del elemento y la ruta del archivo son obligatorios'}), 400

    try:
        # Aquí, en una implementación real, buscarías el elemento usando el element_id
        # Por simplicidad, este ejemplo no implementa la búsqueda del elemento
        # Asumimos que el elemento existe y está disponible
        #element = selenium_manager.driver.find_element(By.ID, element_id)
        #element.send_keys(file_path)
        return jsonify({'message': f'Archivo subido correctamente al elemento con ID {element_id}'}), 200
    except Exception as e:
        return jsonify({'error': f'Error al subir el archivo: {str(e)}'}), 500