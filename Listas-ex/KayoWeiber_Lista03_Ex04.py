tarefas = []
while True:
    try:
        print("\nLista de Tarefas")
        print("1. Adicionar tarefa\n2. Remover tarefa\n3. Alterar tarefa\n4. Marcar tarefa como concluída\n5. Exibir todas as tarefas\n6. Sair")
        menu=int(input("Digite o número desejado: "))
        if menu==1:
            while True:
                titulo_tarefa=input("Digite o título da tarefa: ")
                if titulo_tarefa:
                    break
                else:
                    print("Por favor, digite o título da tarefa.")
            tarefa={"titulo": titulo_tarefa, "status": "pendente"}
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso.")
        elif menu==2:
            if tarefas:
                for i, tarefa in enumerate(tarefas):
                    print(f"{i + 1}. Título: {tarefa['titulo']}, Status: {tarefa['status']}")
                try:
                    remover = int(input("Digite o número da tarefa que deseja remover: "))
                    if 1<=remover<=len(tarefas):
                        index=remover-1
                        tarefas.pop(index)
                        print("Tarefa removida com sucesso.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há tarefas para remover.")
        elif menu==3:
            if tarefas:
                for i, tarefa in enumerate(tarefas):
                    print(f"{i + 1}. Título: {tarefa['titulo']}, Status: {tarefa['status']}")
                try:
                    alterar=int(input("Digite o número da tarefa que deseja alterar: "))
                    if 1<=alterar<=len(tarefas):
                        index=alterar-1
                        novo_titulo=input("Digite o novo título: ")
                        tarefas[index]["titulo"]=novo_titulo
                        print("Tarefa alterada com sucesso.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há tarefas para alterar.")
        elif menu==4:
            if tarefas:
                for i, tarefa in enumerate(tarefas):
                    print(f"{i + 1}. Título: {tarefa['titulo']}, Status: {tarefa['status']}")
                try:
                    concluir=int(input("Digite o número da tarefa que deseja marcar como concluída: "))
                    if 1 <= concluir <= len(tarefas):
                        index=concluir-1
                        tarefas[index]["status"]="concluída"
                        print("Tarefa marcada como concluída.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há tarefas para concluir.")
        elif menu==5:
            if tarefas:
                for i, tarefa in enumerate(tarefas):
                    print(f"{i + 1}. Título: {tarefa['titulo']}, Status: {tarefa['status']}")
            else:
                print("Não há tarefas para exibir.")
        elif menu==6:
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 6.")
    
    except ValueError:
        print("Por favor, digite um número válido.")
