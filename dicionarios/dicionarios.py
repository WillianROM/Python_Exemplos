# Dicionário é uma lista com um "rótulo"
# É muito bom para armazenar informações que precisam de algum tipo de identificador

emails_gerentes = {
    "João de Barro": "joaozinho@birds.com",
    "Pica-Pau": "cabecavermelha@birds.com",
    "pato Donald": "donald@birds.com"
}

# Seu eu quiser descobrir qual o e-mail do "Pica-Pau"
email = emails_gerentes['Pica-Pau']
print(email)

# Seu eu quiser adicionar mais alguém
emails_gerentes["Zé Carioca"] = "zedorio@birds.com"
print(emails_gerentes)

# Se quiser descobrir todos os personagens que temos?
    # forma 1: fazer um for
for shopping in emails_gerentes:
    print(shopping)

    # forma 2: dicionario.keys()
print(emails_gerentes.keys())

# Se quiser todos os e-mails?
    # forma 1:
for shopping in emails_gerentes:
    email = emails_gerentes[shopping]
    print(email)

    # forma 2: dicionario.values()
print(emails_gerentes.values())

# Retirar um personagem
emails_gerentes.pop("pato Donald")
print(emails_gerentes)

# Verificar se um personagem existe
if "pato Donald" in emails_gerentes:
    print("Existe")
else:
    print("Não existe")
