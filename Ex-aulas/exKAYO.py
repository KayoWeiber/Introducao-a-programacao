
#ex01
idade=int(input("Digite sua idade:"))
if(idade>=18):
    print(f"Atingiu a maior idade")


#ex02
senha=str(input("Digite sua senha:"))
if(senha=="eu1234"):
    print(f"Senha correta")


#ex03
idade=int(input("Digite sua idade:"))
if idade>=18:
    print("Atingiu a Maioridade")
else:
    print("Não atingiu a maioridade")

#ex04
senha=str(input("Digite sua senha:"))
if senha=="eu1234":
    print("Senha correta")
else:
    print("Senha invalida")

#ex05
idade=int(input("Digite sua idade:"))
if idade>0 and idade <=12:
    print("Você é uma criança")
elif idade>12 and idade<18:
    print("Você é um adolescente!")
elif idade>=18 and idade<=65:
    print("Você é um adulto")
elif idade>65 and idade<=120:
    print("Você é um idoso")
else:
    print("idade inválida")
    
#ex06
idade=int(input("Digite sua idade:"))
if idade>0 and idade<=2:
    print("bebê")
elif idade >2 and idade <=12:
    print("Criança")
elif idade>12 and idade <=18:
    print('Adolescente')
elif idade >18 and idade<=65:
    print("adulto")
elif idade>65 and idade <120:
    print("idoso")
else:
    print("idade invalida")
  
#exercício01
nota1=float(input("Digite sua nota 1:"))
nota2=float(input("Digite sua nota 2:"))
nota3=float(input("Digite sua nota 3:"))
med=round((nota1+nota2+nota3)/3,3)
print(f"sua nota é {med}")
if med<=7 and med>0:
    print("então você está REPROVADO")
elif med>=7 and med>10:
    print("então você está APROVADO")
else:
    print("valores inválidos")
#exercício02
n1=int(input("Digite um número:"))
n2=int(input("Digite outro número:"))
c=int(input("Digite 1 para ação e 2 para subtração:"))
if c==1:
    soma=n1+n2
    print(f"A sua adição deu o resultado {soma}")
elif c==2:
    soma=n1-n2
    print(f"A sua subtração deu o resultado {soma}")
else: 
    print("Valor inválido")

#exercício03
sal=float(input("Digite o valor atual do seu salário:"))
if  sal<=300:
    print(f"Seu salário é {sal} e receberá um aumento de 35% ficando:", round(sal*1.35,2))
elif sal>300:
    print(f"Seu salário é {sal} e receberá um aumento de 15% ficando:R$", round(sal*1.15,2))
else:
    print("Opção inválida")

#exercício04
nome=str(input("Digite seu nome:"))
ini= nome[0].lower()
vogal=['a','e','i','o','u']
if ini in vogal:
    print(f"Seu nome começa com {ini} e é uma Vogal. ")

else:
    print(f"Seu nome começa com {ini} e é uma consoante.")

#exercício05
valor=float(input())