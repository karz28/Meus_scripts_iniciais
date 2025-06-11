print('Quantos produtos você quer cadastrar?')
num_produtos = int(input('Número de produtos: ')) # Entrada do usuário para o número de produtos
produtos = [] # Lista para armazenar os produtos

# Inicialização de contadores e acumuladores
produto_premium = 0 
produto_comum = 0
total_valor_produtos = 0.0
# Loop para cadastro de produtos
for i in range(num_produtos):
    print(f'\nProduto {i + 1}:')
    nome = input('Nome do produto: ')
    preco = float(input('Preço unitário do produto: '))
    quantidade = int(input('Quantidade do produto: '))
     
    # Determinação do tipo de produto e contagem de produtos Premium e Comuns

    # Se o preço for maior que 100, é Premium, caso contrário, é Comum
    tipo = 'Premium' if preco > 100 else 'Comum'
    
    if tipo == 'Premium':
        produto_premium += 1
    else:
        produto_comum += 1

    valor_total = preco * quantidade
    total_valor_produtos += valor_total

    # Criação do dicionário para o produto
    produto = {
        'nome': nome,
        'preço': preco,
        'quantidade': quantidade,
        'tipo': tipo,
        'valor_total': valor_total
    }

    produtos.append(produto) # Adiciona o produto à lista

# RESUMO
print('\n📦 RESUMO GERAL DOS PRODUTOS')
print(f'Total de produtos cadastrados: {num_produtos}')
print(f'Produtos Premium: {produto_premium}')
print(f'Produtos Comuns: {produto_comum}')
print(f'Valor total acumulado: R$ {total_valor_produtos:.2f}')

print('\n📋 LISTAGEM DE PRODUTOS:')
for i, produto in enumerate(produtos, start=1):
    print(f"\nProduto {i}:")
    print(f"  Nome       : {produto['nome']}")
    print(f"  Preço      : R$ {produto['preço']:.2f}")
    print(f"  Quantidade : {produto['quantidade']}")
    print(f"  Tipo       : {produto['tipo']}")
    print(f"  Total      : R$ {produto['valor_total']:.2f}")