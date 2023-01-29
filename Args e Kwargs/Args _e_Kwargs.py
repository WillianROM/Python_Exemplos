# https://www.youtube.com/watch?v=RcqHJ_l8GVA&ab_channel=HashtagPrograma%C3%A7%C3%A3o

# Funções no Python
# 1. Argumentos de Posição e Keyword
# 2. args e kwargs

def calcular_imposto(valor):
    ir = valor * 0.275
    iss = valor * 0.05
    csll = valor * 0.0375
    pis = valor * 0.03
    return ir + iss + csll + pis

print(calcular_imposto(valor=1000))


def calcular_imposto_args(valor, *args): # args tem um * - faz tuplas
    total_imposto = 0
    for item in args:
        total_imposto += valor * item
    return total_imposto

print(calcular_imposto_args(1000, 0.275, 0.05, 0.0375, 0.03))


def calcular_imposto_kwargs(valor, **kwargs): # kwargs tem dois * - kw = key words, faz dicionários
    total_imposto = 0
    if 'perc_ir' in kwargs:
        total_imposto += valor * kwargs['perc_ir']
    if 'perc_iss' in kwargs:
        total_imposto += valor * kwargs['perc_iss']
    if 'perc_csll' in kwargs:
        total_imposto += valor * kwargs['perc_csll']
    if 'perc_pis' in kwargs:
        total_imposto += valor * kwargs['perc_pis']
    return total_imposto

print(calcular_imposto_kwargs(1000, perc_ir = 0.275, perc_iss = 0.05, perc_csll = 0.0375, perc_pis = 0.03))
