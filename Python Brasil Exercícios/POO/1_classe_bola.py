class Bola:
    def __init__(self, cor=None, circ=None, material=None):
        self.cor = cor
        self.circ = circ
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        return self.cor


if __name__ == '__main__':
    bola_1 = Bola('vermelha', 20, 'Plástico')
    print(bola_1.mostra_cor())
    bola_1.troca_cor('azul')
    print(bola_1.mostra_cor())

