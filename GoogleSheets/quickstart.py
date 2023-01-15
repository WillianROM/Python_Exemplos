from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
import idPlanilhaTeste
SAMPLE_SPREADSHEET_ID = idPlanilhaTeste.id_Planilha # Id da planilha que será manipulado, deixei o id dessa planilha em outro arquivo py chamado idPlanilhaTeste que não vai ficar disponível no meu gitHub
SAMPLE_RANGE_NAME = 'abaTeste!A1:B14'


def main():
    creds = None

    # Essa parte é para ter acesso, se houver não houver token válido, utilizará as credenciais do arquivo json para gerar um nono token:

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

# Essa parte onde começa a fazer as manipulações do arquivo google sheets

    try:
        service = build('sheets', 'v4', credentials=creds) # Para criar um serviço

        # Call the Sheets API
        sheet = service.spreadsheets() # Definir um arquivo

        # result = sheet.values().get para let informações da planilha
        # result = sheet.values().update para adicionar/editar informações da planilha
        # https://developers.google.com/sheets/api/guides/values#python

        #GET
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        valores = result['values']
        print(valores)

        #UPDATE
        valores_adicionar = [
            ["dezembro", 'R$ 99.555,33'],
            ['janeiro', 'R$ 66.555,22']
        ]


        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="A13", valueInputOption="USER_ENTERED",
                                    body={'values': valores_adicionar}).execute()
                                    # RAW - The input is not parsed and is simply inserted as a string, so the input "=1+2" places the string "=1+2" in the cell, not a formula. (Non-string values like booleans or numbers are always handled as RAW.)
                                    # USER_ENTERED - The input is parsed exactly as if it were entered into the Google Sheets UI, so "Mar 1 2016" becomes a date, and "=1+2" becomes a formula. Formats may also be inferred, so "$100.15" becomes a number with currency formatting.

    # Adicionar uma nova coluna com os valores dos impostos
        # Pegar os valores atuais
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        valores = result['values']

        # Criar uma lista com o título da nova coluna
        valores_adicionar = [
            ["imposto"]
        ]

        # Cálcular os valores dos impostos por mês, transformando os valores das vendas em float e cálculando 10% e adicionando os valores dos impostos na lista criado anteriormente
        for i, linha in enumerate(valores): #Para pegar o índice
            if i > 0:
                vendas = linha [1]
                vendas = vendas.replace("R$ ","").replace(".","").replace(",",".")
                vendas = float(vendas) #Converter a String para Float
                imposto = vendas * 0.1
                valores_adicionar.append([imposto]) # Para adicionar itens a lista, lembrando que a variável deve estar entre colchetes []

        # Adicionar a nova coluna na planilha a partir da célula C1
        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="C1", valueInputOption="USER_ENTERED",
                                    body={'values': valores_adicionar}).execute()


    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
