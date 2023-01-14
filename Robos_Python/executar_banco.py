import meu_robo_site_HTML_Table
import meu_robo_banco_classe

tabela = meu_robo_site_HTML_Table.pegar_tabela_do_site()
print(tabela)
#print(tabela.iloc[1,1])


banco = meu_robo_banco_classe.aplicativoBanco()
banco.iniciar_aplicativo()
banco.clicar_botao_iniciar()

for linha in range(len(tabela)):

    banco.selecionar_debito_ou_credito(tabela.iloc[linha,2])
    banco.informar_a_descricao(tabela.iloc[linha,1])
    banco.informar_o_valor(tabela.iloc[linha,3])
    banco.informar_a_data(tabela.iloc[linha,4])
    banco.clicar_no_botao_gravar()

banco.pegar_o_valor_do_saldo_do_banco()
banco.fechar_aplicativo()


