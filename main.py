import textwrap
from conta_corrente import ContaCorrente
from deposito import Deposito
from pessoa_fisica import PessoaFisica
from saque import Saque


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Ciar cliente
[ls] Consultar contas
[a] Criar conta
[q] Sair

=> """
clientes = []
contas = []


def exibir_extrato(clientes):
    cpf = input("Digite o CPF do cliente:")

    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("EXTRATO") 
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        print("Cliente nao tem movimentacao na conta.") 
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tRS{transacao['valor']:.2f}"

        print(extrato)
        print(f"\nSaldo:\n\tRS {conta.saldo:2f}")
        print("FIM")

def sacar(clientes):
    cpf = input("Digite o CPF do cliente:")

    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        return
    
    valor = float(input("informe o valor de saque: "))

    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta,transacao)



def depositar(clientes):
    cpf = input("Digite o CPF do cliente:")

    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        return
    
    valor = float(input("informe o valor do deposito: "))

    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta,transacao)

def filtrar_cliente(cpf,clientes):


    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    
    print("Cliente nao encontrado")        
    return None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("cliente nao tem conta")
        return
    
    return cliente.contas[0]

def criar_conta(clientes,contas):

    cpf = input("Digite o CPF do cliente:")

    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        return

    conta = ContaCorrente.nova_conta(cliente=cliente,numero=len(contas) + 1)
    contas.append(conta)
    cliente.contas.append(conta)

def listar_contas(contas):

    for conta in contas:
        print("========================")
        print(textwrap.dedent(str(conta)))


def criar_cliente(clientes):

    cpf = input("Digite o CPF do cliente:")

    cliente = filtrar_cliente(cpf,clientes)

    if cliente:
        print("Cliente ja cadastrado")
        return
    
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o enderaço: ")

    cliente = PessoaFisica(cpf,nome,data_nascimento,endereco)

    clientes.append(cliente)



while True:

    opcao = input(menu)

    if opcao == "d":
        depositar(clientes)


    elif opcao == "s":
        sacar(clientes)

    elif opcao == "c":
        criar_cliente(clientes)

    elif opcao == "a":
        criar_conta(clientes,contas)
        pass

    elif opcao == "e":
        exibir_extrato(clientes)

    elif opcao == "ls":
        listar_contas(contas)
        
    elif opcao == "ls":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")





    
