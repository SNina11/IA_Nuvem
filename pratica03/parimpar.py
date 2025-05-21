pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Esse número é PAR.")
            pares += 1
        else:
            print("Esse número é ÍMPAR.")
            impares += 1
    except ValueError:
        print("Erro: você deve digitar um número inteiro ou 'fim'.")

print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
