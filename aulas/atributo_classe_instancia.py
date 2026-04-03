# atributo classe e instancia
class Pessoa:
    olhos = 2  # atributo de classe

    def __init__(self, *filhos, nome=None, idade=35):
        self.filhos = filhos  # atributo de instância
        self.nome = nome  # atributo de instância
        self.idade = idade  # atributo de instância

if __name__ == '__main__':
    p1 = Pessoa(nome='Maria')
    p2 = Pessoa(p1, nome='João')
    print(Pessoa.olhos)  # acessando atributo de classe
    print(p1.olhos)  # acessando atributo de classe através da instância
    print(p2.olhos)  # acessando atributo de classe através da instância
    print(p1.nome)  # acessando atributo de instância
    print(p2.nome)  # acessando atributo de instância
    print(p1.filhos)  # acessando atributo de instância
    print(p2.filhos)  # acessando atributo de instânciaz