# Lê a linha de entrada e separa os produtos em uma lista
produtos = input().strip().split()

# TODO: Crie uma estrutura para contar quantas vezes cada produto aparece na lista

# Dica: Use um laço para percorrer a lista e atualizar a contagem de cada produto

# Inicialize variáveis para armazenar o produto mais frequente e sua contagem
maior_contagem = 0
mais_frequente = None
i = 0
while i < len(produtos):
    produto_atual = produtos[i]
    contagem = produtos.count(produto_atual)  # Conta quantas vezes o produto aparece na lista
    if contagem > maior_contagem:
        maior_contagem = contagem
        mais_frequente = produto_atual
    i += 1
    

# Percorra a lista original para garantir o critério de desempate (primeira ocorrência)
for produto in produtos:
    # TODO: Obtenha a contagem do produto atual e atualize mais_frequente se necessário
    contagem = produtos.count(produto)
    if contagem > maior_contagem or (contagem == maior_contagem and produtos.index(produto) < produtos.index(mais_frequente)):
        maior_contagem = contagem
        mais_frequente = produto

# Imprima o produto mais frequente
print(mais_frequente)