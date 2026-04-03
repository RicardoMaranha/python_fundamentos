# construtor ou inicializador em python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # destrutor em python
    def __del__(self):
        print("Objeto destruído")  

    # método para exibir informações da pessoa
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
    
    # método para atualizar a idade da pessoa
    def atualizar_idade(self, nova_idade):
        self.idade = nova_idade


p1 = Pessoa("João", 30)
print(p1.nome)  # Output: João
print(p1.idade)  # Output: 30
del p1  # Isso irá chamar o destrutor e imprimir "Objeto destruído"
print("Fim do programa")