#exercício-06.Gerenciamento de Biblioteca
biblioteca = []
while True:
    try:
        print("\nGerenciamento de Biblioteca")
        print("1. Adicionar livro\n2. Remover livro\n3. Alterar livro\n4. Marcar livro como emprestado\n5. Exibir todos os livros\n6. Sair")
        menu=int(input("Digite o número desejado: "))
        if menu==1:
            titulo_livro=input("Digite o título do livro: ")
            autor_livro=input("Digite o autor do livro: ")
            livro={"titulo": titulo_livro, "autor": autor_livro, "status": "disponível"}
            biblioteca.append(livro)
            print("Livro adicionado com sucesso.")
        elif menu==2:
            if biblioteca:
                for i, livro in enumerate(biblioteca):
                    print(f"{i + 1}. Título: {livro['titulo']}, Autor: {livro['autor']}, Status: {livro['status']}")
                try:
                    remover=int(input("Digite o número do livro que deseja remover: "))
                    if 1<=remover<=len(biblioteca):
                        index=remover-1
                        biblioteca.pop(index)
                        print("Livro removido com sucesso.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há livros para remover.")
        elif menu==3:
            if biblioteca:
                for i, livro in enumerate(biblioteca):
                    print(f"{i + 1}. Título: {livro['titulo']}, Autor: {livro['autor']}, Status: {livro['status']}")
                try:
                    alterar=int(input("Digite o número do livro que deseja alterar: "))
                    if 1<=alterar<=len(biblioteca):
                        index=alterar-1
                        novo_titulo=input("Digite o novo título: ")
                        novo_autor=input("Digite o novo autor: ")
                        biblioteca[index]["titulo"]=novo_titulo
                        biblioteca[index]["autor"]=novo_autor
                        print("Livro alterado com sucesso.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há livros para alterar.")
        elif menu==4:
            if biblioteca:
                for i, livro in enumerate(biblioteca):
                    print(f"{i + 1}. Título: {livro['titulo']}, Autor: {livro['autor']}, Status: {livro['status']}")
                try:
                    emprestar= int(input("Digite o número do livro que deseja marcar como emprestado: "))
                    if 1<=emprestar<=len(biblioteca):
                        index=emprestar-1
                        biblioteca[index]["status"]="emprestado"
                        print("Livro marcado como emprestado.")
                    else:
                        print("Número inválido. Por favor, tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há livros para emprestar.")
        elif menu==5:
            if biblioteca:
                for i, livro in enumerate(biblioteca):
                    print(f"{i + 1}. Título: {livro['titulo']}, Autor: {livro['autor']}, Status: {livro['status']}")
            else:
                print("Não há livros para exibir.")
        elif menu==6:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 6.")
    except ValueError:
        print("Por favor, digite um número válido.")
