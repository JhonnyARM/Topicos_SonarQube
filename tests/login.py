from unittest.mock import MagicMock
import pytest
from login_tests.microsoft_login_test import MicrosoftLoginTest

@pytest.fixture
def mock_driver():
    # Crea un mock del driver de Appium
    driver = MagicMock()
    driver.find_element.return_value = MagicMock()
    driver.find_element().click.return_value = None
    return driver

def test_microsoft_login_with_mock(mock_driver):
    # Instancia la clase con el driver mockeado
    login_handler = MicrosoftLoginTest(mock_driver)

    # Ejecuta el método de login
    login_handler.login("testuser@example.com", "password123")

    # Verifica que se llamaron los métodos esperados
    assert mock_driver.find_element.called
    assert mock_driver.find_element().click.called
