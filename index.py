import time
import os
import subprocess
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do WebDriver do Chrome
driver = webdriver.Chrome()

# Abrir o site do Roblox
driver.get("https://www.roblox.com/login")

# Encontrar o campo de e-mail pelo ID e digitar o e-mail desejado
email_field = driver.find_element(By.ID, "login-username")
senha_field = driver.find_element(By.ID, "login-password")
email_field.send_keys('meu_eggnasuaboca')
senha_field.send_keys('bR@268412345')

# Encontrar e clicar no botão de login pelo ID
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Aguardar a página carregar após o login
time.sleep(5)

# Encontrar o campo de busca pelo ID e digitar o texto desejado (por exemplo, "blox fruit")
busca_field = driver.find_element(By.ID, "navbar-search-input")
busca_texto = "blox fruit"
busca_field.send_keys(busca_texto)

# Pressionar Enter para realizar a busca
busca_field.send_keys(Keys.RETURN)

# Aguardar alguns segundos para visualizar o resultado da busca
time.sleep(5)

# Encontrar e clicar no botão de jogar pelo atributo data-testid
play_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='play-button']")
play_button.click()

# Aguardar alguns segundos para visualizar o resultado do clique
time.sleep(5)

# Encontrar e clicar no botão "confirm-btn" para iniciar o download
install = driver.find_element(By.ID, "confirm-btn")
install.click()

# Aguardar alguns segundos para o download ser concluído
time.sleep(20)

# Localização do arquivo baixado usando a função os.path.expanduser para corrigir espaços no caminho do usuário
download_path = os.path.expanduser("~\\Downloads")
downloaded_file = "RobloxPlayerLauncher.exe"

# Verificar se o arquivo baixado está presente na pasta de downloads
if os.path.exists(os.path.join(download_path, downloaded_file)):
    print("Roblox Player Launcher instalado com sucesso.")
else:
    # Aguardar até que o alerta do navegador seja exibido
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())

    # Aceitar o alerta
    alert.accept()

    # Aguardar alguns segundos para a instalação ser concluída
    time.sleep(10)

    # Encontrar a posição do botão "Abrir Roblox" no alerta do navegador e clicar nessa posição
    # Você pode precisar ajustar as coordenadas de acordo com a posição do botão em sua tela
    x, y = pyautogui.locateCenterOnScreen("open_roblox_button.png")
    pyautogui.click(x, y)

# Fechar o navegador
driver.quit()
