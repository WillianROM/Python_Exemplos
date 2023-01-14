# https://pywinauto.readthedocs.io/en/latest/

import pywinauto
from pywinauto.application import Application

app = Application(backend="uia").start(r"C:\banco\Banco.exe")
app = Application(backend="uia").connect(title="Alex Diogo - Bank", timeout=20)

window = app.AlexDiegoBank
# window.print_control_identifiers()

btnIniciar = window.child_window(title="Iniciar", auto_id="button_Iniciar", control_type="Button").wrapper_object()
btnIniciar.click()

rdBtnDébito = window.child_window(title="Débito", auto_id="radioButton_Debito", control_type="RadioButton").wrapper_object()
rdBtnDébito.click()

editDescricao = window.child_window(auto_id="textBox_Descricao", control_type="Edit").wrapper_object()
editDescricao.type_keys("Isso é um teste", with_spaces = True)

editValor = window.child_window(title="Descrição:", auto_id="textBox_Valor", control_type="Edit").wrapper_object()
editValor.type_keys("1000,15")

editData = window.child_window(auto_id="textBox_Data", control_type="Edit").wrapper_object()
editData.type_keys("01/04/2022")

btnGravar = window.child_window(title="Gravar", auto_id="button_Gravar", control_type="Button").wrapper_object()
btnGravar.click()

lblSaldo = window.child_window(auto_id="label_SALDO", control_type="Text").wrapper_object()
saldo = lblSaldo.window_text()

print('O saldo é ' + saldo)


close = window.child_window(title="Fechar", control_type="Button").wrapper_object()
close.click_input()
