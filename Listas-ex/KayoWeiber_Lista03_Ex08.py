#exercício-08.Catálogo de Filmes
filmes = []
while True:
    try:
        print("\nCatálogo de Filmes")
        print("1. Adicionar filme\n2. Remover filme\n3. Alterar filme\n4. Exibir todos os filmes\n5. Sair")
        menu=int(input("Digite o número desejado: "))
        if menu==1:
            titulo_filme=input("Digite o título do filme: ")
            genero_filme=input("Digite o gênero do filme: ")
            ano_filme=input("Digite o ano de lançamento do filme: ")
            filme={"titulo": titulo_filme, "genero": genero_filme, "ano": ano_filme}
            filmes.append(filme)
            print("Filme adicionado com sucesso.")
        elif menu==2:
            if filmes:
                for i, filme in enumerate(filmes):
                    print(f"{i + 1}. Título: {filme['titulo']}, Gênero: {filme['genero']}, Ano: {filme['ano']}")
                try:
                    remover=int(input("Digite o número do filme que deseja remover: "))
                    if 1 <=remover<=len(filmes):
                        index=remover-1
                        filmes.pop(index)
                        print("Filme removido com sucesso.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há filmes para remover.")
        elif menu==3:
            if filmes:
                for i, filme in enumerate(filmes):
                    print(f"{i + 1}. Título: {filme['titulo']}, Gênero: {filme['genero']}, Ano: {filme['ano']}")
                try:
                    alterar=int(input("Digite o número do filme que deseja alterar: "))
                    if 1<=alterar<=len(filmes):
                        index=alterar-1
                        novo_titulo=input("Digite o novo título: ")
                        novo_genero=input("Digite o novo gênero: ")
                        novo_ano=input("Digite o novo ano de lançamento: ")
                        filmes[index]["titulo"]=novo_titulo
                        filmes[index]["genero"]=novo_genero
                        filmes[index]["ano"]=novo_ano
                        print("Filme alterado com sucesso.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há filmes para alterar.")
        elif menu==4:
            if filmes:
                for i, filme in enumerate(filmes):
                    print(f"{i + 1}. Título: {filme['titulo']}, Gênero: {filme['genero']}, Ano: {filme['ano']}")
            else:
                print("Não há filmes para exibir.")
        elif menu==5:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")
    except ValueError:
        print("Por favor, digite um número válido.")