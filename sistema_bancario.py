menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500
extrato_list = []

numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor_deposito):
    global saldo, extratextrato_listo
    if valor_deposito <= 0:
        print(f"voce nao pode depositar o valor {valor_deposito}")
    else:
        saldo += valor_deposito
        extrato_list.append("R$"+str(valor_deposito))

def sacar(valor_saque):
    global saldo, numero_saques, extrato_list
    if numero_saques == LIMITE_SAQUES:
        print(f"voce atingiu o numero de saques diario maximo de {LIMITE_SAQUES}")
    elif valor_saque > limite:
        print(f"voce nao pode sacar o valor {valor_saque} pois é maior que limite{limite}")
    elif valor_saque > saldo:
        print(f"voce nao pode sacar o valor {valor_saque} pois é maior que saldo {saldo}")
    else:
        numero_saques += 1
        saldo -= valor_saque
        extrato_list.append("-R$"+str(valor_saque))


def extrato():
    global saldo
    if extrato_list:
        print(f"extrato: {extrato_list}")
    else:
        print(f"Nao foram realizadas movimentações")
    print(f"seu saldo é de R$: {saldo:.2f}")



while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = input("Digite o valor de deposito: ")
        depositar(int(valor_deposito))


    elif opcao == "s":
        valor_saque = input("Digite o valor do saque: ")
        sacar(int(valor_saque))


    elif opcao == "e":
        extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



    
