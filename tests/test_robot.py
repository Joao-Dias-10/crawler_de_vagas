import pytest
from unittest.mock import MagicMock, patch
from src.automation.robot import VagaColetor  # Agora importamos a classe
from selenium.webdriver.common.by import By

@pytest.fixture
def mock_webdriver():
    with patch("selenium.webdriver.Chrome") as mock_chrome:
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        yield mock_driver

@pytest.fixture
def mock_wait():
    with patch("selenium.webdriver.support.ui.WebDriverWait") as mock_webdriver_wait:
        mock_wait_instance = MagicMock()
        mock_webdriver_wait.return_value = mock_wait_instance
        yield mock_wait_instance

@pytest.fixture
def mock_os_getenv():
    with patch("os.getenv") as mock_getenv:
        mock_getenv.side_effect = lambda x: {
            "USER_LINKEDIN": "test_user",
            "PASSWORD_LINKEDIN": "test_password"
        }.get(x)
        yield

# Teste para o sucesso da coleta de vagas
def test_coletar_vagas_sucesso(mock_webdriver, mock_wait, mock_os_getenv):
    mock_user_element = MagicMock()
    mock_password_element = MagicMock()
    mock_profile_card = MagicMock()
    mock_ul_element = MagicMock()

    side_effects = [
        mock_user_element,
        mock_password_element,
        mock_profile_card,
        mock_ul_element,
    ]

    # Agora adicionamos 4 mocks para cada uma das 5 vagas
    for i in range(1, 6):
        mock_title = MagicMock()
        mock_title.text = f"Título Vaga {i}"

        mock_company = MagicMock()
        mock_company.text = f"Empresa {i}"

        mock_location = MagicMock()
        mock_location.text = f"Localização {i}"

        mock_url = MagicMock()
        mock_url.get_attribute.return_value = f"http://url{i}.com"

        side_effects.extend([mock_title, mock_company, mock_location, mock_url])

    mock_wait.until.side_effect = side_effects

    # Instanciando a classe VagaColetor
    coletor = VagaColetor(user="test_user", password="test_password")

    # Chama o método de coleta de vagas
    vagas = coletor.coletar_vagas("Python remoto")

    # Verifica se o número de vagas coletadas é 5
    assert len(vagas) == 5
    assert vagas[0]["titulo"] == "Título Vaga 1"
    assert vagas[0]["empresa"] == "Empresa 1"
    assert vagas[0]["localizacao"] == "Localização 1"
    assert vagas[0]["url"] == "http://url1.com"
    assert vagas[4]["titulo"] == "Título Vaga 5"
    assert vagas[4]["url"] == "http://url5.com"

    # Verifica se os campos de login estão sendo preenchidos
    mock_user_element.send_keys.assert_called_with("test_user")
    mock_password_element.send_keys.assert_any_call("test_password")

    # Verifica se o método quit foi chamado no driver
    mock_webdriver.quit.assert_called_once()
