'''#ex01
def cal(num1,num2):
    soma=num1+num2
    print(f"A soma dos números digitado será {soma}")
cal(int(input("Digite o número 1 a ser somado:")),int(input("Digite o número 2 a ser somado:")))

#ex02
def lista(listas):
    maior_num=max(listas)
    print(f"O maior número digitado é {maior_num}")
list=[]
while True:
    try:
        num=int(input("Digite um número a ser adicionado a lista (digite 0 para finalizar o programa): "))
        if num==0:
            print("lista foi criada.")
            break
        else:
            list.append(num)
    except ValueError:
        print("Por favor, digite um número positivo.")
lista(list)

#ex03
def conta_vogais(string):
    string=string.lower()
    vogais=["a", "e", "i", "o", "u"]
    contador=0
    for i in string:
        if i in vogais:
            contador+=1
    print(f"A string possui {contador} vogais.")
conta_vogais(input("Digite uma string para descobrir quantas vogais possui nela: "))

#ex04
def media_lista(lista):
    quant=len(lista)
    soma=sum(lista)
    print(f"A média da lista será: {soma/quant:.2f}")
list=[]
while True:
    try:
        num=float(input("Digite um número a ser adicionado a lista para realizar a média (digite 0 para finalizar o programa): "))
        if num==0:
            print("lista foi criada.")
            break
        elif num<0:
            print("Por favor, digite um número positivo")
        else:
            list.append(num)
    except ValueError:
        print("Por favor, digite um número positivo.")
media_lista(list)


#ex05
def numero_primo(numeros):
    for numero in numeros:
        if numero<2:
            print(f"{numero} não é primo.")
        else:
            for i in range(2,numero):
                if numero%i==0:
                    print(f"{numero} não é primo.")
                    break
            else:
                print(f"{numero} é primo.")          
list=[]
while True:
    try:
        num=int(input("Digite um número a ser adicionado a lista (digite 0 para finalizar o programa): "))
        if num==0:
            print("lista foi criada.")
            break
        elif num<0:
            print("Por favor, digite um número positivo")
        else:
            list.append(num)
    except ValueError:
        print("Por favor, digite um número positivo.")
numero_primo(list)

#ex06
def palíndromo(texto):
    texto=texto.lower()
    invertido=texto[::-1]
    if invertido==texto:
        print(f"A palavra {texto} é palíndromo.")
    else:
        print(f"A palavra {texto} não é palíndromo.")
while True:
        try: 
            texto_entrada=str(input("Digite o texto para verificação de palíndromo (digite 0 para finalizar):"))
            if texto_entrada=="0":
                print("Programa finalizado")
                break
            else:
                palíndromo(texto_entrada)
        except ValueError:
            print("O valor digitado não é válido.")

#ex07
def lista_pares(números):
    lista_par=[]
    for i in números:
        if i%2==0:
            lista_par.append(i)
    print("Os números digitados que são pares são:")
    for i in lista_par:
        print(i)
            
lista_números=[]
while True:
    try:
        num=int(input("Digite os números a ser adicionado a lista (digite 00 para executar a função): "))
        if num==00:
            lista_pares(lista_números)
            break
        else:
            lista_números.append(num)
    except ValueError:
        print("O valor digitado não é válido.")

#ex08
def contador_letras(lista_string):
    lista_palavras=[]
    for palavras in lista_string:
        letras=len(palavras)
        if letras>5:
            lista_palavras.append(palavras)
    print("As palavras digitadas que possuem mais de 5 letras são: ")
    for i in lista_palavras:
        print(i)
lista_str=[]
while True:
    try:
        strings=str(input("Digite uma palavra a ser adicionando a lista(digite 0 para executar a função): "))
        if strings=="0":
            break
        else:
            lista_str.append(strings)    
    except ValueError:
        print("O valor digitado não é válido")
contador_letras(lista_str)

#ex09
def tabuada(numero):
    numbers=[1,2,3,4,5,6,7,8,9,10]
    print(f"Tabuada do número {numero}:")
    for i in numbers:
        soma=numero*i
        print(f"{numero} x {i} = {soma}")
tabuada(int(input("Digite o número que deseja saber a TABUADA: ")))
'''
#ex10
def produto(products):
    num=1
    for i in products:
        num*=i
    print(f"O produto dos números digitado é {num}")
lista=[]
while True:
    try:
        number=int(input("Digite o números a ser adicionado a lista (digite -100 para finalizar):"))
        if number==-100:
            break
        else:
            print("Número adicionado.")
            lista.append(number)
    except ValueError:
        print("O valor digita é inválido.")
produto(lista)