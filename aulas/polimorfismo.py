# Polimorfismo em Python
class Animal:
    def falar(self):
        pass  # Método genérico, será implementado pelas subclasses

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Pássaro(Animal):
    def falar(self):
        return "Piu piu!"

# Criando uma lista de animais
animais = [Cachorro(), Gato(), Pássaro()]   
# Usando polimorfismo para chamar o método falar de cada animal
for animal in animais:
    print(animal.falar())
# O que é polimorfismo em Python e como ele é implementado?
# Polimorfismo é um conceito da programação orientada a objetos que permite que objetos de diferentes classes sejam tratados como objetos de uma classe comum. Em Python, o polimorfismo é implementado através da herança e da sobrescrita de métodos. As subclasses podem fornecer suas próprias implementações do método falar(), e quando chamamos esse método em uma lista de objetos, o Python determina qual implementação usar com base no tipo do objeto em tempo de execução.

