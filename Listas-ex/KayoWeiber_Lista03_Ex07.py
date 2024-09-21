#exercício-07.Sistema de Notas de Alunos
alunos = []
while True:
    try:
        print("\nSistema de Notas de Alunos")
        print("1. Adicionar aluno\n2. Remover aluno\n3. Adicionar nota ao aluno\n4. Exibir notas do aluno\n5. Calcular média do aluno\n6. Exibir todos os alunos e suas médias\n7. Sair")
        menu=int(input("Digite o número desejado: "))
        if menu==1:
            nome_aluno = input("Digite o nome do aluno: ")
            aluno = {"nome": nome_aluno, "notas": []}
            alunos.append(aluno)
            print("Aluno adicionado com sucesso.")
        elif menu==2:
            if alunos:
                for i, aluno in enumerate(alunos):
                    print(f"{i + 1}. Nome: {aluno['nome']}")
                try:
                    remover=int(input("Digite o número do aluno que deseja remover: "))
                    if 1<=remover<=len(alunos):
                        index=remover-1
                        alunos.pop(index)
                        print("Aluno removido com sucesso.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há alunos para remover.")
        elif menu==3:
            if alunos:
                for i, aluno in enumerate(alunos):
                    print(f"{i + 1}. Nome: {aluno['nome']}")
                try:
                    adicionar_nota=int(input("Digite o número do aluno que deseja adicionar nota: "))
                    if 1<=adicionar_nota<=len(alunos):
                        index=adicionar_nota-1
                        try:
                            nota=float(input("Digite a nota: "))
                            alunos[index]["notas"].append(nota)
                            print("Nota adicionada com sucesso.")
                        except ValueError:
                            print("Por favor, digite uma nota válida.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há alunos para adicionar nota.")
        elif menu==4:
            if alunos:
                for i, aluno in enumerate(alunos):
                    print(f"{i + 1}. Nome: {aluno['nome']}")
                try:
                    exibir_notas=int(input("Digite o número do aluno para exibir as notas: "))
                    if 1 <=exibir_notas<=len(alunos):
                        index=exibir_notas-1
                        print(f"Notas de {alunos[index]['nome']}: {alunos[index]['notas']}")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há alunos para exibir notas.")
        elif menu==5:
            if alunos:
                for i, aluno in enumerate(alunos):
                    print(f"{i + 1}. Nome: {aluno['nome']}")
                try:
                    calcular_media=int(input("Digite o número do aluno para calcular a média: "))
                    if 1<=calcular_media<=len(alunos):
                        index=calcular_media-1
                        notas=alunos[index]["notas"]
                        if notas:
                            media=sum(notas) / len(notas)
                            print(f"Média de {alunos[index]['nome']}: {media:.2f}")
                        else:
                            print("Este aluno não possui notas.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há alunos para calcular média.")
        elif menu==6:
            if alunos:
                for aluno in alunos:
                    notas=aluno["notas"]
                    if notas:
                        media=sum(notas) / len(notas)
                        print(f"Nome: {aluno['nome']}, Média: {media:.2f}")
                    else:
                        print(f"Nome: {aluno['nome']}, Média: N/A")
            else:
                print("Não há alunos para exibir.")
        elif menu==7:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 7.")
    except ValueError:
        print("Por favor, digite um número válido.")
