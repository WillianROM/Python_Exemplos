#pip install pywinauto
import time
from pywinauto.application import Application

app = Application(backend='uia').start(r'notepad.exe') # Para abrir o aplicativo
app = Application(backend='uia').connect(title='Sem título - Bloco de Notas', timeout=20) # Para conectar o aplicativo

window = app.SemTituloBlocoDeNotas
window.set_focus()

#window.print_control_identifiers() # Para ver os identificadores dos elementos do aplicativo (Lembrando que depois do app. vem o nome do título do aplicativo sem espaços e traços)

textEditor = window.child_window(title="Editor de Texto", auto_id="15", control_type="Edit").wrapper_object()
textEditor.type_keys("Hello, World! How are you, guys? João e José, vocês são legais.", with_spaces = True) # É necessário colocar with_spaces = True para ser digitado os espaços

""" fileMenu = window.child_window(title="Arquivo", control_type="MenuItem").wrapper_object()
fileMenu.click_input() # Clique usando o mouse, tem ótima funcionalidade

time.sleep(1)

close = window.child_window(title="Sair", auto_id="7", control_type="MenuItem").wrapper_object()
close.click_input() """

app.SemTituloBlocoDeNotas.menu_select("Arquivo->Sair")


btnNotSave = window.child_window(title="Não Salvar", auto_id="CommandButton_7", control_type="Button").wrapper_object()
btnNotSave.click() # Clique sem usar o mouse, não funciona para todos os casos
