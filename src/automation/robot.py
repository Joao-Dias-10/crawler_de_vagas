from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 

import os

from src.utils.configsAll import *



def coletar_vagas(palavra_chave):

    driver = webdriver.Chrome()
    driver.get(f"https://www.linkedin.com/login/pt")
    driver.maximize_window()

    user = WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.NAME, "session_key")))
    user.send_keys(os.getenv('USER_LINKEDIN'))
    password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "session_password")))
    password.send_keys(os.getenv('PASSWORD_LINKEDIN'))
    password.send_keys(Keys.ENTER)

    nomeUserVlidacaoDeAcesso = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "profile-card-member-details")))

    driver.get(f"https://www.linkedin.com/jobs/search/?keywords={palavra_chave.replace(' ', '%20')}")
    vagas = []
    elementos = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul')))
    elementos = driver.find_elements(By.XPATH, '/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul')[:5]
    for el in elementos:
        try:
            titulo = el.find_element(By.TAG_NAME, 'a').get_attribute('href')
            empresa = el.find_element(By.TAG_NAME, 'a').get_attribute('href')
            localizacao = el.find_element(By.TAG_NAME, 'a').get_attribute('href')
            url = el.find_element(By.TAG_NAME, 'a').get_attribute('href')
            vagas.append({
                "titulo": titulo,
                "empresa": empresa,
                "localizacao": localizacao,
                "url": url
            })
        except:
            continue

    driver.quit()
    return vagas
