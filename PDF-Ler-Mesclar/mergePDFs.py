import PyPDF2

# Abrindo arquivo em modo binário e leitura
arq1 = open('Tabela.pdf','rb') 
arq2 = open('Fax.pdf','rb')
arq3 = open('Texto.pdf','rb')

# Lendo os dados dos binários que são PDF
dados_do_arq1 = PyPDF2.PdfReader(arq1) # Recebe um binário do arquivo, não o caminho do arquivo
dados_do_arq2 = PyPDF2.PdfReader(arq2)
dados_do_arq3 = PyPDF2.PdfReader(arq3)

# declarando um objeto do tipo Merge
merge = PyPDF2.PdfMerger() # Setando a variável merge

# Colocar os dados dos arquivos na variável merge
merge.append(dados_do_arq1)
merge.append(dados_do_arq2)
merge.append(dados_do_arq3)

# Escrevendo o novo arquivo PDF
merge.write('ArquivoFundido.pdf')
