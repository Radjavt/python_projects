class Conta:
    def __init__(self, agencia, numero, saldo, chave_pix, senha):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        self.chave_pix = chave_pix
        self.senha = senha

    def debitar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def creditar(self, valor):
        self.saldo += valor

class Pix:
    def __init__(self):
        self.contas = {}

    def cadastrar_conta(self, conta):
        chave_pix = conta.chave_pix
        self.contas[chave_pix] = conta

    def autenticar(self, chave_pix, senha):
        if chave_pix in self.contas:
            conta = self.contas[chave_pix]
            return conta.senha == senha
        return False

    def transferencia_pix(self, chave_origem, chave_destino, valor, senha, descricao="Transferência PIX"):
        if self.autenticar(chave_origem, senha):
            if chave_origem in self.contas and chave_destino in self.contas:
                conta_origem = self.contas[chave_origem]
                conta_destino = self.contas[chave_destino]

                if conta_origem.debitar(valor):
                    conta_destino.creditar(valor)
                    print("Transferência realizada com sucesso:")
                    print("Origem:", conta_origem.chave_pix)
                    print("Destino:", conta_destino.chave_pix)
                    print("Valor:", valor)
                    print("Descrição:", descricao)
                else:
                    print("Saldo insuficiente na conta de origem.")
            else:
                print("Conta(s) não encontrada(s).")
        else:
            print("Autenticação falhou. Chave PIX ou senha incorreta.")

def main():
    pix = Pix()

    conta1 = Conta("001", "123456", 1000.0, "11111111111", "senha123")
    pix.cadastrar_conta(conta1)

    conta2 = Conta("001", "654321", 1500.0, "22222222222", "senha456")
    pix.cadastrar_conta(conta2)

    while True:
        print("\nEscolha uma operação:")
        print("1. Cadastrar Conta")
        print("2. Transferência PIX")
        print("3. Sair")

        escolha = int(input("Digite o número da operação desejada: "))

        if escolha == 3:
            print("Programa encerrado.")
            break

        if escolha < 1 or escolha > 3:
            print("Opção inválida. Tente novamente.")
            continue

        if escolha == 1:
            agencia = input("Digite o número da agência: ")
            numero = input("Digite o número da conta: ")
            saldo = float(input("Digite o saldo inicial: "))
            chave_pix = input("Digite a chave PIX: ")
            senha = input("Digite a senha: ")
            nova_conta = Conta(agencia, numero, saldo, chave_pix, senha)
            pix.cadastrar_conta(nova_conta)
            print("Conta cadastrada com sucesso.")

        elif escolha == 2:
            chave_origem = input("Digite a chave PIX da conta de origem: ")
            chave_destino = input("Digite a chave PIX da conta de destino: ")
            valor = float(input("Digite o valor da transferência: "))
            senha = input("Digite a senha: ")
            descricao = input("Digite uma descrição para a transferência: ")

            pix.transferencia_pix(chave_origem, chave_destino, valor, senha, descricao)

if __name__ == "__main__":
    main()