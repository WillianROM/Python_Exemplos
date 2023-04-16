# https://www.youtube.com/watch?v=MRmqMRLleK4&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=6&ab_channel=RonanVico
#pip install pypdf2
import PyPDF2
#import re  # replace, usado para substituir

# Abrindo arquivos em modo leitura e lendo o binário
pdf_file_tabela = open('Tabela.pdf','rb') # rb = read binary, ler o arquivo como binário
pdf_file_fax = open('Fax.pdf','rb')
pdf_file_texto = open('Texto.pdf','rb')

# Após pegar o binário, pegamos os dados de PDF desse Binário
dados_do_pdf_tabela = PyPDF2.PdfReader(pdf_file_tabela) # Recebe um binário do arquivo, não o caminho do arquivo
dados_do_pdf_fax = PyPDF2.PdfReader(pdf_file_fax)
dados_do_pdf_texto = PyPDF2.PdfReader(pdf_file_texto)

# Mostrar a quantidade de páginas que tem no arquivo
print('Números de páginas da Tabela: ' + str(len(dados_do_pdf_tabela.pages)))
print('Números de páginas do Fax: ' + str(len(dados_do_pdf_fax.pages)))
print('Números de páginas do Texto: ' + str(len(dados_do_pdf_texto.pages)))

# Setando a variável pagina1_tabela com o objeto pagina1_tabela
pagina1_tabela = dados_do_pdf_tabela.pages[0]
pagina1_fax = dados_do_pdf_fax.pages[0]
pagina1_texto = dados_do_pdf_texto.pages[0]

# Extrair texto da primeira página
texto_da_pagina1_tabela = pagina1_tabela.extract_text()
texto_da_pagina1_fax = pagina1_fax.extract_text()
texto_da_pagina1_texto = pagina1_texto.extract_text()

#texto_da_pagina1_tabela = re.sub('\n','',texto_da_pagina1_tabela)

print("Tabela: \n" + texto_da_pagina1_tabela)
print("Fax: \n" + texto_da_pagina1_fax)
print("Texto: \n" + texto_da_pagina1_texto)
