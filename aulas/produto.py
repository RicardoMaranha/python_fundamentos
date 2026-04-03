# Leitura da entrada: preço e código de promoção
entrada = str(input("Digite o preço do produto e o código de promoção (ex: 10.99 S): ").strip())
preco_str, codigo_promocao = entrada.split()

# Conversão do preço para float
preco = float(preco_str)

# TODO: Se o produto estiver em promoção ("S"), aplique 10% de desconto ao preço.
# Caso contrário, mantenha o preço original.
# Dica: Use uma estrutura condicional para decidir qual valor atribuir à variável preco_final.
# preco_final = ...

if codigo_promocao.upper() == "S":
    preco_final = preco - (preco * 0.10)  # Aplica 10% de desconto
else:
    preco_final = preco  # Mantém o preço original

# Exibe o valor final com duas casas decimais
print(f"preço inicial: {preco:.2f} / preço final: {preco_final:.2f}")
