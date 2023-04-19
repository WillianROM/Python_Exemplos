#https://www.youtube.com/watch?v=zazI9ntX6dw&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=15&ab_channel=RonanVico
#pip install playwright
#playwright install

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://google.com.br")
    print(page.title())
    
    #Digitar algo no textarea
    page.fill("textarea[name='q']",'algo')
       
    #Clicar no botão pesquisar
    page.click('input[name="btnK"]')
    
    
    page.wait_for_timeout(5000)
    time.sleep(20)
    #browser.close()