import pytest
from login_tests.utils.driver_utils import initialize_driver
from login_tests.microsoft_login_test import MicrosoftLoginTest

# Fixture para manejar el driver
@pytest.fixture
def driver():
    custom_des_cap = {
        "platformName": "Android",
        "appium:platformVersion": "11",
        "appium:deviceName": "emulator-5554",
        "appium:appPackage": "com.example.florales",
        "appium:appActivity": ".MainActivity",
        "app": "C:\\Users\\Usuario\\UniversidadLabs\\proyecto-si8811a-2024-ii-u1-desarrollomovil_corrales_viveros\\build\\app\\outputs\\flutter-apk\\app-debug.apk",
        "appium:noReset": True
    }

    driver = initialize_driver(user_input=custom_des_cap)
    yield driver
    driver.quit()

# Prueba del flujo de login
def test_microsoft_login(driver):
    login_handler = MicrosoftLoginTest(driver)

    try:
        login_handler.login("correo", "contraseña")
    except RuntimeError as e:
        pytest.fail(f"Error en el flujo de login: {e}")

    # Agregar validaciones adicionales si es posible
    assert driver.current_activity == ".MainActivity", "El login no redirigió correctamente"
