#https://www.youtube.com/watch?v=RCx21l73Vj8&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=17&ab_channel=RonanVico
# pip install playwright

import Site # Link do forms para preencher
import time
import pytest

####### Importações para ler o arquivo Excel
import pandas as pd

####### Importações para automatizar a web
from playwright.sync_api import sync_playwright


# 0 - Ler o arquivo Excel
# 1 - Loopar Arquivo, Loopar cada linha do arquivo EXCEL
#   1.1 - Preencher os dados lidos para cada linha no navegador web

nome_do_arquivo = 'Contatos.xlsx'

df = pd.read_excel(nome_do_arquivo)

#print(df)

for index, row in df.iterrows():
    #print("Index: " +str(index) + " E o nome do fulano é " + row["NOME"])
    
    with sync_playwright() as p:
        # Abrindo o navegador
        driver = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = driver.new_context(no_viewport=True)
        
        page = context.new_page()
           
        page.goto(Site.site)
        
        time.sleep(3)
        
        try:
            BUTTON_INICIAR_AGORA = "div#form-main-content1 button div"
            page.click(BUTTON_INICIAR_AGORA)
            
        except:
            print("Botão 'Iniciar agora' não encontrado")
        else: 
            print("Botão 'Iniciar agora' encontrado")
        finally:
            INPUT_NOME = "input[placeholder='Insira sua resposta']"
            INPUT_TELEFONE = "input[placeholder='O valor deve ser um número']"
            SPAN_NOTAS = "span[aria-label='" + str(row["NOTA"]) + " Star']"
            BUTTON_ENVIAR = "button[data-automation-id='submitButton']"
            
            
            
            page.fill(INPUT_NOME, row["NOME"])
            page.fill(INPUT_TELEFONE, str(row["TELEFONE"]))
            page.click(SPAN_NOTAS)
            page.click(BUTTON_ENVIAR)        
            
            time.sleep(1)
            
            MESSAGE_THANK_YOU = page.text_content("div[data-automation-id='thankYouMessage'] > span")
            
            driver.close()
            
            assert MESSAGE_THANK_YOU == "Sua resposta foi enviada."
            
        
        