# Com base em seu conhecimento, defina um registro para cheque bancário

class ContaBancária:

    def __init__(self, nome, CPF, saldo):
        self.nome = nome
        self.CPF = CPF
        self.saldo =saldo

    def deposito(self):
        self.saldo += self
        return self.saldo


