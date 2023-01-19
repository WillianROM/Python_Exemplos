#https://www.youtube.com/watch?v=J3SiyMingRk&list=PLHnSLOMOPT11njaNmENJN6p2ro9MTc7t_&index=2&ab_channel=IzzyAnalytics
import win32com.client as client
import os
from PIL import ImageGrab
import pandas as pd
import pathlib
import csv
from time import sleep

anexo_image_path = str(pathlib.Path('happy-birthday.jpg').absolute())
empresa = "Sonhos Company Ltda"

#################################################################################################
# Copiar e salvar o range do Excel como uma imagem para colocar no corpo do e-mail
nome_imagem_excel = 'paste.png'

workbook_path = os.getcwd() + '\\tabela.xlsx'
excel = client.Dispatch('Excel.Application')
wb = excel.Workbooks.Open(workbook_path)

# Dá para acessar a aba pelo item, index ou pelo nome:
#sheet = wb.Sheets.Item(1)
#sheet = wb.Sheets[0]
sheet = wb.Sheets['tabela']

excel.visible = 1

copyrange = sheet.Range('A1:B5')

copyrange.CopyPicture(Appearance=1, Format=2)

ImageGrab.grabclipboard().save(nome_imagem_excel)


excel_image_path = os.getcwd() + '\\' + nome_imagem_excel

excel.Quit()

#################################################################################################
# Copiar o range do Excel e colar no corpo do e-mail, no formato HTML

df = pd.read_excel('tabela.xlsx', index_col=False, nrows=5, usecols = "A:B")

tabela = df.to_html(index=False)


#################################################################################################

# Pegar base do arquivo CSV para enviar os e-mails

with open(r'baseEmails.csv', newline='') as f:
    reader = csv.reader(f)
    distro = [row for row in reader]


outlook = client.Dispatch('Outlook.Application')

for name, email in distro:
    message = outlook.CreateItem(0)
    message.Display()
    message.to = email
    message.CC = 'testeCC@testando.com'
    message.BCC = 'testeBCC@testando.com'
    message.subject = f'{name}, feliz aniversário'
    message.Attachments.Add(anexo_image_path)
    html_body = f"""
<body>
    <div>
        <h1 style="font-family: 'Lucida Handwriting'; font-size: 56; font-weight: bold; color: #9eac9c;">
            Feliz aniversário!
        </h1>
        <span style="font-family: 'Lucida Sans'; font-size: 28; color: #8d395c;">
           {name}, desejo a você tudo de melhor no seu aniversário!!
            <p>Um grande abraço da esquipe da {empresa}<p/>
        </span><br>
        <div>
           bolo
        </div>
        <div>
            <img src='{excel_image_path}' with=50%>
        </div><br>
        <div>
            {tabela}
        </div>
    </div><br>
</body>

"""

    message.HTMLBody = html_body + message.HTMLBody


#################################################################################################
# Adicionar SOMBRAS para a imagem no e-mail # https://www.youtube.com/watch?v=y7zEtV4yRVs&list=PLHnSLOMOPT11njaNmENJN6p2ro9MTc7t_&index=16&ab_channel=IzzyAnalytics
    inspector = message.GetInspector
    inspector.Display()
    doc = inspector.WordEditor

    selection = doc.Content
    selection.Find.Text = 'bolo'
    selection.Find.Execute()
    selection.text = ""

    img = selection.InlineShapes.AddPicture(anexo_image_path, 0, 1)
    shadow = img.Shadow
    shadow.Blur = 23
    shadow.Transparency = 0.35

    # tipo de sombras(shadow.Type):
    # flat - 1-20
    # outer - 21-29
    # inner - 30-38
    # perspective - 39-43
    shadow.Type = 21

#################################################################################################

    #message.Send()
    sleep(3)


# Download email attachments: https://github.com/israel-dryer/Outlook-Python-Tutorial/wiki/Download-email-attachments
# Reply emails: https://gist.github.com/israel-dryer/79dfa1b62e3015d0223e4fc072b7b410
