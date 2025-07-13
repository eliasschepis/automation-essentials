import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Inicializa ChromeDriver
    driver = webdriver.Chrome()

    # Maximiza la ventana para evitar errores por tamaño
    driver.maximize_window()

    # Navega a la URL base de tu app
    driver.get("https://www.saucedemo.com")

    # Devuelve el driver al test
    yield driver

    # Cierra el navegador al final del test
    driver.quit()
