# metodos de classe Python
class Pessoa:
    cidade = "São Paulo"  # atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_pessoa(cls, nome, idade):
        return cls(nome, idade)
    
    @staticmethod
    def validar_idade(idade):
        if idade < 0:
            raise ValueError("Idade não pode ser negativa")
        return True
    
    #exemplo de uso métdo estático vida real
    @staticmethod
    def calcular_idade_apos_10_anos(idade):
        return idade + 10
    
# metodo para mostrar objetos
def mostrar_pessoa(*objs):
    for objeto in objs:
        print(f"Nome: {objeto.nome}, Idade: {objeto.idade}, Cidade: {objeto.cidade}")

# Criando uma pessoa usando o método de classe
pessoa1 = Pessoa.criar_pessoa("Alice", 30)
pessoa2 = Pessoa.criar_pessoa("Bob", 25)

mostrar_pessoa(pessoa1, pessoa2)
