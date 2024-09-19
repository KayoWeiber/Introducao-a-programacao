
#ex01
idade=int(input("Digite sua idade:"))
if idade>0:
    if idade<18:
        print(f"Você possui {idade} anos e é menor de idade")
    else:
       print(f"Você possui {idade} anos e é maior de idade") 
else:
    print(f"Idade inválida")

#ex02
num1=int(input("Digite um número:"))
num2=int(input("Digite outro número:"))
if num1>num2:
    print(f"o número {num1} é maior que o número {num2}")
else:
    print(f"o número {num2} é maior que o número {num1}")

#ex03
num=int(input("Digite um número:"))
if num%2==0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")

#ex04
num1=int(input("Digite um número1:"))
num2=int(input("Digite um número2:"))
num3=int(input("Digite um número3:"))
if num1<num2 and num1<num3:
    print(f"O número {num1} é o menor número digitado!")
elif num2<num1 and num2<num3:
    print(f"O número {num2} é o menor número digitado!")
else:
    print(f"O número {num3} é o menor número digitado!")

#ex05
import datetime
hora = datetime.datetime.now().hour
#hora=13
nome=str(input("Digite seu nome:"))
if hora>=12 and hora<18:
    print(f"Olá {nome}, boa tarde!")
elif hora>=6 and hora<12:
    print(f"Olá {nome}, bom dia!")
else:
    print(f"Olá {nome}, boa noite!")
    
#ex06
nota=float(input("Digite sua nota:"))
while nota>10 or nota<0:
        print("Nota Inválida")
        nota=float(input("Digite sua nota:"))
if nota<=5:
    print(f"A nota {nota} é considerada regular")
elif nota>5 and nota<8:
    print(f"A nota {nota} é considerada BOA")
else:
    print(f"A nota {nota} é considerada EXCELENTE")

#ex07
sal=float(input("Digite seu salário BRUTO:"))
inss=sal*0.11
liq=sal-inss
print(f"O desconto do INSS é de R${round(inss,2)} e seu salário líquido é de R${round(liq,2)}")

#ex08
while True:
    try:
        num=int(input("Digite um número inteiro:"))
        break
    except ValueError:
        print("Valor Inválido")
if num>0:
    print(f"o número {num} é um número positivo")
elif num<0:
    print(f"o número {num} é um número negativo")
else:
    print(f"o número digitado é {num}")

#ex09
num=int(input('Digite um número:'))
if num%5==0 and num%7==0:
    print(f"O número {num} é multiplo de 5 e 7")
elif num%5==0:
    print(f"O número {num} é multiplo de 5")
elif num%7==0:
    print(f"O número {num} é multiplo de 7")
else:
    print(f"O número {num} não é multiplo de 5 e 7")

#ex10
while True:
    try:
        idade=int(input("Digite sua idade:"))
        if idade<0:
            print("Idade inválida")
        else:
            break   
    except ValueError:
        print("Idade inválida")
if idade<=12:
    print(f"Você possui {idade} anos e está na faixa etária considerada como CRIANÇA")
elif idade>=13 and idade<=17:
     print(f"Você possui {idade} anos e está na faixa etária considerada como ADOLESCENTE")
elif idade>=18 and idade<=29:
     print(f"Você possui {idade} anos e está na faixa etária considerada como ADULTO JOVEM")
elif idade>=30 and idade<=59:
     print(f"Você possui {idade} anos e está na faixa etária considerada como ADULTO")
else:
     print(f"Você possui {idade} anos e está na faixa etária considerada como IDOSO")


#ex11
while True:
    try:
        num=float(input("Digite a nota:"))
        num2=float(input("Digite a nota2:"))
        if num<0 or num2<0:
            print("Nota Inválida")
        else:
            break
    except ValueError:
        print("Nota Inválida")
media=(num+num2)/2
if media>6:
    print(f"O aluno com a média {media} está APROVADO")
else:
       print(f"O aluno com a média {media} está REPROVADO")  
       
#ex12
while True:
    try:
        nome=str(input("Digite seu nome:"))
        idade=int(input("Digite sua idade:"))
        if idade<0:
            print("idade inválida")
        else:
            break
    except ValueError:
        print("Dados inválidos")
if idade>18:
    print(f"{nome} que possui {idade} anos PODE DIRIGIR")
else:
    print(f"{nome} que possui {idade} anos NÃO PODE DIRIGIR")  


#ex13
letra=input("Digite uma letra:").lower()
if len(letra)==1:
    if letra in ["a","e","i","o","u"]:
        print(f"A letra {letra} é vogal")
    else:
        print(f"A letra {letra} é consoante")
else:
    print("Digite apenas letra")

#ex14
while True:
    try:
        lado1 = float(input("Digite o valor do lado 1 do triângulo:"))
        lado2 = float(input("Digite o valor do lado 2 do triângulo:"))
        lado3 = float(input("Digite o valor do lado 3 do triângulo:"))
        if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
            break
        else:
            print("Os valores fornecidos não podem formar um triângulo.")
    except ValueError:
        print("Valor inválido(digite um número).")
if lado1==lado2 and lado3==lado1 and lado3==lado2:
    print(f"O triângulo informado é equilátero")
elif lado1==lado2 or lado3==lado1 or lado3==lado2:
     print(f"O triângulo informado é isósceles")
else:
    print(f"O triângulo informado é escaleno")

#ex15
while True:
    try:
        num = int(input("Digite um número:"))
        break
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
if num <= 1:
    print(f"O número {num} não é primo")
else:
    primo=True
    if num==2 or num==3 or num==5 or num==7:
        primo = True
    elif num%2==0 or num%3==0 or num%5==0 or num%7==0:
        primo = False
    else:
        for i in range(2, int(num ** 0.5) + 1): #int(num ** 0.5) verifica a raiz
            if num%i==0:
                primo = False
                break
    if primo:
        print(f"O número {num} é primo")
    else:
        print(f"O número {num} não é primo")

#ex16
while True:
    try:
        peso=float(input("Digite seu peso:"))
        altura=float(input("Digite sua altura:"))
        break
    except ValueError:
        print("Valor inválido")
imc=round(peso/(altura**2),2)
if imc<18.5:
    print(f"O IMC apresentado foi igual a {imc} e está ABAIXO DO PESO")
elif imc>=18.5 and imc<=24.9:
    print(f"O IMC apresentado foi igual a {imc} e está PESO NORMAL")
elif imc>24.9 and imc<=29.9:
    print(f"O IMC apresentado foi igual a {imc} e está SOBREPESO")
elif imc>29.9 and imc<=34.9:
    print(f"O IMC apresentado foi igual a {imc} e está OBESIDADE GRAU 1")
elif imc>34.9 and imc<=39.9:
    print(f"O IMC apresentado foi igual a {imc} e está OBESIDADE GRAU 2")
else:
    print(f"O IMC apresentado foi igual a {imc} e está OBESIDADE GRAU 3")       
                
#ex17
hr = input("Digite uma hora (no formato HH:MM):")
min = hr.split(":")
if len(min) == 2:
    horas = int(min[0])
    minutos = int(min[1])
    if 0 <= horas <= 23 and 0 <= minutos <= 59:
        if horas>=0 and horas<=5:
            print("Boa madrugada")
        elif horas>=6 and horas<=11:
            print("Bom dia")
        elif horas>=12 and horas<=17:
            print('Boa tarde')
        else:
            print("Boa noite")
    else:
        print("Hora inválida.")
else:
    print("Formato de hora inválido. Por favor, insira a hora no formato HH:MM")

#ex18
while True:
    try:
        num=int(input("Digite um numero:"))
        if num<0:
            print("O número digitado é inválido.")
        else:
            break
    except ValueError:
         print("O número digitado é inválido.")
print(f"Tabuada do número {num}")
for i in range(0,11):
    tab=num*i
    print(f"{num} x {i} = {tab}")
    

#ex19
while True:
    try:
        num=input('Digite um número:')
        break
    except ValueError:
        print("O número não é válido")
if num == num[::-1]:
    print(f"{num} é um palíndromo.")
else:
    print(f"{num} não é um palíndromo.")
 
#ex20
while True:
    try:
        idade=int(input("Digite sua idade:"))
        if idade<0:
            print("Idade INVÁLIDA")
        else:
            break
    except ValueError:
        print("Idade INVÁLIDA")
if idade>16:
    print(f"{idade} anos pode votar")
else:
    print(f"{idade} anos não pode votar")




