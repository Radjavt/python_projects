def deposito(caixa, conta, valor):
    if conta >= 0 and conta < len(caixa):
        caixa[conta] += valor
        print("Depósito de R$", valor, "na conta", conta, "realizado com sucesso.")
    else:
        print("Conta inválida.")

def saque(caixa, conta, valor):
    if conta >= 0 and conta < len(caixa):
        if caixa[conta] >= valor:
            caixa[conta] -= valor
            print("Saque de R$", valor, "da conta", conta, "realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta inválida.")

def transferencia(caixa, conta_origem, conta_destino, valor):
    if conta_origem >= 0 and conta_origem < len(caixa) and conta_destino >= 0 and conta_destino < len(caixa):
        if caixa[conta_origem] >= valor:
            caixa[conta_origem] -= valor
            caixa[conta_destino] += valor
            print("Transferência de R$", valor, "da conta", conta_origem, "para a conta", conta_destino, "realizada com sucesso.")
        else:
            print("Saldo insuficiente na conta de origem.")
    else:
        print("Conta(s) inválida(s).")

def extrato(caixa, conta):
    if conta >= 0 and conta < len(caixa):
        print("Extrato da conta", conta)
        print("Saldo atual: R$", caixa[conta])
    else:
        print("Conta inválida.")

def criar_conta(caixa):
    caixa.append(0)
    print("Nova conta criada. Número da conta:", len(caixa) - 1)

def todas_contas(caixa):
    print("Todas as contas e seus saldos:")
    for i, saldo in enumerate(caixa):
        print("Conta", i, "- Saldo: R$", saldo)

def balanco_geral(caixa):
    total = sum(caixa)
    print("Balanço Geral do Caixa:")
    print("Total de contas:", len(caixa))
    print("Total de ativos: R$", total)

def main():
    caixa = []

    while True:
        print("\nEscolha uma operação:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Transferência")
        print("4. Consultar Extrato")
        print("5. Criar Nova Conta")
        print("6. Todas as Contas")
        print("7. Balanço Geral")
        print("8. Sair")

        escolha = int(input("Digite o número da operação desejada: "))

        if escolha == 8:
            print("Programa encerrado.")
            break

        if escolha < 1 or escolha > 7:
            print("Opção inválida. Tente novamente.")
            continue

        if escolha != 5 and escolha != 6 and escolha != 7:
            conta = int(input("Digite o número da conta: "))

            if conta < 0 or conta >= len(caixa):
                print("Conta inválida.")
                continue

        if escolha == 1:
            valor = float(input("Digite o valor do depósito: "))
            deposito(caixa, conta, valor)
        elif escolha == 2:
            valor = float(input("Digite o valor do saque: "))
            saque(caixa, conta, valor)
        elif escolha == 3:
            conta_destino = int(input("Digite o número da conta de destino: "))
            valor = float(input("Digite o valor da transferência: "))
            transferencia(caixa, conta, conta_destino, valor)
        elif escolha == 4:
            extrato(caixa, conta)
        elif escolha == 5:
            criar_conta(caixa)
        elif escolha == 6:
            todas_contas(caixa)
        elif escolha == 7:
            balanco_geral(caixa)

if __name__ == "__main__":
    main()