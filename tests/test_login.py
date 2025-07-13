# Importamos los localizadores por tipo (ID, XPATH, etc.)
from selenium.webdriver.common.by import By

# Importamos el driver base para tipar correctamente
from selenium.webdriver.remote.webdriver import WebDriver

# Esperas explícitas para asegurar que los elementos estén presentes/interactuables
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test

def test_login_valid_user(driver):  # El driver es una fixture
    login_page = LoginPage(driver)  # Instanciamos la clase LoginPage
    login_page.login("standard_user", "secret_sauce")  # Ejecutamos el flujo
    assert "inventory" in driver.current_url  # Verificamos redirección
