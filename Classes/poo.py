# https://www.youtube.com/watch?v=97A_Cyyh-eU

class Vendador():
    def __init__(self, nome): # Construtor
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
             print(f"{self.nome}, bateu a meta")
        else:
            print(f"{self.nome}, não bateu a meta")


#########################################################################################################

vendedorJoao =  Vendador("João")  
vendedorJoao.vendeu(1000)
vendedorJoao.bateu_meta(500)


vendadorMaria = Vendador("Maria")
vendadorMaria.vendeu(450)
vendadorMaria.bateu_meta(500)
