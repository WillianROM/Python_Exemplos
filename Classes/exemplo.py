# Vamos criar uma classe para Cleintes da Netflix
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.list_planos = ["Basic", "Premium"]
        if plano in self.list_planos:
            self.plano = plano
        else:
            raise Exception("Plano Inválido")

    def nudar_plano(self, novo_plano):
        if novo_plano in self.list_planos:
            self.plano = novo_plano
        else:
            raise Exception("Plano Inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver Filme {filme}")
        elif self.plano == "Premium":
            print(f"Ver Filme {filme}")
        elif self.plano == "Basic" and plano_filme == "Premium":
             print("Faça upgrade para Premium para ver esse filme")
        else:
            raise Exception("Plano Inválido")


cliente = Cliente("João", "joao@bird.com", "Basic")
print(cliente.nome)
cliente.ver_filme("Avatar: O Caminho das Águas", "Premium")

# no botão de upgrade
cliente.nudar_plano("Premium")
print(cliente.plano)
cliente.ver_filme("Avatar: O Caminho das Águas", "Premium")


