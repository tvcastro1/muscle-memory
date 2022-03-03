class Quadrado:
    def __init__(self):
        self.lado = None

    def mudar_valor_lado(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


if __name__ == '__main__':
    quadrado = Quadrado()
    quadrado.lado = 2
    print(quadrado.lado)
    print(quadrado.calcular_area())
    quadrado.mudar_valor_lado(4)
    print(quadrado.lado)
    print(quadrado.calcular_area())

