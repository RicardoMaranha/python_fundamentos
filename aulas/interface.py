# interface em Python
from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def metodo_abstrato(self):
        pass

class Implementacao(Interface):
    def metodo_abstrato(self):
        print("Implementação do método abstrato")
# Criando uma instância da classe de implementação
objeto = Implementacao()
objeto.metodo_abstrato()  # Output: Implementação do método abstrato

# exemplo real utilizado por profissionais em Python
class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

class PagamentoCartao(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor} com cartão de crédito")

class PagamentoBoleto(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor} com boleto bancário")
# Criando instâncias das classes de pagamento
pagamento_cartao = PagamentoCartao()
pagamento_boleto = PagamentoBoleto()
pagamento_cartao.processar_pagamento(100)  # Output: Processando pagamento de R$100 com cartão de crédito
pagamento_boleto.processar_pagamento(200)  # Output: Processando pagamento de R$200 com boleto bancário
