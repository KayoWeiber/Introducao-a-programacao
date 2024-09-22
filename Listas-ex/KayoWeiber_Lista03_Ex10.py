#exercício-10.Cadastro de Funcionários
funcionarios = []
while True:
    try:
        print("\nCadastro de Funcionários")
        print("1. Adicionar funcionário\n2. Remover funcionário\n3. Alterar funcionário\n4. Exibir todos os funcionários\n5. Calcular folha de pagamento total\n6. Sair")
        menu=int(input("Digite o número desejado: "))
        if menu==1:
            nome_funcionario=input("Digite o nome do funcionário: ")
            cargo_funcionario=input("Digite o cargo do funcionário: ")
            try:
                salario_funcionario=float(input("Digite o salário do funcionário: "))
                funcionario={"nome": nome_funcionario, "cargo": cargo_funcionario, "salario": salario_funcionario}
                funcionarios.append(funcionario)
                print("Funcionário adicionado com sucesso.")
            except ValueError:
                print("Por favor, digite um valor válido para o salário.")
        elif menu==2:
            if funcionarios:
                for i, funcionario in enumerate(funcionarios):
                    print(f"{i + 1}. Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}, Salário: {funcionario['salario']}")
                try:
                    remover=int(input("Digite o número do funcionário que deseja remover: "))
                    if 1 <=remover<=len(funcionarios):
                        index=remover-1
                        funcionarios.pop(index)
                        print("Funcionário removido com sucesso.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há funcionários para remover.")
        elif menu==3:
            if funcionarios:
                for i, funcionario in enumerate(funcionarios):
                    print(f"{i + 1}. Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}, Salário: {funcionario['salario']}")
                try:
                    alterar=int(input("Digite o número do funcionário que deseja alterar: "))
                    if 1<=alterar<=len(funcionarios):
                        index=alterar-1
                        novo_nome=input("Digite o novo nome: ")
                        novo_cargo=input("Digite o novo cargo: ")
                        try:
                            novo_salario = float(input("Digite o novo salário: "))
                            funcionarios[index]["nome"]=novo_nome
                            funcionarios[index]["cargo"]=novo_cargo
                            funcionarios[index]["salario"]=novo_salario
                            print("Funcionário alterado com sucesso.")
                        except ValueError:
                            print("Por favor, digite um valor válido para o salário.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há funcionários para alterar.")
        elif menu==4:
            if funcionarios:
                for i, funcionario in enumerate(funcionarios):
                    print(f"{i + 1}. Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}, Salário: {funcionario['salario']}")
            else:
                print("Não há funcionários para exibir.")
        elif menu==5:
            if funcionarios:
                folha_pagamento=sum(funcionario['salario'] for funcionario in funcionarios)
                print(f"Folha de pagamento total: R$ {folha_pagamento:.2f}")
            else:
                print("Não há funcionários na folha de pagamento.")
        elif menu==6:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 6.")
    except ValueError:
        print("Por favor, digite um número válido.")
