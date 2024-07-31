
lista_de_compras = []
totalProdutos = 0.0

def AdicionarProduto():
    
    global totalProdutos
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor_unitario = float(input("Digite o valor unitário do produto: "))

    valor_total = quantidade * valor_unitario
    produto = {
        "produto": nome,
        "valor": valor_unitario,
        "quantidade": quantidade,
        "total": valor_total
    }

    lista_de_compras.append(produto)
    totalProdutos += valor_total

    print(f"Produto '{nome}' adicionado com sucesso!")

def VerListaDeProdutos():
    
    global totalProdutos
    if lista_de_compras:
        print("\nLista de Produtos:")
        for i, produto in enumerate(lista_de_compras):
            print(f"{i + 1}. Nome: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor Unitário: {produto['valor']:.2f}, Valor Total: {produto['total']:.2f}")
        print(f"\nValor Total de Todos os Produtos: {totalProdutos:.2f}")
    else:
        print("A lista de produtos está vazia.")

def AtualizarProduto():
    
    global totalProdutos

    if not lista_de_compras:
        print("A lista de produtos está vazia. Não há produtos para atualizar.")
        return

    VerListaDeProdutos()
    
    try:
        escolha = int(input("Escolha o número do produto que deseja atualizar: ")) - 1
        
        if 0 <= escolha < len(lista_de_compras):
            produto = lista_de_compras[escolha]
            
            while True:
                try:
                    nova_quantidade = int(input(f"Digite a nova quantidade para '{produto['produto']}': "))
                    break
                except ValueError:
                    print("Erro: A quantidade deve ser um número inteiro. Tente novamente.")
            
            while True:
                try:
                    novo_valor_unitario = float(input(f"Digite o novo valor unitário para '{produto['produto']}': "))
                    break
                except ValueError:
                    print("Erro: O valor unitário deve ser um número. Tente novamente.")
            
            valor_total_antigo = produto["total"]

            produto["quantidade"] = nova_quantidade
            produto["valor"] = novo_valor_unitario
            produto["total"] = nova_quantidade * novo_valor_unitario

            totalProdutos += produto["total"] - valor_total_antigo
            print(f"Produto '{produto['produto']}' atualizado com sucesso!")
        else:
            print("Número de produto inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

def RemoverProduto():
    
    global totalProdutos
    if not lista_de_compras:
        print("A lista de produtos está vazia. Não há produtos para remover.")
        return

    VerListaDeProdutos()
    
    try:
        escolha = int(input("Escolha o número do produto que deseja remover: ")) - 1
        
        if 0 <= escolha < len(lista_de_compras):
            produto = lista_de_compras.pop(escolha)
            totalProdutos -= produto["total"]
            print(f"Produto '{produto['produto']}' removido com sucesso!")
        else:
            print("Número de produto inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

def Menu():
    
    while True:
        print("\nMenu de Gerenciamento de Compras")
        print("1. Adicionar produto")
        print("2. Ver lista de produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Encerrar programa")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            AdicionarProduto()
        elif escolha == '2':
            VerListaDeProdutos()
        elif escolha == '3':
            AtualizarProduto()
        elif escolha == '4':
            RemoverProduto()
        elif escolha == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    Menu()