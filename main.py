produtos = []
carrinho = []


def cadastrarProduto():
    nomeProduto = input('Nome do produto: ')
    precoProduto = float(input('Preço: '))
    quantidadeProduto = int(input('Quantidade: '))
    produto = {'Nome': nomeProduto, 'Preço': precoProduto, 'Quantidade': quantidadeProduto}
    produtos.append(produto)
    print('Produto cadastrado com Sucesso!')
    
def listarProdutos():
    print('Lista de Produtos')
    numProdutos = 0
    for produto in produtos:
        numProdutos += 1
        print('ID do Produto: ', numProdutos)
        print(f"Nome: {produto['Nome']}, Preço: R${produto['Preço']:.2f}, Quantidade: {produto['Quantidade']}")
        print()
        
        
def adicionarCarrinho():
    listarProdutos()
    addProdutoCarrinho = int(input('Digite o ID do produto que deseja adicionar ao carrinho: '))
    if addProdutoCarrinho > 0 and addProdutoCarrinho <= len(produtos):
        produto_selecionado = produtos[addProdutoCarrinho - 1]
        addQuantidade = int(input('Digite a quantidade que deseja: '))
        if addQuantidade <= produto_selecionado['Quantidade']:
            produto_no_carrinho = {'Nome': produto_selecionado['Nome'], 'Preço': produto_selecionado['Preço'], 'Quantidade': addQuantidade}
            carrinho.append(produto_no_carrinho)
            print('Produto adicionado ao carrinho.')
            # Atualizar a quantidade do produto na lista de produtos
            produtos[addProdutoCarrinho - 1]['Quantidade'] -= addQuantidade
        else:
            print('Quantidade indisponível do produto.')
    else:
        print('ID de produto inválido.')
    

while True:
    print('|-----------Menu---------|')
    print('|1 - Cadastrar produto(s)|')
    print('|2 - Listar produto(s)   |')
    print('|3 - Comprar produto(s)  |')
    print('|4 - Carrinho            |')
    print('|5 - Finalizar compra    |')
    print('|0 - Sair do programa    |')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        print('Você selecionou a opção 1 - Cadastrar produto(s)')
        cadastrarProduto()
    elif opcao == 2:
        print('Você selecionou a opção 2 - Listar produto(s)')
        listarProdutos()
    elif opcao == 3:
        print('Você selecionou a opção 3 - Comprar produto(s)')
        adicionarCarrinho()
    elif opcao == 4:
        print('Você selecionou a opção 4 - Carrinho')
        # Aqui você pode colocar o código para visualizar o carrinho
    elif opcao == 5:
        print('Você selecionou a opção 5 - Finalizar compra')
        # Aqui você pode colocar o código para finalizar a compra
    elif opcao == 0:
        print('Saindo do programa...')
        break  # Sai do loop
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
