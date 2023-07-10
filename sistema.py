contas = []
clientes = []
numero_conta = 1

def cadastrar_cliente(nome, cpf):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print("CPF já cadastrado.")
            return
    clientes.append({'nome': nome, 'cpf': cpf})
    print("Cliente cadastrado com sucesso!")

def criar_conta(cpf):
    global numero_conta
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            contas.append({'agencia': '0001', 'numero': numero_conta, 'cpf': cpf})
            numero_conta += 1
            print("Conta criada com sucesso!")
            return
    print("Cliente não encontrado.")

def depositar(valor):
    global saldo, extrato
    if valor <= 0:
        print("Valor inválido.")
        return
    saldo += valor
    extrato += f"\nDepósito realizado - R$ {valor:,.2f}"
    print(f"Seu depósito no valor de R$ {valor:,.2f} foi realizado!")

def sacar(*, valor):
    global saldo, extrato, saques_quantia
    if valor <= 0:
        print("Valor inválido.")
        return
    if valor > saldo:
        print("Seu saldo é insuficiente para realizar este saque.")
        return
    if valor > limite:
        print(f"Saque negado por ultrapassar o limite de R$ {limite:,.2f} por saque.")
        return
    if saques_quantia >= SAQUES_MAXIMO:
        print("Você atingiu seu limite diário de 3 saques, então não pode realizar mais saques.")
        return
    saldo -= valor
    saques_quantia += 1
    extrato += f"\nSaque realizado - R$ {valor:,.2f}"
    print(f"Seu saque no valor de R$ {valor:,.2f} foi realizado!")

def exibir_extrato(*args, **kwargs):
    global saldo, extrato
    for key, value in kwargs.items():
        extrato += f"\n{key}: {value}"
    if args:
        extrato += f"\nOutros argumentos posicionais: {args}"
    print(f"{extrato}\n\nSaldo atual - R$ {saldo:,.2f}")

def exibir_contas(cpf):
    cliente_encontrado = False
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            cliente_encontrado = True
            print(f"Contas do cliente {cliente['nome']} (CPF: {cpf}):")
            for conta in contas:
                if conta['cpf'] == cpf:
                    print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero']}")
            break
    if not cliente_encontrado:
        print("Cliente não encontrado.")

print("""
===== Bem-vindo ao nosso sistema bancário (beta v.1) =====""")

menu = """
Insira no teclado numérico a operação que deseja realizar

[1] Realizar um depósito
[2] Realizar um saque 
[3] Exibir seu extrato bancário
[4] Cadastrar cliente
[5] Criar conta
[6] Exibir contas do cliente
[0] Encerrar operação

==> """

saldo = 0
limite = 500
saques_quantia = 0
SAQUES_MAXIMO = 3
extrato = """SEU EXTRATO BANCÁRIO
"""

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor que deseja depositar ==> R$ "))
        depositar(valor)
        
    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar ==> R$ "))
        sacar(valor=valor)
        
    elif opcao == "3":
        exibir_extrato()
        
    elif opcao == "4":
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        cadastrar_cliente(nome, cpf)
        
    elif opcao == "5":
        cpf = input("Digite o CPF do cliente para criar a conta: ")
        criar_conta(cpf)
        
    elif opcao == "6":
        cpf = input("Digite o CPF do cliente para exibir as contas: ")
        exibir_contas(cpf)
        
    elif opcao == "0":
        print("Obrigado por testar nosso sistema!")
        break
        
    else:
        print("Operação inválida ou inexistente")
