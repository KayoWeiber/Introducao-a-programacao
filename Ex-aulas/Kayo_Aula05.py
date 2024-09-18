

#ex01
n1=int(input("digite um número:"))
n2=int(input("digite um número:"))
n3=int(input("digite um número:"))
n4=int(input("digite um número:"))
soma=n1+n2+n3+n4
print(f"A soma dos núemro apresentados é {soma}")

#ex02
nome1=str(input("Digite seu nome:"))
nasc1=str(input("Digite sua data de nascimento:"))
nome2=str(input("Digite o nome de outra pessoa:"))
nasc2=str(input("Digite a data de nascimento dessa pessoa:"))
nome3=str(input("Digite outro nome de uma pessoa:"))
nasc3=str(input("Digite a data de nascimento:"))
print(f"A data de nascimento da primeira é {nasc1} e seu nome é {nome1}.\nA data de nascimento da segunda pessoa é {nasc2} e seu nome é {nome2}.\nA data de nascimento da terceira pessoa é {nasc3} e seu nome é {nome3}.")

#ex03
let1=str(input('Digite uma letra:'))
let2=str(input('Digite mais uma letra:'))
let3=str( input('digite outra letra:'))
print(f'A ultima letra lida foi "{let3}"\nA penúltima letra lida foi"{let2}"\nE a primeira letra lida foi "{let1}"')

#ex04
r=float(input("Digite o raio da esfera:"))
pi=3.14159
c=round(2*pi*r,4)
a=round(pi*r**2,4)
v=round((4/3)* pi * r**3, 4)
print(f"O Comprimento da esfera é {c}")
print(f"A área da esfera é {a} ")
print(f"O volume da esfera é {v}")

#ex05
v1=int(input("Digite o ângulo de um triângulo:"))
v2=int(input("Digite o segundo ângulo do triângulo:"))
v3=180-v1-v2
print(f"Sabendo que um triângulo possui três ângulos internos totalizando  180º, então o terceiro ângulo seria {v3}º")

#ex06
num=int(input("Digite um número para ser mostrado a tabuada:"))
x1=num*1
x2=num*2
x3=num*3
x4=num*4
x5=num*5
x6=num*6
x7=num*7
x8=num*8
x9=num*9
x10=num*10
print(f"{num}x1={x1}\n{num}x2={x2}\n{num}x3={x3}\n{num}x4={x4}\n{num}x5={x5}\n{num}x6={x6}\n{num}x7={x7}\n{num}x8={x8}\n{num}x9={x9}\n{num}x10={x10}")

#ex07
c=float(input("Digite a temperatura em celsius:"))
f=180*(c+32)/100
print(f"A temperatura em Farenheit é {f}°F")

#ex08
us=int(input("Digite o valor de medida em pés:"))
p=us*12
j=us/3
m=round(us/1760,4)
print(f"Os valores dessas medidas em polegadas é {p}, em jardas é {j} e em milhas é {m}")

#ex09
h=int(input("Digite o valor das horas:"))
m=int(input("Digite o valor de minutos:"))
segtotal=(h*3600)+(m*60)
meian=86400-segtotal
print(f"Segundos desde a meia-noite: {segtotal} segundos")
print(f"Segundos restantes até a próxima meia-noite: {meian} segundos")

#ex10
sal=float(input("Digite o valor do seu salário:"))
soma=round(sal*0.30,2)
print(f"O valor máximo das prestações a serem pagas será R${soma}")