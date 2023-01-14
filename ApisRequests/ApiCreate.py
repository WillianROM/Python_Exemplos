# https://www.youtube.com/watch?v=WWVEymSt1iI
# Api criado no site https://replit.com/
# Vai ser necessário a biblioteca flask que permite criar sites e APIs - pip install flask

import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# construir as funcionalidades
@app.route('/')
def homepage():
  return 'A API está no ar'

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('advertising.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total vendas': total_vendas}
  return jsonify(resposta)
  
# rodar a API
app.run(host='0.0.0.0')
