
#exercício01
nota1=float(input("Digite sua nota 1:"))
nota2=float(input("Digite sua nota 2:"))
nota3=float(input("Digite sua nota 3:"))
med=round((nota1+nota2+nota3)/3,3)
print(f"sua média é {med}")
if 0 <= med <= 10:
    if med >= 7:
        print("Você está APROVADO")
    else:
        print("Você está REPROVADO")
else:
    print("Valores inválidos para as notas. Por favor, verifique se as notas estão entre 0 e 10.")

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
if sal>0 and sal<=300:
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
val=int(input("Digite um valor inteiro:"))
if val >0 and val <=9:
  print(f"O valor {val} está na faixa permitida")
else:
  print(f"O valor {val} está fora da faixa permitida")

#exercício06
nome=str(input("Digite seu nome:"))
sexo=str(input("Digite seu sexo, M para masculino e F para feminino:")).lower()
if sexo=="m"or sexo=="f":
  if sexo=="m":
    print(f"Ilmo sr. {nome}")
  else:
    print(f"Ilmo sra. {nome}")
else:
  print("informação inválida")
  #poderia usar o elif

#exercício07
num=int(input("Digite um número:"))
a=0
b=0
if num >0:
  a=0+num
else:
  b=0+num
print(f"O valor da váriavel A: {a} ")
print(f"O valor da váriavel B: {b} ")

#exercício08
alt=float(input("Digite sua altura:"))
sexo=str(input("Digite seu sexo, M para masculino e F para feminino:")).lower()
if sexo=="m" or sexo=="f":
  if sexo=="m":
    imc=round((72.7*alt)-58,2)
    print(f'O seu peso ideal é {imc} kg')
  else:
    imc=round((62.1*alt)-44.7,2)
    print(f'O seu peso ideal é {imc} kg')
else:
  print("Sexo inválido")

#exercício09
nota1=float(input("Digite sua nota 1:"))
nota2=float(input("Digte sua nota 2:"))
nota3=float(input("Digte sua nota 3:"))
nota4=float(input("Digte sua nota 4:"))
media=round((nota1+nota2+nota3+nota4)/4,2)
if (0 <= nota1 <= 10) and (0 <= nota2 <= 10) and (0 <= nota3 <= 10) and (0 <= nota4 <= 10):
  if media>5:
    print(f"Sua média é {media} e está aprovado! ")
  elif media >=3 and media<=5:
     print(f"Sua média é {media} e está de recuperação! ")
  else:
      print(f"Sua média é {media} e está reprovado! ")
else:
  print("Valores inválido, tente novamente!")

#exercício10
nota1=float(input("Digite sua nota 1:"))
nota2=float(input("Digite sua nota 2:"))
nota3=float(input("Digite sua nota 3:"))
nota4=float(input("Digite sua nota 4:"))
media=round((nota1+nota2+nota3+nota4)/4,2)
if (0 <= nota1 <= 10) and (0 <= nota2 <= 10) and (0 <= nota3 <= 10) and (0 <= nota4 <= 10):
  if media >= 7:
    print("O aluno está aprovado com média.")
  else:
    exame=float(input("Digite sua nota do exame:"))
    novamed=round((media+exame)/2,2)
    if novamed >=5:
      print("O aluno foi aprovado na recuperação com média.")
    else:
      print("O aluno não foi aprovado na recuperação com média.")
else:
  print("Valores inválido, tente novamente!")