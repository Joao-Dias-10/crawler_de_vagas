from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import os
import time
import re

from src.utils.configsAll import *


def coletar_vagas(palavra_chave):
    driver = webdriver.Chrome()
    wait = ui.WebDriverWait(driver, 30)
    driver.get("https://www.linkedin.com/login/pt")
    driver.maximize_window()

    user = wait.until(EC.visibility_of_element_located((By.NAME, "session_key")))
    user.send_keys(os.getenv('USER_LINKEDIN'))

    password = wait.until(EC.visibility_of_element_located((By.NAME, "session_password")))
    password.send_keys(os.getenv('PASSWORD_LINKEDIN'))
    password.send_keys(Keys.ENTER)

    # Validação de login
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "profile-card-member-details")))

    driver.get(f"https://www.linkedin.com/jobs/search/?keywords={palavra_chave.replace(' ', '%20')}")
    time.sleep(5)  

    vagas = []

    # Esperar a lista de vagas carregar
    ul_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'XLsfDgRPWWqswmzbPfSkbwlIWKwwAGMMWV')))

    for i in range(1,6):
            # Procurar elementos que contenham as classes esperadas (mesmo que parcialmente)
            titulo = wait.until(EC.presence_of_element_located((By.XPATH, rf"/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{i}]/div/div/div[1]/div[1]/div[2]/div[1]/a/span[1]/strong"))).text
            empresa = wait.until(EC.presence_of_element_located((By.XPATH, rf"/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{i}]/div/div/div[1]/div[1]/div[2]/div[2]/span"))).text
            localizacao = wait.until(EC.presence_of_element_located((By.XPATH, rf"/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{i}]/div/div/div[1]/div[1]/div[2]/div[3]/ul/li/span"))).text
            url = wait.until(EC.presence_of_element_located((By.XPATH, rf"/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{i}]/div/div/div[1]/div[1]/div[2]/div[1]/a"))).get_attribute("href")

            vagas.append({
                "titulo": titulo,   
                "empresa": empresa,
                "localizacao": localizacao,
                "url": url
            })

    driver.quit()
    return vagas
