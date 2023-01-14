# Instalar o selenium e o webdriver-manager na máquina:
# pip install selenium
# pip install webdriver-manager
# pip install pandas
# pip install openpyxl

def pegar_tabela_do_site():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    # utilizar o webdriver-manager
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service

    import time
    import pandas as pd

    servico = Service(ChromeDriverManager().install()) # Para instalar o chormedriver conforme a versão atual do Chrome da máquina do usuário

    driver = webdriver.Chrome(service=servico)

    driver.maximize_window()

    driver.get("https://desafiosrpa.com.br/extrato.html")

    ids = driver.find_elements("xpath","//table[@id='example']/tbody/tr/td[1]")
    descricoes = driver.find_elements("xpath","//table[@id='example']/tbody/tr/td[2]")
    tipos = driver.find_elements("xpath","//table[@id='example']/tbody/tr/td[3]")
    valores = driver.find_elements("xpath","//table[@id='example']/tbody/tr/td[4]")
    datas = driver.find_elements("xpath","//table[@id='example']/tbody/tr/td[5]")


    population_result=[]

    for i in range(len(ids)):
        temporary_data = {'Id': ids[i].text,
                        'Descrição': descricoes[i].text,
                        'Tipo': tipos[i].text,
                        'Valor': valores[i].text,
                        'Data': datas[i].text}
        population_result.append(temporary_data)


    df_data = pd.DataFrame(population_result)

    df_data.to_excel('population_scraping_result.xlsx', index=False)
    df_data.to_csv('population_scraping_result.csv', index=False)

    return df_data
