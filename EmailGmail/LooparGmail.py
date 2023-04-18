#https://www.youtube.com/watch?v=3HnIB_AY6Kw&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=15&ab_channel=RonanVico

import imaplib
import email
import os
import base64

# Dados do Email
import DadosEmail

#Conectamos ao servidor do gmail com IMAP
objCon = imaplib.IMAP4_SSL("imap.gmail.com")

#Passamos o login e senha para entrar na caixa de emails
login = DadosEmail.login
senha = DadosEmail.senha


objCon.login(login, senha)

#Loopar a caixa de entrada
objCon.list()
objCon.select(mailbox='inbox', readonly=True)
resposta,idDosEmails = objCon.search(None,'All')

#loopando cada id de email na caixa de entrada
for num in idDosEmails[0].split():
    #decodificando o email e jogando em uma variável as partes do email
    resultado, dados = objCon.fetch(num,'RFC822')
    texto_do_email = dados[0][1]
    texto_do_email = texto_do_email.decode('utf-8')
    texto_do_email = email.message_from_string(texto_do_email )
    
    #Loopando as partes do email
    for part in texto_do_email.walk():
        # se tiver anexo, pegar o nome do anexo
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        #Pegamos nome do arquivo em anexo
        filename = part.get_filename()
        #Criamos um arquivo com o mesmo nome na pasta local
        arquivo = open(filename,'wb')
        #escrevemos o binário do anexo no arquivo
        arquivo.write(part.get_payload(decode=True))