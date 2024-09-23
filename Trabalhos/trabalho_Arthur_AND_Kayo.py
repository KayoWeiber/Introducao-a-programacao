#ex01
cont=0
valores=[]
for i in range(5):
    cont+=1
    valor=float(input(f"Digite o valor inteiro{cont}:"))
    valores.append(valor)
media=sum(valores)/len(valores)
print(f"A Média é {media} e os valores maiores que ela é:")
for valor in valores:
    if valor>media:
        print(valor)

#ex02
alt=float(input("Digite sua altura:"))
peso=float(input("Digite seu peso:"))
imc=round(peso/(alt**2),2)
if imc<18.5:
    print(f"o imc valor do IMC é {imc} e está ABAIXO DO PESO")
elif imc>=18.5 and imc<=24.9:
    print(f"o imc valor do IMC é {imc} e está PESO NORMAL")
elif imc>=25 and imc<=29.9:
    print(f"o imc valor do IMC é {imc} e está SOBREPESO")
elif imc>=30 and imc<=34.9:
    print(f"o imc valor do IMC é {imc} e está OBESIDADE GRAU 1")
elif imc>=35 and imc<=39.9:
    print(f"o imc valor do IMC é {imc} e está OBESIDADE GRAU 2")
else:
    print(f"o imc valor do IMC é {imc} e está OBESIDADE GRAU 3")

#Ex3
rs1=0
rs=0
for dia in range (1,8):
    p=float(input(f"Digite o peso do peixe no dia {dia}:"))
    if p>50:
        p1=p-50
        multa=p1*4
        rs+=(p*30)-multa
        print(f"No dia {dia}, a multa vai ser {multa}")   
    else:
        rs1+=(p*30)
        print(f"Dia {dia} não teve multa")
rs2=rs+rs1
print(f"O rendimento semanal foi de {rs2}")   
   
#ex04
nota1=float(input("Digite a nota do trabalho 1:"))
nota2=float(input("Digite a nota do trabalho 2:"))
prova=float(input("Digite o valor da prova:"))
soma=round(nota1+nota2+prova,2)
while nota1<0 or nota1>30:
    print("VALOR DO TRABALHO 1 INVÁLIDO")
    nota1=float(input("Digite a nota do trabalho 1:"))
    nota2=float(input("Digite a nota do trabalho 2:"))
    prova=float(input("Digite o valor da prova:"))
    soma=round(nota1+nota2+prova,2)
while nota2<0 or nota2>30:
    print("VALOR DO TRABALHO 1 INVÁLIDO")
    nota1=float(input("Digite a nota do trabalho 1:"))
    nota2=float(input("Digite a nota do trabalho 2:"))
    prova=float(input("Digite o valor da prova:"))
    soma=round(nota1+nota2+prova,2)
while prova<0 or prova>40:
    print("VALOR DA PROVA INVÁLIDO")
    nota1=float(input("Digite a nota do trabalho 1:"))
    nota2=float(input("Digite a nota do trabalho 2:"))
    prova=float(input("Digite o valor da prova:"))
    soma=round(nota1+nota2+prova,2)
if soma >=60:
    print(f"O aluno está APROVADO com {soma} pontos")
elif soma >=40 and soma<=59.99:
    print("O aluno está DEPENDÊNCIA e tem direito de fazer outra prova.")
    nprova=float(input("Digite o valor da prova de substituta:"))
    if nprova<0 or nprova>100:

        print("VALOR DA PROVA INVÁLIDO")
    elif nprova>=60:
        print(f"O aluno está APROVADO com {nprova} pontos")
    else:
        print(f"O aluno está REPROVADO com {nprova} pontos")
else:
    print(f"O aluno está REPROVADO com {soma} pontos") 

#ex05
import datetime
ano = datetime.datetime.now().year
nome=str(input("Digite seu nome:"))
sal=float(input("Digite seu salário atual:"))
nasc=int(input("Digite o ano de nascimento:"))
ingr=int(input("Digite o ano que ingressou na empresa:"))

idade=ano-nasc
temp=ano-ingr

if nasc>ano or ingr>ano:
    print("Data inválida")
else:
    if temp>10 and idade>40:
        nsal=sal*1.20
        print(f"O funcionário {nome} receberá 20% de aumento e novo salário será R$ {round(nsal,3)}")
    else:
        nsal=sal*1.10
        print(f"O funcionário {nome} receberá 10% de aumento e novo salário será R$ {round(nsal,3)}")