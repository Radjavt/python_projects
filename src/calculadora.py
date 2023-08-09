def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero não é permitida"
    return num1 / num2

def porcentagem(num1, num2):
    return (num1 * num2) / 100

def main():
    while True:
        print("\nEscolha uma operação:")
        print("(1) Soma")
        print("(2) Subtração")
        print("(3) Multiplicação")
        print("(4) Divisão")
        print("(5) Porcentagem")
        print("(6) Sair")

        escolha = int(input("Digite o número da operação desejada: "))

        if escolha == 6:
            print("Calculadora encerrada.")
            break

        if escolha < 1 or escolha > 5:
            print("Opção inválida. Tente novamente.")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == 1:
            resultado = soma(num1, num2)
        elif escolha == 2:
            resultado = subtracao(num1, num2)
        elif escolha == 3:
            resultado = multiplicacao(num1, num2)
        elif escolha == 4:
            resultado = divisao(num1, num2)
        elif escolha == 5:
            resultado = porcentagem(num1, num2)

        print("Resultado:", resultado)

if __name__ == "__main__":
    main()