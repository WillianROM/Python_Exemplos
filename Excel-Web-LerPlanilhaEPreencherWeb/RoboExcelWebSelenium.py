#https://www.youtube.com/watch?v=RCx21l73Vj8&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=17&ab_channel=RonanVico
# pip install selenium
# pip install webdriver-manager

import Site # Link do forms para preencher
import time
import pytest

####### Importações para ler o arquivo Excel
import pandas as pd

####### Importações para automatizar a web
from selenium import webdriver #navegaodor
from selenium.webdriver.common.by import By # Achar os elementos
from selenium.webdriver.common.keys import Keys # Para digitar no teclado na web

#######  Gerenciador de navegador
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# 0 - Ler o arquivo Excel
# 1 - Loopar Arquivo, Loopar cada linha do arquivo EXCEL
#   1.1 - Preencher os dados lidos para cada linha no navegador web

nome_do_arquivo = 'Contatos.xlsx'

df = pd.read_excel(nome_do_arquivo)

#print(df)

for index, row in df.iterrows():
    #print("Index: " +str(index) + " E o nome do fulano é " + row["NOME"])
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    
    driver.get(Site.site)
    try:
        BUTTON_INICIAR_AGORA = driver.find_element(By.XPATH,"//div[@id='form-main-content1']//button/div")
        BUTTON_INICIAR_AGORA.click()
    except:
        print("Botão 'Iniciar agora' não encontrado")
    else: 
        print("Botão 'Iniciar agora' encontrado")
    finally:
        INPUT_NOME = driver.find_element(By.XPATH,"//span[contains(text(),'Nome:')]/../../../..//input")
        INPUT_TELEFONE = driver.find_element(By.XPATH,"//span[contains(text(),'Telefone')]/../../../..//input")
        SPAN_NOTAS = driver.find_element(By.XPATH,"//span[@aria-label='" + str(row["NOTA"]) + " Star']")
        BUTTON_ENVIAR = driver.find_element(By.CSS_SELECTOR,"button[data-automation-id='submitButton']")
        
        INPUT_NOME.clear()
        INPUT_NOME.send_keys(row["NOME"])
        
        INPUT_TELEFONE.clear()
        INPUT_TELEFONE.send_keys(row["TELEFONE"])
        
        SPAN_NOTAS.click()
        
        BUTTON_ENVIAR.click()
        
        time.sleep(1)
        
        MESSAGE_THANK_YOU = driver.find_element(By.CSS_SELECTOR,"div[data-automation-id='thankYouMessage'] > span").get_attribute("textContent")
        
        driver.quit
        
        assert MESSAGE_THANK_YOU == "Sua resposta foi enviada."
        
        
        