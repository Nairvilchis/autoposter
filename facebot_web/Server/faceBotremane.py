import os
import pickle
import random
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

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
        
        # Banco de mensajes variados (personaliza según tu necesidad)
        self.message_bank = [
            """¡Hola comunidad! 👋

Acabo de descubrir esto y quería compartirlo con ustedes. 
¿Qué opinan al respecto?

#Compartiendo #Ideas""",

            """¿Alguien más ha probado esto? 

Me pareció interesante y quería saber sus experiencias. 
¡Los leo en los comentarios!

#Debate #Experiencias""",

            """¡Buen día a todos! 🌞

Comparto esta información que puede ser útil para la comunidad. 
Si tienen dudas, pregúntenme.

#Ayuda #Información""",

            """Pregunta rápida para la comunidad:

¿Cuál ha sido su experiencia con este tema? 
¡Aprendemos mucho compartiendo!

#Pregunta #Aprendizaje""",

            """¡Wow! 😮 

No puedo creer lo que acabo de encontrar. 
¿Ya lo conocían? 

#Descubrimiento #Comunidad"""
        ]

    def setup_driver(self):
        """Configura Chrome con opciones avanzadas"""
        options = Options()
        options.add_argument(f"user-data-dir={os.path.join(os.getcwd(), 'chrome_profile')}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 115)}.0.0.0 Safari/537.36")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def random_sleep(self, sleep_type='medium'):
        """Espera un tiempo aleatorio según tipo"""
        sleep_time = self.wait_times[sleep_type]
        print(f"⏳ Esperando {sleep_time:.1f} segundos...")
        time.sleep(sleep_time)

    def human_type(self, element, text):
        """Escribe texto como humano con variaciones"""
        actions = ActionChains(self.driver)
        for char in text:
            actions.send_keys(char)
            actions.pause(random.uniform(0.05, 0.3))
            # Ocasionalmente hace una pausa más larga
            if random.random() < 0.1:
                actions.pause(random.uniform(0.5, 1.2))
        actions.perform()

    def get_random_message(self):
        """Selecciona y modifica ligeramente un mensaje aleatorio"""
        base_msg = random.choice(self.message_bank)
        
        # Variaciones adicionales para hacer único cada mensaje
       # variations = [
        #    ("¡Hola", ["¡Hola", "Hola", "Hey", "Holi", "¡Buenas"]),
         #   ("😮", ["😮", "😯", "🤯", "😲", "¡Wow!"]),
         #   ("#Comunidad", ["#Comunidad", "#Grupo", "#Todos", "#Amigos"])
        #]
        
       # modified_msg = base_msg
        #for original, replacements in variations:
        #    if original in modified_msg:
         #       modified_msg = modified_msg.replace(original, random.choice(replacements), 1)
                
        return base_msg

    def manual_login(self):
        """Proceso de login manual con guardado de cookies"""
        print("\n🔵 Por favor completa el login manualmente (incluyendo 2FA)...")
        self.driver.get("https://www.facebook.com")
        
        input("✅ Presiona ENTER cuando hayas iniciado sesión completamente...")
        
        with open(self.cookies_file, 'wb') as file:
            pickle.dump(self.driver.get_cookies(), file)
        print("🔐 Cookies guardadas correctamente.")
        self.random_sleep('long')

    def load_cookies(self):
        """Carga cookies existentes para reutilizar sesión"""
        if os.path.exists(self.cookies_file):
            self.driver.get("https://www.facebook.com")
            with open(self.cookies_file, 'rb') as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    if 'domain' in cookie and '.facebook.com' in cookie['domain']:
                        self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.random_sleep('medium')
            
            # Verificar si el login persistió
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Facebook')]"))
                )
                return True
            except:
                return False
        return False

    def post_to_group(self, group_url, image_path=None):
        """Publicación automática con mensaje aleatorio"""
        try:
            # Verificar/Cargar sesión
            if not self.load_cookies():
                self.manual_login()

            print(f"\n🔄 Navegando al grupo: {group_url}")
            self.driver.get(group_url)
            
            # Esperar carga del grupo
            WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(@class, 'group')]"))
            )
            self.random_sleep('medium')

            # Seleccionar mensaje aleatorio
            message = self.get_random_message()
            print(f"✉ Mensaje seleccionado:\n---\n{message}\n---")

            # Localizar área de publicación
            post_area = WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH,
                    "//div[contains(@aria-label, 'Crear una publicación') or "
                    "contains(@aria-label, 'Escribe una publicación')]"))
            )
            
            # Movimiento humano para hacer clic
            ActionChains(self.driver).move_to_element(post_area).pause(1).click().perform()
            self.random_sleep('short')

            # Escribir mensaje
            text_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
            )
            self.human_type(text_box, message)
            self.random_sleep('short')

            # Subir imagen (opcional)
            if image_path and os.path.exists(image_path):
                print(f"📤 Subiendo imagen: {image_path}")
                try:
                    file_input = self.driver.find_elements(By.XPATH,
                        "//input[@type='file' and contains(@accept, 'image')]")[-1]  # Usar el último elemento
                    file_input.send_keys(os.path.abspath(image_path))
                    
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.XPATH,
                            "//div[contains(@aria-label, 'Foto') or contains(@aria-label, 'Imagen')]"))
                    )
                    self.random_sleep('medium')
                except Exception as e:
                    print(f"⚠ Error al subir imagen: {str(e)}")

            # Publicar con movimiento humano
            post_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,
                    "//div[contains(@aria-label, 'Publicar') and @role='button'] | "
                    "//span[contains(text(), 'Publicar')]/ancestor::div[@role='button']"))
            )
            
            # Hacer scroll y mover mouse aleatoriamente antes de publicar
            self.driver.execute_script("window.scrollBy(0, 200)")
            ActionChains(self.driver).move_by_offset(random.randint(0, 50), random.randint(0, 50)).perform()
            ActionChains(self.driver).move_to_element(post_button).pause(0.8).click().perform()
            
            # Verificación
            WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located((By.XPATH,
                    "//div[contains(text(), 'Publicación compartida') or "
                    "contains(text(), 'Tu publicación')]"))
            )
            print(f"✅ Publicación exitosa en {group_url}")
            self.random_sleep('xlong')

        except Exception as e:
            print(f"❌ Error en {group_url}: {str(e)}")
            self.take_screenshot("error")

    def take_screenshot(self, prefix="screenshot"):
        """Captura de pantalla para diagnóstico"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{prefix}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        print(f"📸 Captura guardada como: {filename}")

    def close(self):
        """Cierra el navegador correctamente"""
        print("\n🔴 Cerrando sesión...")
        self.driver.quit()

# Configuración y ejecución
if __name__ == "__main__":
    # Configuración (personalizar)
    print("entrando")
    
    
    CONFIG = {
        'groups': [
            'https://www.facebook.com/groups/139514976732492',
            'https://www.facebook.com/groups/550738879025440',
            'https://www.facebook.com/groups/493301607514323'
            'https://www.facebook.com/groups/1249443939267697'
            'https://www.facebook.com/groups/1612345032452561'
            'https://www.facebook.com/groups/136093930358072'
            'https://www.facebook.com/groups/1511243562477434'
            'https://www.facebook.com/groups/1533433056877812'
            'https://www.facebook.com/groups/318432308220899'
        ],
        'image_paths': [
            'img1.jpg',
            'img2.jpg',
            'img3.jpg',
            'img4.jpg',
            'img5.jpg',
            'img6.jpg',
            'img7.jpg',
            'img8.jpg',
            'img9.jpg',         
            'img1.png'
            #None  # Algunas publicaciones sin imagen
        ]
    }

    # Inicializar
    bot = FacebookAutoPoster()
    
    try:
        # Publicar en cada grupo con configuración aleatoria
        for group in CONFIG['groups']:
            # Seleccionar imagen aleatoria o None
            image_choice = random.choice(CONFIG['image_paths']) if CONFIG['image_paths'] else None
            
            bot.post_to_group(
                group_url=group,
                image_path=image_choice
            )
            
            # Espera variable entre publicaciones (5-15 minutos)
            wait_time = random.randint(300, 900)
            print(f"⏳ Esperando {wait_time//60} minutos antes de la próxima publicación...")
            time.sleep(wait_time)

    except KeyboardInterrupt:
        print("\n🛑 Detenido por el usuario")
    except Exception as e:
        print(f"\n💥 ERROR CRÍTICO: {str(e)}")
        bot.take_screenshot("critical_error")
    finally:
        bot.close()