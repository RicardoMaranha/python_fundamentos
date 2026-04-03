# Primeiro programa em programação orientada a objetos (POO) em Python
# Criando a classe Bicicleta
class Bicicleta:
    def __init__(self, marca, modelo, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        return "Buzina: Biiiiii!"

    def descricao(self):
        return f"{self.ano} {self.marca} {self.modelo}"
    

# Criando um objeto da classe Bicicleta
minha_bicicleta = Bicicleta("Caloi", "Elite", 2020, 1500.00)
# Acessando os atributos do objeto
print(minha_bicicleta.marca)  # Saída: Caloi
print(minha_bicicleta.modelo)  # Saída: Elite
print(minha_bicicleta.ano)     # Saída: 2020
print(minha_bicicleta.valor)   # Saída: 1500.00
# Chamando os métodos do objeto
print(minha_bicicleta.buzinar())  # Saída: Buzina: Biiiiii!
print(minha_bicicleta.descricao())  # Saída: 2020 Caloi Elite   
