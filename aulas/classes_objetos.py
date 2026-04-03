# classe em python
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        return "Au au!"
    
    def aniversario(self):
        self.idade += 1
        return f"{self.nome} agora tem {self.idade} anos."
    
# Criando um objeto da classe Cachorro
meu_cachorro = Cachorro("Rex", 5)  
print(meu_cachorro.nome)  # Saída: Rex
print(meu_cachorro.idade)  # Saída: 5
print(meu_cachorro.latir())  # Saída: Au au!
print(meu_cachorro.aniversario())  # Saída: Rex agora tem 6 anos.
