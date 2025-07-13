def test_login_valid_user(driver):  # El driver es una fixture
    login_page = LoginPage(driver)  # Instanciamos la clase LoginPage
    login_page.login("standard_user", "secret_sauce")  # Ejecutamos el flujo
    assert "inventory" in driver.current_url  # Verificamos redirección
