# https://www.youtube.com/watch?v=l7pL_Y3fw-o

# Documentação: https://developers.google.com/sheets/api/quickstart/python

# Passo 1: Entre no site do Google Developer Console e crie um novo projeto -> Selecione o projeto criado

# Passo 2: Com o projeto criado no Google Developer Console, ative as APIs do Google Drive e do Google Sheets

# Passo 3: Vá no menu hambuguer -> APIs e serviços -> APIs e serviços ativados -> Tela de permissão OAuth -> Interno (se for usuário do google space - empresa) ou externo (se não for usuário do google space) -> Clique no botão Criar -> Dê um nome ao app e informe o e-mail -> Clique em Salvar e Continuar -> Se quiser colocar alguma limitação de acesso ao aplicativo, como somente leitura, vá em Adicionar e Remover Escopos, do contrário pode ir em frente -> Clique em Salvar e Continuar -> Adicione os usuário que terão acesso ao aplicativo -> Clique em Salvar e Continuar

# Passo 4: Vá em Credenciais -> Clique em + CRIAR CREDENCIAIS -> ID do cliente OAuth -> Selecione o tipo de aplicativo que está construindo  (nesse caso é App para computador) -> Dê um nome -> Clique em Criar -> Fazer download das credenciais no formato Json

# Passo 5: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Passo 6: Copie o código da documentação do google: https://developers.google.com/sheets/api/quickstart/python e cole no arquivo quickstart.py

