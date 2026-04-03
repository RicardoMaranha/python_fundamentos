# encapsulamento em python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria("Maria", 1000)
print(conta.titular)  # Output: Maria
conta.depositar(500)  # Output: Depósito de R$500 realizado com sucesso.
conta.sacar(200)  # Output: Saque de R$200 realizado com sucesso.
print(conta.consultar_saldo())  # Output: 1300
# Tentando acessar o saldo diretamente (isso não é recomendado e pode causar um erro)
# print(conta.__saldo)  # Isso irá gerar um AttributeError, pois __saldo
# é um atributo privado e não pode ser acessado diretamente fora da classe.
