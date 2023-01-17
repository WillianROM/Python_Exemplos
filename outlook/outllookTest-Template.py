# https://www.youtube.com/watch?v=J3SiyMingRk&list=PLHnSLOMOPT11njaNmENJN6p2ro9MTc7t_&index=2&ab_channel=IzzyAnalytics
import win32com.client as client
import pathlib


anexo = str(pathlib.Path('happy-birthday.jpg').absolute())

outlook = client.Dispatch('Outlook.Application')
message = outlook.CreateItem(0)
message.Display()
message.to = 'teste@testando.com'
message.CC = 'testeCC@testando.com'
message.BCC = 'testeBCC@testando.com'
message.subject = 'Feliz aniversário'

message.Attachments.Add(anexo)

html_body = r"""
<body>
    <div>
        <h1 style="font-family: 'Lucida Handwriting'; font-size: 56; font-weight: bold; color: #9eac9c;">
            Feliz aniversário!
        </h1>
        <span style="font-family: 'Lucida Sans'; font-size: 28; color: #8d395c;">
           {}, desejo a você tudo de melhor no seu aniversário!!
            <p>Um grande abraço da esquipe da {}<p/>
        </span>
    </div><br>
    <div>
        <img src="C:\Users\Windows\Downloads\happy-birthday-916253_1920.jpg" with=50%>
    </div>
</body>

"""

html_body = html_body.format("Rafael", "Empresa dos Sonhos")
message.HTMLBody = html_body + message.HTMLBody

#message.Send()
