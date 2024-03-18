produtos = []
carrinho = []


def cadastrarProduto():
    nomeProduto = input('Nome do produto:')
    precoProduto = float(input('Preço:'))
    quantidadeProduto = int(input('Quantidade:'))
    produto = {'Nome': nomeProduto, 'Preço': precoProduto, 'Quantidade': quantidadeProduto}
    for produto in produtos:
        if produto['Nome'] == nomeProduto and produto['Preço'] == precoProduto:
            produto['Quantidade'] += quantidadeProduto
            print('Quantidade do produto atualizada com sucesso!')
            break
    else:
        produtos.append(produto)
        print('Novo produto cadastrado com sucesso!')
    
def listarProdutos():
    if not produtos:
        print('\nNenhum produto disponivel.\n')
    print('Lista de Produtos')
    numProdutos = 0
    for produto in produtos:
        numProdutos += 1
        print('ID do Produto:', numProdutos)
        print(f"Nome: {produto['Nome']}, Preço: R${produto['Preço']:.2f}, Quantidade: {produto['Quantidade']}")
        print()
        
        
def adicionarCarrinho():
    listarProdutos()
    addProdutoCarrinho = int(input('Digite o ID do produto que deseja adicionar ao carrinho:'))
    if addProdutoCarrinho > 0 and addProdutoCarrinho <= len(produtos):
        produto_selecionado = produtos[addProdutoCarrinho - 1]
        addQuantidade = int(input('Digite a quantidade que deseja:'))
        if addQuantidade <= produto_selecionado['Quantidade']:
            produto_no_carrinho = {'Nome': produto_selecionado['Nome'], 'Preço': produto_selecionado['Preço'], 'Quantidade': addQuantidade}
            carrinho.append(produto_no_carrinho)
            print('Produto adicionado ao carrinho.\n')
            # Atualizar a quantidade do produto na lista de produtos
            produtos[addProdutoCarrinho - 1]['Quantidade'] -= addQuantidade
        else:
            print('Quantidade indisponível do produto.\n')
    else:
        print('ID de produto inválido.\n')
    
def produtosCarrinho():
    print('\nProdutos no carrinho\n')
    for produto in carrinho:
        print(f"Nome: {produto['Nome']}, Preço: R${produto['Preço']:.2f}, Quantidade: {produto['Quantidade']}\n")
        
def finalizarCompra():
    if not carrinho:
        print('Carrinho vazio. Não é possível finalizar a compra.\n')
        return
    print('\nProdutos no carrinho\n')
    for produto in carrinho:
        print(f"Nome: {produto['Nome']}, Preço: R${produto['Preço']:.2f}, Quantidade: {produto['Quantidade']}\n")
        total = sum(produto['Preço'] * produto['Quantidade'] for produto in carrinho)
        print(f'Total a pagar: R${total:.2f}')
    finalizar = input('\nDeseja finalizar a compra? (S/N)\n')
    if finalizar == 'S' or 's':
        print(f'\nTotal da compra: R${total:.2f}')
        carrinho.clear()
        print('Compra finalizada com sucesso!\n')
    elif finalizar == 'N' or 'n':
        print('Voltando ao menu...\n')
    else:
        print('Opção inválida.\n')


while True:
    print('|-----------Menu---------|')
    print('|1 - Cadastrar produto(s)|')
    print('|2 - Listar produto(s)   |')
    print('|3 - Comprar produto(s)  |')
    print('|4 - Carrinho            |')
    print('|5 - Finalizar compra    |')
    print('|0 - Sair do programa    |')

    opcao = int(input('\nDigite a opção desejada:'))

    if opcao == 1:
        print('\nCadastrar produto(s)\n')
        cadastrarProduto()
    elif opcao == 2:
        print('\nListar produto(s)\n')
        listarProdutos()
    elif opcao == 3:
        print('\nComprar produto(s)\n')
        adicionarCarrinho()
    elif opcao == 4:
        print('\nCarrinho\n')
        produtosCarrinho()
    elif opcao == 5:
        print('\nFinalizar compra\n')
        finalizarCompra()
    elif opcao == 0:
        print('Saindo do programa...')
        break  # Sai do loop
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
