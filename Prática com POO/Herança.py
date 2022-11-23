class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N°{self.numero} Saldo: {self.saldo}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]}")
        print(f"\n    Saldo: {self.saldo}\n")


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abre_conta(self, conta):
        self.contas.append(conta)

    def lista_contas(self):
        for c in self.contas:
            c.resumo()


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])


# joao = Cliente("João da Silva", "777-1234")
# maria = Cliente("Maria da Silva", "555-4321")
# conta1 = Conta([joao], 1, 1000)
# print(vars(conta1))
# conta2 = ContaEspecial([maria, joao], 2, 500, 1000)
# print(vars(conta2))
# conta1.saque(50)
# conta2.deposito(300)
# conta1.saque(190)
# conta2.deposito(95.15)
# conta2.saque(1500)
# conta1.extrato()
# conta2.extrato()


class Cachorro:
    def __init__(self, nome, raca, peso, patas=4):
        self.nome = nome
        self.raca = raca
        self.peso = peso
        self.patas = patas
        self.racao_dia = []

    def vocaliza(self):
        if self.peso <= 10:
            print(f'{self.nome} diz :au au au')
        else:
            print(f'{self.nome} diz: WOOF WOOF')

    def quantidade_racao(self):
        if self.peso <= 5:
            self.racao_dia.append(95)
        elif 5 < self.peso <= 10:
            self.racao_dia.append(150)
        else:
            self.racao_dia.append(200)


class Gato(Cachorro):
    def __init__(self, nome, raca, peso):
        super().__init__(nome, raca, peso)

    def vocaliza(self):
        if self.peso <= 10:
            print(f'{self.nome} diz :miau miau')
        else:
            print(f'{self.nome} diz: MIAU MIAU')


frida = Cachorro('Frida', 'SRD', 17)
frida.vocaliza()
frida.quantidade_racao()

print(frida.racao_dia)

morgana = Gato('Morgana', 'SRD', 5)
morgana.vocaliza()
morgana.quantidade_racao()
print(morgana.racao_dia)
