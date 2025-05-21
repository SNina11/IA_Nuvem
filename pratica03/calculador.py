def calcular():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
        except ValueError:
            print("Erro: entrada inválida. Digite um número válido.")
            continue

        try:
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: entrada inválida. Digite um número válido.")
            continue

        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            try:
                resultado = num1 / num2
            except ZeroDivisionError:
                print("Erro: divisão por zero não é permitida.")
                continue
        else:
            print("Erro: operação inválida. Use apenas +, -, * ou /.")
            continue

        print(f"Resultado: {resultado}")
        break

# Executa a calculadora
calcular()