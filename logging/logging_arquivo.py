# https://www.youtube.com/watch?v=Z7ojOhYdolk
# https://www.hashtagtreinamentos.com/logging-em-python
# https://docs.python.org/3/library/logging.html
import logging
logging.basicConfig(level=logging.INFO, filename='programa.log', format='%(asctime)s - %(levelname)s - %(message)s') # https://docs.python.org/3/library/logging.html#logrecord-attributes

def resultado_operacional(faturamento, custo):
    return faturamento - custo

def lucro_liquido(faturamento, custo, aliquota_imposto):
    if aliquota_imposto == 0:
        logging.warning("Alíquota de imposto é 0, tá certo isso?")
    return (faturamento - custo) * (1 - aliquota_imposto)

def lucro_por_acoes(faturamento, custo, aliquota_imposto, acoes):
    if acoes == 0:
        logging.error("Não pode as ações serem igual a 0")
    return   lucro_liquido(faturamento, custo, aliquota_imposto)/acoes

faturamento = 1000
custo = 400
aliquota_imposto = 0.3
acoes = 100

resultado = resultado_operacional(faturamento, custo)
logging.info(f'Resultado: {resultado}')

lucro = lucro_liquido(faturamento, custo, aliquota_imposto)
logging.info(f'Lucro: {lucro}')

lucro_acao = lucro_por_acoes(faturamento, custo, aliquota_imposto, acoes)
logging.info(f'Lucro Ação: {lucro_acao}')

##### Resumo:

# logging.debug
# DEBUG - Informação detalhada, tipicamente de interesse apenas quenado diagnosticando problemas.

# logging.info
# INFO - Confirmação de que as coisas estão funcionando como esperado.

# logging,warning
# WARNING  - Uma indicação que algo inesperado aconteceu, ou um indicativo que algum problema em um futuro próximo (ex.: ‘pouco espaço em disco’). O software está ainda funcionando como esperado.

# logging.error
# ERROR - Por conta de um problema mais grave, o software não conseguiu executrar alguma função.

# logging.çcritical
# CRITICAL - Um erro grave, indicando que o programa pode não conseguir continuar rodando.