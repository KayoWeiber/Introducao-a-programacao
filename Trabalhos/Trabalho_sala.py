#Gerenciador de dados e fluxo de caixa de uma empresa
cliente=[]
nome2 = []
quantidade = []
preço = []
clientes = []
produtos = []
caixa = []
receitas = []
despesas = []
while True:
    while True:
            try:
                print("Gerenciador de dados e fluxo de caixa")
                print("1.cliente\n2.Produtos\n3.Caixa\n4.Sair")
                menu=int(input("Digite a opção desejada: "))
                break
            except ValueError:
                print("Valor inválido, Digite umas das opções citadas.")
    if menu==1:
        while True:
            while True:
                print()
                print("Selecione umas das opções")
                print("1.Cadastrar Cliente\n2.Excluir Cliente\n3.Alterar Cliente\n4.Mostrar todos os clientes\n5.Voltar ao menu anterior")
                try:
                    menu2=int(input("Digite a opção desejada: "))
                except ValueError:
                    print("Valor inválido, Digite umas das opções citadas.")
                if menu2==1:
                    while True:
                        try:
                            nome=str(input("Digite o nome do cliente:")).title()
                            break
                        except ValueError:
                            print("Por favor, digite o nome do contato.")
                    while True:
                        try:
                            fone=str(input("Digite o número de telefone:"))
                            break
                        except ValueError:
                            print("Por favor, digite o número de contato.")
                    cadastro={"nome": nome, "telefone": fone}
                    cliente.append(cadastro)
                    print("Ação realizada com sucesso.")
                    break
                elif menu2==2:
                    while True:
                        if cliente:
                            for i, cadastro in enumerate(cliente):
                                print(f"{i + 1}. nome:{cadastro["nome"]}, telefone:{cadastro["telefone"]}")
                            try:
                                remover=int(input("Digite o número do cadastro que deseja remover: "))
                                try:
                                    certeza=int(input("Você têm certeza que deseja remover esse contato? Digite 1 para \"sim\" e 2 para \"não\""))
                                except ValueError:
                                    print("Por favor, digite um número inteiro.")
                                if certeza==1:
                                    if 1<=remover<=len(cliente):
                                        index=remover-1
                                        cliente.pop(index)
                                        print("Cadastro removido com sucesso.")
                                        break
                                    else:
                                        print("Número inválido. Por favor, tente novamente.")
                                elif 2:
                                    print("Operação cancelada.")
                                    break
                                else:
                                    print("Por favor, digite uma das opções")

                            except ValueError:
                                print("Por favor, digite um número válido.")
                        else:
                            print("Não há cadastro para remover.")
                elif menu2==3:
                    while True:
                        if cliente:
                            for i, cadastro in enumerate(cliente):
                                print(f"{i + 1}. nome:{cadastro["nome"]}, telefone:{cadastro["telefone"]}")
                            try:
                                alterar=int(input("Digite o número do livro que deseja alterar: "))
                                if 1<=alterar<=len(cliente):
                                    index=alterar-1
                                    try:
                                        print("Opções:\n1.Nome\n2.Telefone\n3.Tudo do cadastro")
                                        escolha_alterar=int((input("Oque você deseja alterar do cadastro:")))
                                    except ValueError:
                                        print("Digite um número inteiro")
                                    if escolha_alterar==3:
                                        novo_nome=input("Digite o novo nome: ")
                                        novo_telefone=input("Digite o novo telefone: ")
                                        cliente[index]["nome"]=novo_nome
                                        cliente[index]["telefone"]=novo_telefone
                                        print("Cadastro alterado com sucesso.")
                                        break
                                    elif escolha_alterar==2:
                                        novo_telefone=input("Digite o novo telefone: ")
                                        cliente[index]["telefone"]=novo_telefone
                                        break
                                    elif escolha_alterar==1:
                                        novo_nome=input("Digite o novo nome: ")
                                        cliente[index]["nome"]=novo_nome
                                        break
                                    else:
                                        print("Por favor, digite um número válido.")
                                        
                                else:
                                    print("Número inválido. Por favor, tente novamente.")
                            except ValueError:
                                print("Por favor, digite um número válido.")
                        else:
                            print("Não há livros para alterar.")
                elif menu2==4:
                    if cliente:
                        for i, cadastro in enumerate(cliente):
                            print(f"{i + 1}. nome:{cadastro["nome"]}, telefone:{cadastro["telefone"]}")
                    else:
                        print("Não há livros para exibir.")
                elif menu2==5:
                    break   
                else:
                    print("Digite um valor válido")
            if menu2==5:
                print("Retornando para o menu anterior.")     
                break     
    elif menu==2:

        while True:
            try:
                print("Registro de Produtos em Estoque.")
                print("1. Adicionar produto\n2. Exibir os produtos\n3.Somar valor de estoque\n4. Sair")
                menu3 = int(input("Digite o número desejado: "))  
                if menu3 == 1:
                    while True:
                        nome_produto = input("Digite o nome do produto: ").title()
                        if nome_produto:
                            break
                        else:
                            print("Por favor, digite o nome do produto.")
                    if nome_produto in nome2:
                        print("O nome do produto já existe no estoque.")
                        index = nome2.index(nome_produto)
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
                                nome2.append(nome_produto)
                                quantidade.append(quant)
                                preço.append(pre)
                                print("Ação realizada com sucesso.")
                                break
                            except ValueError:
                                print("Por favor, digite o valor do produto.")
                elif menu3==2:
                    if nome2:
                        print("Produtos em estoque:")
                        for n, q, p in zip(nome2, quantidade, preço):
                            print(f"Nome: {n}, Quantidade: {q}, Preço: {p:.2f}")
                    else:
                        print("Não há produtos no estoque.")
                elif menu3==3:
                    valor_teste=[]
                    for i in range(len(quantidade)):
                        valor_estoque = quantidade[i] * preço[i]
                        valor_teste.append(valor_estoque)
                    sum_valor = sum(valor_teste)
                    print(f"\n Total do valor de estoque: R${sum_valor:.2f}")
                elif menu3==4:
                    print("Programa encerrado.")
                    break
                else:
                    print("Por favor, digite um número válido.")
            except ValueError:
                print("Valor inválido, tente novamente.")
            if menu3==4:
                print("Voltando ao menu anterior.")
                break
    elif menu==3:
        def adicionar_receita():
            descricao = input("Digite a descrição da receita: ")
            valor = float(input("Digite o valor da receita: "))
            caixa.append(("receita", descricao, valor))
            receitas.append(("Receitas", descricao, valor))
        def adicionar_despesa():
            descricao = input("Digite a descrição da despesa: ")
            valor = float(input("Digite o valor da despesa: "))
            caixa.append(("despesa", descricao, valor))
            despesas.append(("Despesas", descricao, valor))
        def mostrar_movimentacao():
            saldo = 0
            for tipo, descricao, valor in caixa:
                if tipo == "receita":
                    saldo += valor
                else:
                    saldo -= valor
            print(f"Saldo atual: R${saldo:.2f}")
        while True:
            print("\nMenu:")
            print("1. Adicionar receita")
            print("2. Adicionar despesa")
            print("3. Mostrar movimentação do caixa e saldo")
            print("4. Sair")
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    adicionar_receita()
                elif opcao == 2:
                    adicionar_despesa()
                elif opcao == 3:
                    mostrar_movimentacao()
                    print("\nCaixa:")
                    for tipo, descricao, valor in caixa:
                        print(f"{tipo}: {descricao} - R${valor:.2f}")
                elif opcao == 4:
                    print("1. Sim")
                    print("2. Não")
                    n=int(input("Tem certeza que deseja sair?"))
                    if n == 1:
                        print("Até mais!")
                        break
                    else:
                        continue
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Opção inválida. Digite um número.")
    elif menu==4:
        try:
            certeza_2=int(input("Você têm certeza que deseja sair do programa?"))
            print("1. Sim")
            print("2. Não")
            n=int(input("Tem certeza que deseja sair?"))
            if n == 1:
                print("Programa encerrado.")
                break
            else:
                continue
        except ValueError:
            print("Por Favor, Digite um número inteiro")

    else:
        print("Por favor, digite um número válido.")