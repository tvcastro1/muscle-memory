class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, idade):
        self.idade += idade
        for n in range(self.idade):
            self.altura += 0.5
            if n == 20:
                break
        return None

    def engordar(self):
        pass

    def emagrecer(self):
        pass

    def crescer(self):
        pass

    def imprimir_pessoa(self):
        return f'A idade é {self.idade} anos e a altura é {self.altura} centímetros'


if __name__ == '__main__':
    p1 = Pessoa('Thiago', 2, 12, 80)
    p1.envelhecer(12)
    print(p1.imprimir_pessoa())