#exercício-05.Controle de Gastos Mensais
descrição = []
valor = []
while True:
    try:
        print("\nControle de Gastos Mensais.")
        print("1. Adicionar gasto\n2. Remover gasto\n3. Alterar gasto\n4. Exibir todos os gastos\n5. Calcular total de gasto\n6. Sair")
        menu = int(input("Digite o número desejado: "))
        if menu == 1:
            while True:
                descrição_gasto = input("Digite a descrição do gasto: ")
                if descrição_gasto:
                    break
                else:
                    print("Por favor, digite a descrição do gasto.")
            while True:
                try:
                    valor_gasto = float(input("Digite o valor do gasto: "))
                    break
                except ValueError:
                    print("Por favor, digite um valor válido.")
            descrição.append(descrição_gasto)
            valor.append(valor_gasto)
            print("Ação realizada com sucesso.")
        elif menu == 2:
            while True:
                if descrição:
                    for i, (desc, val) in enumerate(zip(descrição, valor)):
                        print(f"{i + 1}. Descrição: {desc}, Valor: {val}")
                    try:
                        remover = int(input("Digite o número do gasto que deseja remover: "))
                        if 1 <= remover <= len(descrição):
                            index = remover - 1
                            certeza = int(input("Você têm certeza que deseja remover esse gasto? Digite 1 para \"sim\" e 2 para \"não\": "))
                            if certeza == 1:
                                print(f"Removendo gasto: Descrição: {descrição[index]}, Valor: {valor[index]}")
                                descrição.pop(index)
                                valor.pop(index)
                                print("Gasto removido com sucesso.")
                            else:
                                print("Operação cancelada.")
                            break
                        else:
                            print("Número inválido. Por favor, tente novamente.")
                    except ValueError:
                        print("Por favor, digite um número válido.")
                else:
                    print("Não há gastos para remover.")
                    break
        elif menu == 3:
            if descrição:
                for i, (desc, val) in enumerate(zip(descrição, valor)):
                    print(f"{i + 1}. Descrição: {desc}, Valor: {val}")
                try:
                    alterar = int(input("Digite o número do gasto que deseja alterar: "))
                    if 1 <= alterar <= len(descrição):
                        index = alterar - 1
                        nova_descrição = input("Digite a nova descrição: ")
                        while True:
                            try:
                                novo_valor = float(input("Digite o novo valor: "))
                                break
                            except ValueError:
                                print("Por favor, digite um valor válido.")
                        descrição[index] = nova_descrição
                        valor[index] = novo_valor
                        print("Gasto alterado com sucesso.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há gastos para alterar.")
        elif menu == 4:
            if descrição:
                for i, (desc, val) in enumerate(zip(descrição, valor)):
                    print(f"{i + 1}. Descrição: {desc}, Valor: {val}")
            else:
                print("Não há gastos para exibir.")
        elif menu == 5:
            total = sum(valor)
            print(f"Total de gastos: R$ {total:.2f}")
        elif menu == 6:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 6.")
    except ValueError:
        print("Por favor, digite um número válido.")
