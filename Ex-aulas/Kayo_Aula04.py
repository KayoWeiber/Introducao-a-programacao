#ex01-Operações
n1=int(input("digite um número "))
n2=int(input("digite outro número "))
adi=n1+n2
sub=n1-n2
mul=n1*n2
div=round(n1/n2,2)
print(f"O número 1 é {n1} e o número 2 é {n2} e a soma é {adi}")
print(f"O número 1 é {n1} e o número 2 é {n2} e a subtração é {sub}")
print(f"O número 1 é {n1} e o núemro 2 é {n2} e a multiplicação será {mul} ")
print(f"O núemro 1 é {n1} e o núemro 2 é {n2} e a divisão será {div}")

#ex02-Conversor de Temperatura
temp=int(input("digite a temperatura em Celsius "))
soma= (temp*1.8)+32
print(f"a temperatura em fahrenheit é {soma}")

#ex03-Calculadora de IMC
kg=float(input("digite o seu peso em KG "))
alt=float(input("digite sua altura "))
soma=round(kg/(alt*alt),2)
print(f"Seu IMC será {soma}")

#ex04-Cálculo da Média
n1=float(input("digite sua nota 1 "))
n2=float(input("digite sua nota 2 "))
n3=float(input("digite sua nota 3 "))
n4=float(input("digite sua nota 4 "))
soma=(n1+n2+n3+n4)/4
print(f"Sua nota média é {soma}")

#ex05-Conversor de moeda
dol = float(input("Digite o valor em dólar americano: "))
soma = round(dol * 5.05,2)
print(f'O valor em Real será R${soma}')

#ex06-Dividindo a pizza
val=float(input("Qual valor da pizza?"))
pes=int(input("Quantas pessoas irão dividir para pagar?"))
soma=val/pes
print(f"O valor a pagar para cada pessoa é {soma}")

#ex07-Cálculo da Soma
n1=int(input('Digite o número 1:'))
n2=int(input('Digite o número 2:'))
n3=int(input('Digite o número 3'))
n4=int(input('Digite o número 4'))
n5=int(input('Digite o número 5'))
soma= n1+n2+n3+n4+n5
print(f'A soma desses 5 números é {soma}')

#ex08-Calculadora
num = int(input('Digite um número: '))
x1 = num * 1
x2 = num * 2
x3 = num * 3
x4 = num * 4
x5 = num * 5
x6 = num * 6
x7 = num * 7
x8 = num * 8
x9 = num * 9
x10 = num * 10
print(f'A tabuada do número {num} é:\n{num} x 1 = {x1}\n{num} x 2 = {x2}\n{num} x 3 = {x3}\n{num} x 4 = {x4}\n{num} x 5 = {x5}\n{num} x 6 = {x6}\n{num} x 7 = {x7}\n{num} x 8 = {x8}\n{num} x 9 = {x9}\n{num} x 10 = {x10}')

#ex09-Nome e Idade
from datetime import date
nome=input('Qual seu nome?')
data=int(input('Qual o ano do seu nascimento?'))
date=date.today().year
soma=date-data
print(f'Seu nome é {nome} e você possui {soma} anos')

#ex10-Carro e média de consumo
car=input('Qual modelo do seu carro?')
con=int(input('Com quantos litros de etanol seu carro faz 1km?'))
val=float(input('Qual valor do etanol?'))
cal=round((650/con)*val, 2)
print(f'O seu veículo do modelo {car} gastará R${cal} em viagem de 650km ')