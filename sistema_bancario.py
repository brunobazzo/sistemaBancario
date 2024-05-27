menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar usuario
[b] Consultar usuario
[a] Criar conta
[q] Sair

=> """

# nome, data de nascimento, cpf, endereco
usuarios = []
# numero, cpf, agencia, saldo, extrato, numero de saques, limite
contas = []
LIMITE_SAQUES = 3

def padroniza_cpf(cpf):
    return int(cpf.replace(".","").replace("-",""))

def criar_conta(cpf):
    global usuarios
    global contas
    
    cpf = padroniza_cpf(cpf)

    for usuario in usuarios:
        print (usuario[0])
        if usuario[0] == cpf:
            agencia = "0001"
            contas.append([f"{len(contas)+1:03d}", cpf, agencia, 0,[],0,500])
            break

    print (contas)


def consultar_cadastro_usuario(cpf):

    global usuarios

    cpf = padroniza_cpf(cpf)
    
    for usuario in usuarios:
        if usuario[0] == cpf:
            print(f"usuario ja cadastrado {usuario}")
            return True

    print(f"usuario nao cadastrado")
    return False



def cadastrar_usuario(cpf):
    global usuarios

    cpf = padroniza_cpf(cpf)

    nome = input("Digite nome: ")
    cidade = input("Digite a cidade: ")

    usuarios.append([cpf, nome, cidade])

    print(usuarios)

def depositar(valor_deposito,numero_conta):
    global contas

    for conta in contas:
        if conta[0] == numero_conta:
            if valor_deposito <= 0:
                print(f"voce nao pode depositar o valor {valor_deposito}")
                break
            else:
                print(f"vai depositar")
                conta[3] += int(valor_deposito)
                conta[4].append("+R$"+str(valor_deposito))
                break
     
    print(contas)


def sacar(valor_saque,numero_conta):

    global contas

    for conta in contas:
        if conta[0] == numero_conta:


            if conta[5] == LIMITE_SAQUES:
                print(f"voce atingiu o numero de saques diario maximo de {LIMITE_SAQUES}")
            elif valor_saque > conta[6]:
                print(f"voce nao pode sacar o valor {valor_saque} pois é maior que limite{conta[6]}")
            elif valor_saque > conta[3]:
                print(f"voce nao pode sacar o valor {valor_saque} pois é maior que saldo {conta[3]}")
            else:
                conta[5] += 1
                conta[3] -= valor_saque
                conta[4].append("-R$"+str(valor_saque))
                break


def extrato(conta):
    global contas

    for conta in contas:
        if conta[0] == numero_conta:
            if conta[4]:
                print(f"extrato: {conta[4]}")
            else:
                print(f"Nao foram realizadas movimentações")
            print(f"seu saldo é de R$: {conta[3]:.2f}")
            break



while True:

    opcao = input(menu)

    if opcao == "d":
        numero_conta = str(input("Digite o número da conta: "))
        valor_deposito = input("Digite o valor de deposito: ")
        depositar(int(valor_deposito),numero_conta)


    elif opcao == "s":
        numero_conta = str(input("Digite o número da conta: "))
        valor_saque = input("Digite o valor do saque: ")
        sacar(numero_conta=numero_conta, valor_saque=int(valor_saque))

    elif opcao == "c":
        cpf = input("Digite o CPF: ")
        if consultar_cadastro_usuario(cpf) == False:
            cadastrar_usuario(cpf)
    elif opcao == "b":
        cpf = input("Digite o CPF: ")
        consultar_cadastro_usuario(cpf)

    elif opcao == "a":
        cpf = input("Digite o CPF: ")
        criar_conta(cpf)

    elif opcao == "e":
        numero_conta = str(input("Digite o número da conta: "))
        extrato(conta=numero_conta)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



    
