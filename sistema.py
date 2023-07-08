""" OBJETIVOS DO PROJETO - checklist

    [x]opções - sacar, depositar, extrato e sair
    [x]depósitos tem que ser armazenados, incluídos no saldo e exibidos no extrato
    [x]não posso depositar um valor negativo
    [x]saques tem que ser armazenados, retirados do saldo e exibidos no extrato
    [x]não posso sacar um valor negativo
    [x]limite de 3 saques diários de até 500 cada
    [x]exibir valores no extrato - R$ xxx.xx"""
    
print("""
===== Bem-vindo ao nosso sistema bancário (beta v.1) =====""")
    
menu =f"""
Insira no teclado numérico a operação que deseja realizar

[1] Realizar um depósito
[2] Realizar um saque 
[3] Exibir seu extrato bancário
[0] Encerrar operação

==> """

saldo = 0
limite = 500
saques_quantia = 0
SAQUES_MAXIMO = 3
extrato = f"""SEU EXTRATO BANCÁRIO
"""


while True:
   
    opcao = input(menu)
    
    if opcao == "1":
        
        deposito = int(input("Digite o valor que deseja depositar ==> R$ "))
        if deposito <= 0:
            print("Valor inválido")
        else:
            saldo += deposito
            extrato += f"""
Depósito realizado - R$ {deposito:,.2f}"""
            print(f"Seu depósito no valor de R$ {deposito:,.2f} foi realizado!")
        
    elif opcao == "2":

        if saques_quantia < SAQUES_MAXIMO:
            
            saque = int(input("Digite o valor que deseja sacar ==> R$ "))
            if saque > saldo:
                print("Seu saldo é insuficiente para realizar este saque")
            elif saque <= 0:
                print("Valor inválido")
            elif saque > limite:
                print(f"Saque negado por ultrapassar o limite de R$ {limite:,.2f} por saque")
            else:
                saldo -= saque
                saques_quantia += 1
                extrato += f"""
Saque realizado - R$ {saque:,.2f}"""
                print(f"Seu saque no valor de R$ {saque:,.2f} foi realizado!")
        else:
            print("Você atingiu seu limite diário de 3 saques, então não pode realizar mais saques")
        
    elif opcao == "3":
        print(f"""{extrato}
Saldo atual ==> R$ {saldo:,.2f}""")
        
    elif opcao == "0":
        print("Obrigado por testar nosso sistema!")
        break
        
    else:
        print("Operação inválida ou inexistente")
        