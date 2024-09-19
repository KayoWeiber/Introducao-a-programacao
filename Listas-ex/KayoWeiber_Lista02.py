#Lista de Exercícios
'''
#ex01
func=0
while True:
    try:
        sal=float(input("Digite o valor bruto do Salário:(digite 0 para finalizar):"))
        func+=1
        if sal==0:
            print("Programa finalizado")
            break
        else:
            if sal<=1412:
                desc=sal*0.075
            elif sal<=2666.6:
                desc=sal*0.09
            elif sal<=4000.03:
                desc=sal*0.12
            else:
                desc=sal*0.14 
            if sal>=2112.01 and sal<=2826.65:
                desc2=sal*0.075
            elif sal>=2826.66 and sal<=3751.05:
                desc2=sal*0.225
            elif sal>=3751.06 and sal<=4664.68:
                desc2=sal*0.225
            elif sal>4664.68:
                desc2=sal*0.275
            else:
                desc2=0
        print(f"O salário líquido do funcionário {func} será R${round(sal-desc-desc2,2)}")                  
    except ValueError:
        print("VALOR INVÁLIDO")


#ex02
while True:
    try:
        cap=float(input("Digite o valor do capital inicial(Digite 0 para finalizar):"))

        if cap==0:
            print("Programa finalizado")
            break
        else:
            taxa=float(input("Digite o valor da taxa anual:"))
            anos=int(input("Digite a quantidade de anos:"))
            if taxa<0 or anos<0:
                print(f"Valor inválido os números precisa ser positivo.")
            else:
                for ano in range(1,anos +1):
                    valor=cap*(1+taxa/100)**ano
                    print(f"O valor acumulado final no ano {ano} será de R${round(valor,2)}")
    except ValueError:
        print("VALOR INVÁLIDO")
       
#ex03
cont=0
while True:
    try:
        horas=float(input("Digite a quantidade de horas trabalhadadas(digite 0 para finazlizar o programa):"))
        if horas==0:
            print("Programa finalizado")
            break
        else:
            if horas<0:
                print("Quantidade de horas inválida.")
            else:
                sal=float(input("Digite o valor do salário semanal do funcionário:"))
                cont+=1
                if horas>40:
                    cal=sal*1.50
                    print(f"O valor do salário do funcionário {cont} será de R${round(cal,2)}")
                else:
                    print(f"O valor do salário do funcionário {cont} será de R${round(sal,2)}")
    except ValueError:
        print("VALOR INVÁLIDO")
        
       
#ex04
cont=0
valortotal=0
while True:
    try:
        produ=input("Digite o valor do produto(digite fim para finalizar):").lower()
        if produ=="fim":
            print("Programa finalizado")
            break
        else:
            produ = produ.replace(',', '.')
            pre=float(produ)
            cont+=1
            valortotal+=pre
            print(f"produto {cont} custá R${pre} e a soma total é R${round(valortotal,2)}")
        
    except ValueError:
       print("VALOR INVÁLIDO")
       
 
  #ex05
estoque = {}

while True:
    produtos = input("Digite o nome do produto (ou 'sair' para finalizar): ").lower()
    
    if produtos == "sair":
        print("Programa finalizado.")
        break
    
    if produtos not in estoque:
        while True:
            try:
                saldoini = int(input(f"Digite a quantidade inicial para o produto {produtos}: "))
                if saldoini < 0:
                    print("Quantidade de produtos não pode ser negativa.")
                else:
                    estoque[produtos] = saldoini
                    break
            except ValueError:
                print("Entrada inválida. Insira um número inteiro para a quantidade.")
    else:
        while True:
            operacao = input("Digite 'adicionar' para adicionar produtos, 'remover' para remover produtos ou 'ver' para ver o estoque: ").lower()
            
            if operacao == "adicionar":
                try:
                    quant = int(input("Digite quantos produtos deseja adicionar ao estoque: "))
                    if quant < 0:
                        print("Quantidade de produtos não pode ser negativa.")
                    else:
                        estoque[produtos] += quant
                        print(f"{quant} unidades adicionadas ao estoque de {produtos}.")
                        break 
                except ValueError:
                    print("Entrada inválida. Insira um número inteiro para a quantidade.")
            
            elif operacao == "remover":
                try:
                    quant = int(input("Digite quantos produtos deseja remover do estoque: "))
                    if quant < 0:
                        print("Quantidade de produtos não pode ser negativa.")
                    elif quant > estoque[produtos]:
                        print(f"Não é possível remover {quant} unidades. O estoque atual de {produtos} é {estoque[produtos]}.")
                    else:
                        estoque[produtos] -= quant
                        print(f"{quant} unidades removidas do estoque de {produtos}.")
                        break 
                except ValueError:
                    print("Entrada inválida. Insira um número inteiro para a quantidade.")
            
            elif operacao == "ver":
                print(f"O estoque atual de {produtos} é {estoque[produtos]} unidades.")
                break
            
            else:
                print("Operação desconhecida. Por favor, insira 'adicionar', 'remover' ou 'ver'.")
    print("\nEstoque atualizado:")
    for item, qtd in estoque.items():
        print(f"{item.capitalize()}: {qtd} unidades")
    print() 

print("Controle de estoque fechado.")

 #ex06
cont=0
total=0
while True:
     try:
        produ=int(input("Digite a quantidade produzida no dia (Digite 0 para realizar média diária): "))
        if produ==0:
            print("Programa finalizado")
            soma=total/cont
            print(f"A quantidade de itens produzidos até o dia {cont} é de {total}")
            print(f"A média de produção diária é de {soma}")               
            break
        else:
            while True:
                    if produ<0:
                        print("O valor de produção não pode ser negativo, tente novamente.")
                        break
                    else:
                        total+=produ
                        cont+=1   
                        print(f"A quantidade de itens produzidos até o dia {cont} é {total}.")
                        break
     except ValueError:
        print("O valor fornecido precisa ser um número inteiro.")

 #ex07
cont=0
total=0
while True:
    try:
        vendas=input("Digite o valor da vendas (digite 'fim' para finalizar):").lower()
        if vendas=="fim":
            try:
                media=total/cont
                print("Programa finalizado.")
                print(f"O valor de vendas vendidas até o dia {cont} é de R${round(total,2)}.")
                print(f"A média de faturamento diário é de R${round(media,2)}")
                break
            except ZeroDivisionError:
                print("Insira dados.")
        else:
            try:
                vendas=vendas.replace(',','.')
                valor=float(vendas)
                if valor<0:
                    print("O valor da venda não é válido.")
                else:
                    total+=valor
                    cont+=1
                    print(f"O valor de vendas vendidas até o dia {cont} é de R${round(total,2)}.")                  
            except ValueError:
                print("O valor informado não é válido.")
    
    except ValueError:
        print("O valor fornecido precisa ser um número inteiro.")

 #ex08
cont=0
while True:
    try:
        valor=input("Digite o valor do produto (digite 0 para finalizar o programa):")
        valor=valor.replace(',','.')
        valores=float(valor)
        if valores==0:
            print("Programa finalizado.")
            break
        elif valores<0:
            print("O valor fornecido não é válido.")
        else:
                try:
                    desc=float(input("Digite em porcentagem o valor do desconto:"))
                    if desc<0:
                        print("O valor fornecido não é válido.")
                    else:
                        cont+=1
                        porc=((desc/100)*valores)
                        pagar=valores-porc
                        print(f"O produto {cont} com o valor R${round(valores,2)} dando um desconto de R${porc} ficará com o valor de R${round(pagar,2)}")
                except ValueError:
                    print("O desconto fornecido não é válido.")
    except ValueError:
        print("O valor fornecido não é válido.")
  
 #ex09
cont=0
total=0
while True:
    try:
        action=input("Digite o valor de entrada(número positivo) ou saída(número negativo). Digite 'fim' para finalizar:").lower()
        if action=="fim":
            print("Programa finalizado.")
            print(f"O caixa teve {cont} operações e o saldo final do caixa é de {round(total,2)}")
            break
        else:
            try:
                action=action.replace(",",".")
                valor=float(action)
                if valor<0:
                    cont+=1
                    total+=valor
                    print(f"A operação {cont} teve uma saída de {round(valor,2)} e o saldo atual é de R${round(total,2)}")
                
                elif valor>0:
                    cont+=1
                    total+=valor
                    print(f"A operação {cont} teve uma entrada de {round(valor,2)} e o saldo atual é de R${round(total,2)}")
                
                else:
                    print('O valor inserido não pode ser 0')
            except ValueError:
                print("O valor precisa ser um número.")
    except ValueError:
        print("Valor digitado não é válido.") 

#ex10
from datetime import datetime
while True:
    nome=str(input("Digite o nome do evento (Digite 'sair' para finalizar programa):")).lower()
    if nome=="sair":
        print("Programa finalizado")
        break
    else:
        try:
            data=input("insira a data no formato correto dd/mm/yyyy :")
            dia=datetime.strptime(data,"%d/%m/%Y")
            #print(f"Data válida:", dia.strftime("%d/%m/%Y"))
            try:
                pessoas=int(input("Digite a quantidade de participantes do evento:"))
                if pessoas<=0:
                    print("A quantidade de pessoas não pode ser 0 ou menor que 0.")
                else:
                    try:
                        custopp=input("Digite o custo fixo médio estimado por participante:")
                        custopp=custopp.replace(",",".")
                        custo=float(custopp)
                        if custo<=0:
                            print("O custo fixo não pode ser igual ou menor que 0")
                        else:
                            total=round(custo*pessoas,2)
                            print(f"o evento {nome} do dia {dia.strftime('%d/%m/%Y')} cujo a quantidade de participantes de {pessoas} com um custo fixo por pessoa de R${custo} terá um valor custo fixo de R${total}")
                    except ValueError:
                        print("O custo inserido não é válido.")
            except ValueError:
                print("A quantidade de participante precisa ser um número inteiro.")
        except ValueError:
            print("A data inserida não é válida")
  '''          
