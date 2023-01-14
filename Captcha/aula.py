# https://www.youtube.com/watch?v=Mdg1D-Kdmrw

# Leia o termo do serviço/política de privacidade dos sites.

# https://anti-captcha.com/pt (Serviço pago)

# https://google.com/recaptcha/api2/demo


# pip install selenium
# pip install webdriver-manager
# pip install anticaptchaofficial -> Para instalar a biblioteca do anti-captcha (https://anti-captcha.com/pt/apidoc/task-types/RecaptchaV2Task), lembrando que é serviço pago


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from anticaptchaofficial.recaptchav2proxyon import * # Verificar em documentações no site Anti-Captcha conforme o modelo de captcha

from chave import chave_api

url = "https://google.com/recaptcha/api2/demo"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get(url)

chave_captcha = driver.find_element(By.ID,'recaptcha-demo').get_attribute('data-sitekey') # No site procure por "data-sitekey", inspecione o elemento do captcha, para cima procure por iframe e em cima do iframe terá o div contendo o atributo "data-sitekey" 
# "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"

solver = recaptchaV2Proxyon()
solver.set_verbose(1) # Verbose = 0, enquanto o captcha está sendo resolvido, o código fica parado, sem printar nada, porém se o verbose for = 1 é printado os status da resolução do captcha
solver.set_key(chave_api) # Aqui é colocado a chave da API gerado no site ANTI CAPTCHA
solver.set_website_url(url)
solver.set_website_key(chave_captcha)

resposta = solver.solve_and_return_solution()

if resposta != 0:
    print("Resposta: " + resposta)
    # A resposta deve ser colocado na tag textarea que geralmente fica para baixo da tag div do captcha no html e o textarea é oculto no css com display como none
    # como o textarea é um campo oculto, é necessário enviar script através do javaScript:
    driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")

    driver.find_element(By.ID,'recaptcha-demo-submit').click()
    
else:
    print("Tarefa finalizado com erro: " + solver.error_code)



time.sleep(100)
