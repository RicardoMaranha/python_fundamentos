# properties em phython
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo protegido
        self._idade = idade  # Atributo protegido

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._nome = valor
        else:
            print("Nome inválido. Deve ser uma string não vazia.")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self._idade = valor
        else:
            print("Idade inválida. Deve ser um número inteiro não negativo.")


    # Qual método utilizamos para criar atributos gerenciados em Python?

#Por padrão tudo é publico em Python, mas considerando as convenções da linguagem quais são os modificadores de acesso que podemos utilizar?