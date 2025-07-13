# Importamos los localizadores por tipo (ID, XPATH, etc.)
from selenium.webdriver.common.by import By

# Importamos el driver base para tipar correctamente
from selenium.webdriver.remote.webdriver import WebDriver

# Esperas explícitas para asegurar que los elementos estén presentes/interactuables
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    # ========================
    # DEFINICIÓN DE LOCATORS
    # ========================
    USERNAME_INPUT = (By.ID, "user-name")       # Campo de usuario
    PASSWORD_INPUT = (By.ID, "password")        # Campo de contraseña
    LOGIN_BUTTON = (By.ID, "login-button")      # Botón para iniciar sesión
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")  # Mensaje de error

    # ========================
    # MÉTODOS DE ACCIÓN
    # ========================

    def enter_username(self, username):
        # Espera a que el campo de usuario sea visible y escribe el texto
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(username)

    def enter_password(self, password):
        # Espera a que el campo de contraseña sea visible y escribe el texto
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)

    def click_login(self):
        # Espera a que el botón sea clickeable y hace click
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, username, password):
        # Método compuesto: ejecuta todo el flujo de login
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        # Devuelve el texto del mensaje de error, si aparece
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text


# Hacer click en un elemento
self.wait.until(EC.element_to_be_clickable(locator)).click()

# Escribir texto en un input
self.wait.until(EC.visibility_of_element_located(locator)).send_keys("mi texto")

# Obtener texto de un elemento
texto = self.wait.until(EC.visibility_of_element_located(locator)).text

# Verificar visibilidad
es_visible = self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

# Obtener atributo específico (por ejemplo, value)
valor = self.driver.find_element(*locator).get_attribute("value")
