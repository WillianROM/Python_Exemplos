# Instalar o selenium e o webdriver-manager na máquina:
# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# utilizar o webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time

servico = Service(ChromeDriverManager().install()) # Para instalar o chormedriver conforme a versão atual do Chrome da máquina do usuário

driver = webdriver.Chrome(service=servico)

driver.maximize_window()

driver.get("https://desafiosrpa.com.br/robo_etl.html")

assert "Alex Diogo - Site de Desafios RPA" in driver.title


driver.find_element("id","ID").send_keys("1234")

driver.find_element("css selector","#PNome").send_keys("João")

driver.find_element(By.CSS_SELECTOR,"#UNome").send_keys("Barro")

driver.find_element("xpath","//label[contains(text(),'Dt. Nascimento')]/..//input[@type='date']").send_keys("01/04/1988")

driver.find_element(By.XPATH,"//label[contains(text(),'Pessoal')]/../input[@type='radio']").click()

driver.find_element("class name", "custom-control-label").click()

driver.find_element(By.XPATH,"//label[@for='DTCREDITO']/following-sibling::div/input[@type='date']").send_keys("01/01/2023")

driver.find_element(By.ID, "btao").click()

time.sleep(5)

