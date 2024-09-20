#ex01
n = int(input("Digite um número (-999 para sair): "))
while n != -999:
    n3 = n * 3
    print(f"O triplo de {n} é: {n3}")
    n = int(input("Insira outro número (-999 para sair): "))
   
#ex02
for i in range(1,101,1):
    print(i)
     
#ex03
for i in range(100, 0, -1):
    print(i)
  
#ex04
cont=0
num=float(input("Digite um número positivo(e negativo para sair):"))
while num >0 :
    cont+=1
    num=float(input("Digite um número positivo(e negativo para sair):"))
print(f"A quantidade de números digitados foi {cont}")

  #ex05
cont=0
soma=0
num=float(input("Digite um número positivo(número negativo para realizar a média):"))
while num>0:
    cont+=1
    soma+=num
    num=float(input("Digite um número positivo(número negativo para realizar a média):"))
    
if cont >0:
    med=soma/cont
    print(f"A média dos números é ",round(med,2))
else:
    print("Nenhum valor positivo foi digitado")
   
#ex06
for i in range(1,600,1):
    if i%2==0:
        print(i)
   
#ex07
cont=0
while True:
    num=int(input("Digite um número entre 100 e 200:"))
    if num==0:
        break
    elif num<200 and num>100:
        cont+=1
        print(f"Foram digitados {cont} entre 100 e 200 (digite 0 para encerrar programa).")
    else:
       print(f"O número {num} não está entre 100 e 200 (digite 0 para encerrar programa).")
print(f"O total de números digitados foi {cont}")


#ex08
cont=0
while True:
    prof=(str(input("Digite sua profissão:"))).lower()
    if prof=="dentista" or prof=="destinta":
        cont+=1
        print(f"{cont} são dentistas(digite Fim para finalizar programa).")
    elif prof=="fim":
        break
    else:
        print(f"{cont} são dentistas(digite Fim para finalizar programa).")
print(f"{cont} é quantidade total de dentistas.")
         
    
#ex09
anos=0
chico=1.50
juca=1.10
while juca<=chico:
    anos+=1
    juca+=0.03
    chico+=0.02
print(f"Juca precisará de {anos} anos para ultrapassar a altura de Chico.")
    
    
#ex10
tn=10
for i in range(tn):
    num=int(input(f"Digite o número {i+1} :"))
    quadr=round(num**2,2)
    met=round(num/2,2)
    print(f"O numero {num} possui o quadrado {quadr} e a metade {met}.")

#ex11
pol = 2.54
print("Tabela de conversão de polegadas para centímetros")
print("Polegadas   |   Centímetros")
for polegadas in range(1, 21):
    centimetros = polegadas * pol
    print(f"{polegadas} polegadas é igual a {round(centimetros,2)} centímetros")


 #ex12 
cont=0
while cont<10:
    cont+=1
    pes1=str(input(f"Digite seu nome{cont}:"))
    pes2=int(input("Digite sua idade:"))
    pes3=str(input("Digite seu sexo(M para masculino e F para feminino):")).lower()
    if pes3=="m" or pes3=="f":
         if pes3=="m" and pes2>21:
             print(f"{pes1} é do sexo masculino e tem {pes2} anos")
    else:
        print("Sexo inválido")
    
         
#ex13
sum=0
for i in range(25,201,1):
    if i%2==0:
       sum+=i
print(f"{sum}")
        
#ex14
import math
for i in range(1,11):
    num=int(input(f"Digite um número{i}:"))
    if num<0:
        print("Número inválido")
    else:
        raiz=math.sqrt(num)
        print(f"A raiz quadrada de {num} é {round(raiz,2)}")

#ex15
num=int(input("Digite um número:"))
sum=0
if num>0:
    for i in range(1,num):
        if num%5==0:
          sum+=i
    print(f"A soma dos números múltiplos de 5 é {sum}")
else:
    print("Número inválido")
   