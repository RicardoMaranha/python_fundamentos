# herança em python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"
    
class Gato(Animal):
    def falar(self):
        return "Miau!"
    
cachorro = Cachorro("Rex")
gato = Gato("Mimi")
print(f"{cachorro.nome} diz: {cachorro.falar()}")  # Output: Rex diz: Au au!
print(f"{gato.nome} diz: {gato.falar()}")  # Output: Mimi diz: Miau!

# herança múltipla em python exemplo real
class Ave(Animal):
    def __init__(self, nome, voa):
        super().__init__(nome) # Chama o construtor da classe base (Animal) para inicializar o nome
        self.voa = voa

    def voar(self):
        return f"{self.nome} está voando!"

class Papagaio(Ave):
    def __init__(self, nome, voa, fala):
        super().__init__(nome, voa)
        self.fala = fala

    def falar(self):
        return f"{self.nome} diz: {self.fala}"

papagaio = Papagaio("Loro", True, "Olá, como vai?")
print(papagaio.falar())  # Output: Loro diz: Olá, como vai?
print(papagaio.voar())   # Output: Loro está voando!

# implementação de mixins em python
class VoarMixin:
    def voar(self):
        return f"{self.nome} está voando!"

class Papagaio(Ave, VoarMixin):
    def __init__(self, nome, voa, fala):
        super().__init__(nome, voa)
        self.fala = fala

    def falar(self):
        return f"{self.nome} diz: {self.fala}"

papagaio = Papagaio("Loro", True, "Olá, como vai?")
print(papagaio.falar())  # Output: Loro diz: Olá, como vai?
print(papagaio.voar())   # Output: Loro está voando!


class Foo: 
    def hello(self): print(self.__class__.__name__.lower()) 
    
class Bar(Foo): 
    def hello(self): 
        return super().hello() 

bar = Bar() 
bar.hello()
