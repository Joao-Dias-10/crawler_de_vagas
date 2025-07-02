from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from typing import List, Dict

from src.utils.config import USER_LINKEDIN, PASSWORD_LINKEDIN

class VagaColetor:
    def __init__(self, user: str = USER_LINKEDIN, password: str = PASSWORD_LINKEDIN):

        self.user = user
        self.password = password
        self.driver = self.configurar_driver()  # Usa a função configurar_driver
        self.wait = ui.WebDriverWait(self.driver, 60)

    def configurar_driver(self):
        """Configura o ChromeDriver com opções para suprimir logs indesejados."""
        chrome_options = Options()

        # Modo headless (sem interface gráfica)
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--disable-gpu")  # Desabilita aceleração de GPU
        chrome_options.add_argument("--no-sandbox")  # Ajuda em ambientes de container ou CI
        chrome_options.add_argument("--disable-software-rasterizer")  # Desabilita rasterizador de software
        chrome_options.add_argument("--log-level=3")  # Nível de log "ERROR" (suprime logs de INFO)
        chrome_options.add_argument("--disable-logging")  # Desabilita logs do ChromeDriver
        chrome_options.add_argument("--disable-extensions")  # Desabilita as extensões do Chrome

        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def login(self) -> None:
        """Realiza o login no LinkedIn."""
        self.driver.get("https://www.linkedin.com/login/pt")
        self.driver.maximize_window()

        user_element = self.wait.until(EC.visibility_of_element_located((By.NAME, "session_key")))
        user_element.send_keys(self.user)

        password_element = self.wait.until(EC.visibility_of_element_located((By.NAME, "session_password")))

        password_element.send_keys(self.password)
        password_element.send_keys(Keys.ENTER)

        # Validação de login
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "profile-card-member-details")))

    def coletar_vagas(self, palavra_chave: str) -> List[Dict]:
        """Coleta vagas do LinkedIn com base na palavra-chave fornecida."""
        self.login()
        self.driver.get(f"https://www.linkedin.com/jobs/search/?keywords={palavra_chave.replace(' ', '%20')}")

        # Esperar o carregamento das vagas
        ul_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sPjpgbyxyDBHcovoUDFvkPFkSAMhQIJkP')))

        vagas = []
        for i in range(1, 6):
            vaga = self._extrair_dados_vaga(i)
            vagas.append(vaga)

        self.driver.quit()
        return vagas

    def _extrair_dados_vaga(self, index: int) -> Dict:
        """Extrai os dados de uma vaga com base no índice na lista de vagas."""
        titulo = self.wait.until(EC.presence_of_element_located((By.XPATH, rf"/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{index}]/div/div/div[1]/div[1]/div[2]/div[1]/a/span[1]/strong"))).text
        empresa = self.wait.until(EC.presence_of_element_located((By.XPATH, rf"/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{index}]/div/div/div[1]/div[1]/div[2]/div[2]/span"))).text
        localizacao = self.wait.until(EC.presence_of_element_located((By.XPATH, rf"/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{index}]/div/div/div[1]/div[1]/div[2]/div[3]/ul/li/span"))).text
        url = self.wait.until(EC.presence_of_element_located((By.XPATH, rf"/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{index}]/div/div/div[1]/div[1]/div[2]/div[1]/a"))).get_attribute("href")

        return {
            "titulo": titulo,
            "empresa": empresa,
            "localizacao": localizacao,
            "url": url
        }
