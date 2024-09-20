#ex01
num=int(input("Digite um número:"))
while num>=0:
    if num<5:
        print(f"O número {num} é menor que 5.")
    elif num>5:
        print(f"O número {num} é maior que 5.")
    else:
        print(f"O número é igual a 5")
    num=int(input("Digite um número(digite um número negativo para encerrar.):"))
print("Programa finalizado")

#ex02
idade=int(input("Digite sua idade:"))
pes1=0
pes2=0
pes3=3
while idade >0<120:
    if idade<=18:
        print("menor de idade")
        pes1+=1
    elif idade<60:
        print("adulto")
        pes2+=1
    else:
        print("idoso")
        pes3+=1
    
    idade=int(input("Digite sua idade (idade menor que 0 e maior que 120 finaliza o progama):"))
print(f"A quantidade de pessoas informada menor de 18 anos foi {pes1}")
print(f"A quantidade de pessoas informada maior de 18 anos foi {pes2}")
print(f"A quantidade de pessoas informada menor de 60 anos foi {pes3}")
print("Programa finalizado")
 
#ex03
num=int(input("Digite um número:"))
maior=0
while num!=-100:
    if num>maior:
        maior=num
    num=int(input("Digite um número(digite -100 para finalizar):"))
print(f"O maior número digitado foi {maior}")
print(f"Programa finalizado")

#ex04
num=float(input("Digite um número real:"))
quant=0
med=0
while num!=0:
    quant+=1
    med+=num
    num=int(input("Digite um número real(digite número 0 para finalizar):"))
soma=med/quant
print(f"A média dos números digitado foi {round(soma,2)} ")
print(f"A quantidade de números digitados foi {quant}")

#ex05
num=int(input("Digite um número:"))
print(f"{'Impar':<10}{'par'}")
for i in range(1,num+1):
    if i%2==0:
        print(f"{i:<10}",end=' ')
       
    else:
         print(f"{i:<10}",end=' ')
    if i%2==0:
        print()

#ex06
num=int(input("Digite um número entre 12 e 20:"))
while True:
    if num>=12 and num<=20:
        print(f"o número digitado foi {num}")  
        break
    else:
        print("Número inválido")
        num=int(input("Digite novamente um número entre 12 e 20:"))

#ex07
def fibonacci_until_limit(limit):
    fib1 = 0
    fib2 = 1
    print(fib1, end=" ")
    while fib2 <= limit:
        print(fib2, end=" ")
        prox = fib1 + fib2
        fib1 = fib2
        fib2 = prox
    print()
    print(fib2)
limite = int(input("Digite um número:"))
if limite > 0:
    fibonacci_until_limit(limite)
else:
    print("Número inválido.")

#ex08
somar=0
par=0
num=int(input("Digite um número ímpar:"))
while True:
  if num%2==0:
    par+=num
    break
  else:
    somar+=num
    num=int(input("Digite um número ímpar(número par para finalizar):"))
res=somar/par
print(f"A Soma de todos os número impares é {somar} e divisão pelo número {par} é {res}")

#ex09
num=int(input("Digite um número:"))
res=0
while True:
  res+=num

  if res%7==0:
    print(f"O número {res} é divisível por 7")
    break
  else:
    print(f"A soma dos números é {res}(para finalizar faça com que o número seja divisivel por 7)")

#ex10
import random
ns=random.randint(1,100)
user=int(input("Adivinhe o número secreto:"))
tent=0
while True:
  tent+=1
  if user>100 or user>1:
    if user==ns:
      print(f"Você acertou em {tent} tentativas")
      break
    elif user>ns:
      print("O número secreto é menor")
      user=int(input("Adivinhe o número secreto:"))
    elif user<ns:
      print("O número secreto é maior")
      user=int(input("Adivinhe o número secreto:"))
  else:
    print("valor inválido")