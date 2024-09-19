#exercício-01.Gerenciamento de Contatos
lista=[]
telefone=[]
while True:
    try:
        print("Gerenciamento de Contatos.")
        print("1. Adicionar contato\n2. Remover Contato\n3. Alterar contato\n4. Exibir os contatos\n5. Sair")
        menu=int(input("Digite o número desejado: "))
        if menu==1:
            while True:
                try:
                    nome=str(input("Digite o nome do contato:")).title()
                    break
                except ValueError:
                    print("Por favor, digite o nome do contato.")
            while True:
                try:
                    fone=str(input("Digite o número de telefone:"))
                    break
                except ValueError:
                    print("Por favor, digite o número de contato.")
            lista.append(nome)
            telefone.append(fone)
            print("Ação realizada com sucesso.")
        elif menu==2:
            while True:
                try:
                    remover=str(input("Digite o nome do contato que deseja remover: ")).title()
                    break
                except ValueError:
                    print("Por favor, digite o nome do contato que deseja remover.")
            if remover in lista:
                index=lista.index(remover)
                while True:
                    try:
                        certeza=int(input("Você têm certeza que deseja remover esse contato? Digite 1 para \"sim\" e 2 para \"não\""))
                        if certeza==1:
                            lista.pop(index)
                            telefone.pop(index)
                            print(f"{remover} foi removido da lista.")
                            break
                        elif 2:
                            print("Operação cancelada.")
                            break
                        else:
                            print("Por favor, digite uma das opções")
                                
                    except ValueError:
                        print("A Informação digitado está incorreto.")
            else:
                print("O nome de contato digitado não possui nos contatos.")
        elif menu==3:
            while True:
                try:
                    alterar=str(input("Digite o nome do contato que deseja alterar: ")).title()
                    break
                except ValueError:
                    print("Por favor, digite o nome do contato que deseja remover.")
            if alterar in lista:
                op=int(input("Você deseja alterar o nome ou o número? (Digite 1 para número e 2 para nome):"))
                index = lista.index(alterar)
                while True:
                    try:
                        if op == 1:
                            novonum=str(input("Digite o novo número:"))
                            telefone[index]=novonum
                            print(f"O número de {alterar} foi mudado para {novonum}")
                            break
                        elif op==2:
                            novonome=str(input("Digite o novo nome do contato:"))
                            lista[index]=novonome
                            print(f"O nome de {alterar} foi mudado para {novonome}")
                            break
                        else:
                            print("O valor digitado não é válido")
                    except ValueError:
                        print("Valor inválido, tente novamente.")
            else:
                print("O nome de contato digitado não possui nos contatos.")  
        elif menu==4:
            print("{:<20} {:<15}".format("Nomes do Contato", "Número do Contato"))
            for nome, numero in zip(lista, telefone):
                print("{:<20} {:<15}".format(f"Nome: {nome}", f"Número: {numero}"))
        elif menu==5:
            print("Programa encerrado.")
            break
        else:
            print("Por favor, digitar um dos valores mostrados anteriormente")
    
    except ValueError:
        print("Valor Inválido, Tente novamente")
