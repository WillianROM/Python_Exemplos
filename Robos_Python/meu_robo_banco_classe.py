# https://pywinauto.readthedocs.io/en/latest/
# window.print_control_identifiers() #Usar para identificar os elementos da tela 
class aplicativoBanco:
    from pywinauto.keyboard import send_keys

    def __init__(self):
        self.caminhoDoAplicativo = r'C:\banco\Banco.exe' # O executável está disponível no site https://desafiosrpa.com.br/bank-robot.html
        

    def iniciar_aplicativo(self):
        from pywinauto.application import Application
        app = Application(backend="uia").start(self.caminhoDoAplicativo)
        app = Application(backend="uia").connect(title="Alex Diogo - Bank", timeout=20)
        self.window = app.AlexDiegoBank

    def clicar_botao_iniciar(self):
        btnIniciar = self.window.child_window(title="Iniciar", auto_id="button_Iniciar",             control_type="Button").wrapper_object()
        btnIniciar.click()

    def selecionar_debito_ou_credito(self, tipo):
        self.tipo = tipo
        if tipo == "Débito":
            rdBtnTipo = self.window.child_window(title="Débito", auto_id="radioButton_Debito", control_type="RadioButton").wrapper_object()
        elif tipo == "Crédito":
            rdBtnTipo = self.window.child_window(title="Crédito", auto_id="radioButton_Credito", control_type="RadioButton").wrapper_object()
        rdBtnTipo.click()

    def informar_a_descricao(self, descricao):
        
        editDescricao = self.window.child_window(auto_id="textBox_Descricao", control_type="Edit").wrapper_object()
        editDescricao.set_edit_text(u'') # clean-up
        editDescricao.type_keys(descricao, with_spaces = True)
        
    def informar_o_valor(self, valor):
       
        editValor = self.window.child_window(title="Descrição:", auto_id="textBox_Valor", control_type="Edit").wrapper_object()
        editValor.set_edit_text(u'') # clean-up
        editValor.type_keys(valor)

    def informar_a_data(self, data):
        
        editData = self.window.child_window(auto_id="textBox_Data", control_type="Edit").wrapper_object()
        editData.set_edit_text(u'') # clean-up
        editData.type_keys(data)

    def clicar_no_botao_gravar(self):
        btnGravar = self.window.child_window(title="Gravar", auto_id="button_Gravar", control_type="Button").wrapper_object()
        btnGravar.click()

    def pegar_o_valor_do_saldo_do_banco(self):
        lblSaldo = self.window.child_window(auto_id="label_SALDO", control_type="Text").wrapper_object()
        saldo = lblSaldo.window_text()
        print('O saldo é ' + saldo)

    def fechar_aplicativo(self):
        close = self.window.child_window(title="Fechar", control_type="Button").wrapper_object()
        close.click_input()




