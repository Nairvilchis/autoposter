from flask import Flask, request, jsonify
import os
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
from selenium.webdriver.common.action_chains import ActionChains

app = Flask(__name__)

# Aquí deberías inicializar tu clase FacebookAutoPoster
# Esto es solo un ejemplo, asegúrate de adaptarlo a tu código real
class FacebookAutoPoster:
    def __init__(self):
        self.cookies_file = "fb_cookies.pkl"
        self.setup_driver()
        self.wait_times = {
            'micro': random.uniform(0.1, 0.5),
            'short': random.uniform(1, 3),
            'medium': random.uniform(3, 7),
            'long': random.uniform(8, 15),
            'xlong': random.uniform(20, 40)
        }
        self.driver = None

    def setup_driver(self):
        """Configura Chrome con opciones avanzadas"""
        options = Options()
        options.add_argument(
            f"user-data-dir={os.path.join(os.getcwd(), 'chrome_profile')}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument(
            f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 115)}.0.0.0 Safari/537.36")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def load_cookies(self):
        """Carga cookies existentes para reutilizar sesión"""
        if os.path.exists(self.cookies_file):
            self.driver.get("https://www.facebook.com")
            try:
                with open(self.cookies_file, 'rb') as file:
                    cookies = pickle.load(file)
                    for cookie in cookies:
                        if 'domain' in cookie and '.facebook.com' in cookie['domain']:
                            self.driver.add_cookie(cookie)
                self.driver.refresh()
                return True
            except Exception as e:
                print(f"Error loading cookies: {e}")
                return False
        return False

    def manual_login(self):
        """Proceso de login manual con guardado de cookies"""
        print("\n🔵 Por favor completa el login manualmente (incluyendo 2FA)...")
        self.driver.get("https://www.facebook.com")

        input("✅ Presiona ENTER cuando hayas iniciado sesión completamente...")

        with open(self.cookies_file, 'wb') as file:
            pickle.dump(self.driver.get_cookies(), file)
        print("🔐 Cookies guardadas correctamente.")
        return True

    def close(self):
        """Cierra el navegador correctamente"""
        if self.driver:
            print("\n🔴 Cerrando sesión...")
            self.driver.quit()

# Crear una instancia de FacebookAutoPoster (esto puede depender de cómo quieres manejar la sesión)
fb_poster = FacebookAutoPoster()

@app.route('/login', methods=['POST'])
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

@app.route('/')
def hello_world():
    return '¡Hola, mundo desde Flask!'

if __name__ == '__main__':
    app.run(debug=True)
