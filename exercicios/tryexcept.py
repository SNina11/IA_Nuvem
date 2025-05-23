try:
    numerador = int(input("Digite o número:"))
    denominador = int(input("Digite o denominador:"))
    resultado = numerador / denominador
    print("O resultado é: ", resultado)
except ValueError:
   print("Por favor, entre apenas com número")
except ZeroDivisionError:
    print('Divisão por zero!!!')
    