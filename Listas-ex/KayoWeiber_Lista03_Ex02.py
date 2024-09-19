#exercício-02.Registro de Porudutos em Estoque
nome = []
quantidade = []
preço = []
while True:
    try:
        print("Registro de Produtos em Estoque.")
        print("1. Adicionar produto\n2. Remover Produto\n3. Alterar produto\n4. Exibir os produtos\n5. Sair")
        menu = int(input("Digite o número desejado: "))  
        if menu == 1:
            #adicionar produto
            while True:
                nome_produto = input("Digite o nome do produto: ").title()
                if nome_produto:
                    break
                else:
                    print("Por favor, digite o nome do produto.")
            if nome_produto in nome:
                print("O nome do produto já existe no estoque.")
                index = nome.index(nome_produto)
                while True:
                    try:
                        acre = int(input("Você deseja acrescentar mais unidades a esse produto? Se \"sim\" digite 1 ou se \"não\" digite 2: "))
                        if acre == 1:
                            acrescentar_quantidade = int(input("Digite a quantidade de produtos para acrescentar: "))
                            quantidade[index] += acrescentar_quantidade
                            print("A quantidade de produto foi acrescentada com sucesso.")
                            break
                        elif acre == 2:
                            break
                        else:
                            print("Por favor, digite 1 ou 2.")
                    except ValueError:
                        print("O valor informado é inválido.")
            else:
                while True:
                    try:
                        quant = int(input("Digite a quantidade de produtos: "))
                        break
                    except ValueError:
                        print("Por favor, digite a quantidade de produtos.")
                while True:
                    try:
                        pre = float(input("Digite o valor unitário do produto: "))
                        nome.append(nome_produto)
                        quantidade.append(quant)
                        preço.append(pre)
                        print("Ação realizada com sucesso.")
                        break
                    except ValueError:
                        print("Por favor, digite o valor do produto.")
        elif menu == 2:
            # Remover produto
            while True:
                remover = input("Digite o nome do produto que deseja remover: ").title()
                if remover:
                    break
                else:
                    print("Por favor, digite o nome do produto.")
            
            if remover in nome:
                index = nome.index(remover)
                while True:
                    try:
                        certeza = int(input("Você tem certeza que deseja remover esse produto? Digite 1 para \"sim\" e 2 para \"não\": "))
                        if certeza == 1:
                            while True:
                                try:
                                    escolha = int(input("Você quer remover apenas uma quantidade do produto ou remover o registro do produto inteiro? Digite 1 para a primeira opção ou 2 para a segunda opção: "))
                                    if escolha == 1:
                                        remover_quantidade = int(input("Digite a quantidade de produtos para remover: "))
                                        quantidade[index] -= remover_quantidade
                                        print("Remoção realizada com sucesso.")
                                        break
                                    elif escolha == 2:
                                        nome.pop(index)
                                        quantidade.pop(index)
                                        preço.pop(index)
                                        print(f"{remover} foi removido do estoque.")
                                        break
                                    else:
                                        print("O valor digitado não é válido, tente novamente.")
                                except ValueError:
                                    print("O valor informado é inválido.")
                            break
                        elif certeza == 2:
                            print("Operação cancelada.")
                            break
                        else:
                            print("Por favor, digite 1 ou 2.")
                    except ValueError:
                        print("O valor informado é inválido.")
            else:
                print("O produto digitado não está no estoque.")
        elif menu == 3:
            #alterar produto
            while True:
                alterar = input("Digite o nome do produto que deseja alterar: ").title()
                if alterar:
                    break
                else:
                    print("Por favor, digite o nome do produto.")
            if alterar in nome:
                index = nome.index(alterar)
                while True:
                    try:
                        op = int(input("Você deseja alterar o nome do produto ou o preço do produto? (Digite 1 para nome e 2 para o preço): "))
                        if op == 1:
                            novonome = input("Digite o novo nome do produto: ").title()
                            nome[index] = novonome
                            print(f"O nome de {alterar} foi mudado para {novonome}")
                            break
                        elif op == 2:
                            novopreço = float(input("Digite o novo preço do produto: "))
                            preço[index] = novopreço
                            print(f"O preço de {alterar} foi mudado para {novopreço}")
                            break
                        else:
                            print("O valor digitado não é válido.")
                    except ValueError:
                        print("O valor informado é inválido.")
            else:
                print("O produto digitado não está no estoque.")
        elif menu == 4:
            #exibir produtos
            if nome:
                print("Produtos em estoque:")
                for n, q, p in zip(nome, quantidade, preço):
                    print(f"Nome: {n}, Quantidade: {q}, Preço: {p:.2f}")
            else:
                print("Não há produtos no estoque.")
        elif menu == 5:
            #sair do programa
            print("Programa encerrado.")
            break
        else:
            print("Por favor, digite um número válido.")
    except ValueError:
        print("Valor inválido, tente novamente.")