#exercício-03.Agenda de Compromissos
data = []
hora = []
descrição = []
while True:
    try:
        print("Gerenciamento de Compromissos.")
        print("1. Adicionar compromisso\n2. Remover compromisso\n3. Alterar compromisso\n4. Exibir os compromissos\n5. Sair")
        menu = int(input("Digite o número desejado: "))
        if menu == 1:
            #adicionar compromisso
            while True:
                data_compromisso = input("Digite a data do compromisso (DD/MM/AAAA): ")
                if data_compromisso:
                    break
                else:
                    print("Por favor, digite a data do compromisso.")
            hora_compromisso = input("Digite a hora do compromisso (HH:MM): ")
            descrição_compromisso = input("Digite a descrição do compromisso: ")
            if data_compromisso in data:
                index = data.index(data_compromisso)
                hora[index].append(hora_compromisso)
                descrição[index].append(descrição_compromisso)
            else:
                data.append(data_compromisso)
                hora.append([hora_compromisso])
                descrição.append([descrição_compromisso])
            print("Compromisso adicionado com sucesso.")
        elif menu == 2:
            while True:
                remover = input("Digite a data do compromisso que deseja remover (DD/MM/AAAA): ")
                if remover:
                    break
                else:
                    print("Por favor, digite a data do compromisso.")
            if remover in data:
                index = data.index(remover)
                print("Compromissos nessa data:")
                for i, (h, d) in enumerate(zip(hora[index], descrição[index])):
                    print(f"{i + 1}. Hora: {h}, Descrição: {d}")
                while True:
                    try:
                        qual_remover = int(input("Digite o número do compromisso que deseja remover ou 0 para remover todos: "))
                        if qual_remover == 0:
                            data.pop(index)
                            hora.pop(index)
                            descrição.pop(index)
                            print(f"Todos os compromissos em {remover} foram removidos.")
                            break
                        elif 1 <= qual_remover <= len(hora[index]):
                            hora[index].pop(qual_remover - 1)
                            descrição[index].pop(qual_remover - 1)
                            if not hora[index]:
                                data.pop(index)
                                hora.pop(index)
                                descrição.pop(index)
                            print(f"Compromisso {qual_remover} em {remover} foi removido.")
                            break
                        else:
                            print("Número inválido, tente novamente.")
                    except ValueError:
                        print("O valor informado é inválido.")
            else:
                print("O compromisso digitado não está na agenda.")
        elif menu == 3:
            #alterar compromisso
            while True:
                alterar = input("Digite a data do compromisso que deseja alterar (DD/MM/AAAA): ")
                if alterar:
                    break
                else:
                    print("Por favor, digite a data do compromisso.")
            if alterar in data:
                index = data.index(alterar)
                print("Compromissos nessa data:")
                for i, (h, d) in enumerate(zip(hora[index], descrição[index])):
                    print(f"{i + 1}. Hora: {h}, Descrição: {d}")
                while True:
                    try:
                        qual_alterar = int(input("Digite o número do compromisso que deseja alterar: "))
                        if 1 <= qual_alterar <= len(hora[index]):
                            op = int(input("Você deseja alterar a data, hora ou descrição do compromisso? (Digite 1 para data, 2 para hora e 3 para descrição): "))
                            if op == 1:
                                nova_data = input("Digite a nova data do compromisso (DD/MM/AAAA): ")
                                data.append(nova_data)
                                hora.append([hora[index][qual_alterar - 1]])
                                descrição.append([descrição[index][qual_alterar - 1]])
                                hora[index].pop(qual_alterar - 1)
                                descrição[index].pop(qual_alterar - 1)
                                if not hora[index]:
                                    data.pop(index)
                                    hora.pop(index)
                                    descrição.pop(index)
                                print(f"A data do compromisso foi alterada para {nova_data}.")
                            elif op == 2:
                                nova_hora = input("Digite a nova hora do compromisso (HH:MM): ")
                                hora[index][qual_alterar - 1] = nova_hora
                                print(f"A hora do compromisso foi alterada para {nova_hora}.")
                            elif op == 3:
                                nova_descrição = input("Digite a nova descrição do compromisso: ")
                                descrição[index][qual_alterar - 1] = nova_descrição
                                print(f"A descrição do compromisso foi alterada para {nova_descrição}.")
                            else:
                                print("O valor digitado não é válido.")
                            break
                        else:
                            print("Número inválido, tente novamente.")
                    except ValueError:
                        print("O valor informado é inválido.")
            else:
                print("O compromisso digitado não está na agenda.")
        elif menu == 4:
            # Exibir compromissos
            if data:
                print("Compromissos na agenda:")
                for d, hs, ds in zip(data, hora, descrição):
                    for h, desc in zip(hs, ds):
                        print(f"Data: {d}, Hora: {h}, Descrição: {desc}")
            else:
                print("Não há compromissos na agenda.")
        elif menu == 5:
            # Sair do programa
            print("Programa encerrado.")
            break
        else:
            print("Por favor, digite um número válido.")
    except ValueError:
        print("Valor inválido, tente novamente.")