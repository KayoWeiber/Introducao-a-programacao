#exercício-08.Gerenciamento de Inventário de Loja
inventario = []
while True:
    try:
        print("\nGerenciamento de Inventário de Loja")
        print("1. Adicionar item\n2. Remover item\n3. Alterar item\n4. Exibir todos os itens\n5. Calcular valor total do inventário\n6. Sair")
        menu=int(input("Digite o número desejado: "))
        if menu==1:
            nome_item=input("Digite o nome do item: ")
            try:
                quantidade_item=int(input("Digite a quantidade do item: "))
                preco_item=float(input("Digite o preço do item: "))
                item={"nome": nome_item, "quantidade": quantidade_item, "preco": preco_item}
                inventario.append(item)
                print("Item adicionado com sucesso.")
            except ValueError:
                print("Por favor, digite valores válidos para quantidade e preço.")
        elif menu==2:
            if inventario:
                for i, item in enumerate(inventario):
                    print(f"{i + 1}. Nome: {item['nome']}, Quantidade: {item['quantidade']}, Preço: {item['preco']}")
                try:
                    remover=int(input("Digite o número do item que deseja remover uma unidade: "))
                    if 1<=remover<=len(inventario):
                        index=remover-1
                        if inventario[index]['quantidade']>1:
                            quant_unidades=int(input("Digite quantas unidades deseja remover do item:"))
                            inventario[index]['quantidade']-=quant_unidades
                            print(f"{quant_unidades} unidades do item foi removida com sucesso.")
                        else:
                            inventario.pop(index)
                            print("Item removido do inventário.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há itens para remover.")
        elif menu==3:
            if inventario:
                for i, item in enumerate(inventario):
                    print(f"{i + 1}. Nome: {item['nome']}, Quantidade: {item['quantidade']}, Preço: {item['preco']}")
                try:
                    alterar=int(input("Digite o número do item que deseja alterar: "))
                    if 1<=alterar<=len(inventario):
                        index=alterar-1
                        novo_nome=input("Digite o novo nome: ")
                        try:
                            novo_preco=float(input("Digite o novo preço: "))
                            inventario[index]["nome"]=novo_nome
                            inventario[index]["preco"]=novo_preco
                            print("Item alterado com sucesso.")
                        except ValueError:
                            print("Por favor, digite valores válidos para quantidade e preço.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há itens para alterar.")
        elif menu==4:
            if inventario:
                for i, item in enumerate(inventario):
                    print(f"{i + 1}. Nome: {item['nome']}, Quantidade: {item['quantidade']}, Preço: {item['preco']}")
            else:
                print("Não há itens para exibir.")
        elif menu==5:
            if inventario:
                valor_total=sum(item['quantidade'] * item['preco'] for item in inventario)
                print(f"Valor total do inventário: R$ {valor_total:.2f}")
            else:
                print("Não há itens no inventário.")
        elif menu==6:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 6.")
    except ValueError:
        print("Por favor, digite um número válido.")