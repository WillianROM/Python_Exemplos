# https://www.youtube.com/watch?v=umvzsQLZYD4&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=8&ab_channel=RonanVico

# SMTP - Simple Mail Transfer Protocol
# Para criar o servidor e enviar o e-mail
import smtplib

#MIME - Norma de envio de emails pela internet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#MIME - Para anexar arquivos no email
from email.mime.base import MIMEBase
from email import encoders


# Dados do Email
import DadosEmail


#1 - STARTAR O SRVIDOR SMTP
host = DadosEmail.HostDoEmail
port = DadosEmail.PortaDoEmail
login = DadosEmail.EnderecoEmail
senha = DadosEmail.SenhaDoEmail

# Dando start no servidor
server = smtplib.SMTP(host, port)

server.ehlo
server.starttls
server.login(login,senha)


#2 - CONSTRUIR O EMIAL TIPO MIME

email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = login
email_msg['Subject'] = "Email enviado pelo Python<"

corpo = "<strong>Olá, tudo bem?</strong>"

#email_msg.attach(MIMEText(corpo, 'plain'))
email_msg.attach(MIMEText(corpo, 'html'))

#Anexo
#Abrir o arquivo em modo leitura e binary
cam_arquivo = "Teste.xlsx"
attachment = open(cam_arquivo,'rb')

#Ler o arquivo no modo binário e converter para BASE64 (que é o que o email precisa)
att = MIMEBase('application', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

#Adicionar o cabeçalho no tipo anexo de email
att.add_header('Content-Disposition', f'attachment; filename=Teste.xlsx')
#fecha o arquivo
attachment.close()
#coloca o anexo no corpo do email
email_msg.attach(att)


#3 - ENVIAR O EMAIL tipo MIME no SERVIDOR SMTP
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

server.quit()
