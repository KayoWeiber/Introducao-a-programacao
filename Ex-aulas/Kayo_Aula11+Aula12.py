
#Disciplina: Introdução à Programação
#Aluno(a): Kayo Weiber Freire Martins

# Aula 11 - Exercícios

# Aula 11 - Exercício 1
palavra = str(input("Digite uma palavra: "))
print("A quantidade de letras é:", len(palavra))

# Aula 11 - Exercício 2
string = str(input("Digite uma palavra: "))
print("A primeira letra é:", string[0])
print("A última letra é:", string[-1])

#Aula 11 - Exercício 3
string=str(input("Digite uma palavra:"))
print(string[1::2])

#Aula 11 - Exercício 4
string=str(input("Digite uma palavra:"))
if string==string[::-1]:
    print("Seu nome é palídromo")
else:
    print("Seu nome não é palídromo")

#Aula 11 - Exercício 5
string=str(input("Digite uma palavra:"))
print(string.replace("a","i"))

#Aula 11 - Exercício 6
palavra1=str(input("Digite uma palavra: "))
palavra2=str(input("Digite outra palavra: "))
print(f"A concatenação dessas palavras será {palavra1+palavra2} ou com espaço {palavra1+' '+palavra2} ")

#Aula 11 - Exercício 7
palavra=str(input("Digite uma palavra: "))
print(f"A palavra {palavra} de trás para frente fica dessa forma:{palavra[::-1]}")

#Aula 11 - Exercício 8
palavra=str(input("Digite uma palvra:")).lower()
caractere=str(input("Digite o caractere que deseja contar:")).lower()
countador=palavra.count(caractere)
print(f'A quantida do caractere {caractere} que aparece na palavra {palavra} é {countador}')


#Aula 11 - Exercício 9
palavra=str(input("Digite uma palavra:"))
seq=str(input("Digite a sequência que deseja saber se a palavra segue:"))
inicio=palavra.startswith(seq)
final=palavra.endswith(seq)
if inicio:
    print(f"A palavra inicia com a sequência {seq}")
elif final:
    print(f"A palavra tem a sequência final de {seq}")
else:
    print("A aplavra não atende nenhuma sequência citada")


#Aula 11 - Exercício 10
frase=str(input("Digite uma frase a ser capitalizada:"))
cap=frase.title()
print(f"A frase capitalizada ficará \"{cap}\"")

#Aula 12 - Exercício 1
lista=[]
count=0
for i in range(0,5):
    count+=1
    número=int(input(f"{count} Digite um número para à lista:"))
    lista.append(número)
print(f"Os números introduzidos na lista são: {lista}")

#Aula 12 - Exercício 2
lista=[]
count=0
for i in range(0,10):
    count+=1
    num=int(input(f"{count} Digite um número para à lista:"))
    lista.append(num)
lista.sort(reverse=True)
print(f"Os números introduzidos exibindo em ordem reversa na lista são: {lista}")


#Aula 12 - Exercício 3
lista=[]
count=0
for i in range(0,4):
    count+=1
    nota=float(input(f"Digite a nota {count}:"))
    lista.append(nota)
quant=len(lista)
soma=sum(lista)
media=soma/quant
print(f"A media da nota inserida é {media}")


#Aula 12 - Exercício 4
lista=[]
vogais=["a","e","i","o","u"]
count=0
cons=[]
while count!=10:
    count+=1
    letra = input(f"{count} Digite uma única letra: ")
    if len(letra) == 1 and letra.isalpha():
        lista.append(letra)
        if letra not in vogais:
            cons.append(letra)
    else:
        print("Entrada inválida. Por favor, digite apenas uma letra.")
quant=len(cons)
num=len(lista)
print(f"A Quantidade de letras digitadas foi {num} e a quantidade de consoantes foram {quant} \nque são {cons}")


#Aula 12 - Exercício 5
lista=[]
par=[]
impar=[]
count=0
while count!=20:
    try:
        count+=1
        num=int(input(f"{count}. Digite um número inteiro: "))
        lista.append(num)
        if num%2==0:
            par.append(num)
        else:
            impar.append(num)
    except ValueError:
        print("O valor digitado precisa ser um número interiro.")
print(f"Os Números digitados foram:{lista}")
print(f"Os números pares inseridos foram:{par}")
print(f"Os números ímpares inseridos foram:{impar}")



#Aula 12 - Exercício 6
count=0
maxi=0
while True:
    saltos=[]
    try:
        name=str(input("Digite o nome do atleta (para finalizar aperte ENTER sem inserir dados):"))
        if name=="":
            print("Programa finalizado.")
            break
        else:
            while count!=5:
               try:
                   count+=1
                   salto=float(input(f"Digite a altura do salto número {count}: "))
                   saltos.append(salto)
                   if salto>maxi:
                       maxi=salto 
               except ValueError:
                   print("O valor informado precisa ser um número.")
                   count-=1
            quant=len(saltos)
            soma=sum(saltos)
            media=soma/quant
            
            print("")
            print(f"atleta: {name}")
            print("")
            print(f"Primeiro Salto: {saltos[0]}")
            print(f"Segundo Salto: {saltos[1]}")
            print(f"Terceiro Salto: {saltos[2]}")
            print(f"Quarto Salto: {saltos[3]}")
            print(f"Quinto Salto: {saltos[4]}")
            print("")
            print(f"Resultado final: {maxi}")
            print(f"Atleta: {name}")
            print(f"Saltos: {' - '.join(map(str, saltos))}")
            print(f"Média dos Saltos:{round(media,2)}")
            
    except ValueError:
        print("O dado digitado está incorreto")



#Aula 12 - Exercício 7
try:
    count=0
    Sistemas=["Windows Server","Unix","Linux","Netware","Mac OS","Outros"]
    resposta={"Num 1":0, "Num 2":0,"Num 3":0, "Num 4":0, "Num 5":0,"Num 6":0}
    while True:
        try:
            print("Por Favor, responda!")
            print("As Possíveis respostas são:\n1-Windows Server\n2-Unix\n3-Linux\n4-Netware\n5-Mac OS\n6-Outros")
            res=int(input("Qual o melhor Sistema Operacional para o uso em servidores?(Digite 0 para finalizar o Programa)"))
            
            if res==0:
                print("Programa Finalizado")
                break
            elif res>=1 and res<=6:
                count+=1
                escolha=f"Num {res}"
                resposta[escolha]+=1
            else:
                print("O valor digitado não é válido, por favor digite um valor entre 0 e 6")   
        except ValueError:
            print("Valor inválido, Por favor digte um número inteiro.")

    porcentagens = {sistema: (resposta[f"Num {i+1}"] / count) * 100 for i, sistema in enumerate(Sistemas)}
    print("\nResultados da Votação:")
    print("{:<20} {:<10} {:<15}".format("Sistema Operacional", "Votos", "Porcentagem"))
    print("-" * 45)
    for i, sistema in enumerate(Sistemas):
        votos = resposta[f"Num {i+1}"]
        porcentagem = porcentagens[sistema]
        print("{:<20} {:<10} {:.2f}%".format(sistema, votos, porcentagem))
    print("-" * 45)
    print(f"Total de votos: {count}")
    vencedor = max(porcentagens, key=porcentagens.get)
    totalvotos=resposta[f"Num {Sistemas.index(vencedor)+1}"]
    print(f"O Sistema Operacional mais votado foi o {vencedor}, com {totalvotos} votos, correspondendo a {porcentagens[vencedor]:.2f}")

except ZeroDivisionError:
    print("Nenhum dado foi inserido.")


#Aula 12 - Exercício 8
import random
count=0
dado={"numero 1":0,"numero 2":0,"numero 3":0,"numero 4":0,"numero 5":0,"numero 6":0}
for i in range(0,100):
    count+=1
    res=random.randint(1, 6)
    valor=f"numero {res}"
    dado[valor]+=1
vencedor=max(dado,key=dado.get)
totalvotos=dado[vencedor]
print(f"O número vencedor foi o {vencedor} com {totalvotos} vezes aparecidos")
print(dado)