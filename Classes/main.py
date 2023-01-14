# https://www.youtube.com/watch?v=gomDSZaay3E
class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o Canal")
        elif botao == "-":
            print("Diminuir o Canal")



Controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
print(Controle_remoto.cor)
Controle_remoto.passar_canal("+")

Controle_remoto2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")
print(Controle_remoto2.cor)
Controle_remoto2.passar_canal("-")
