# Programa para calcular a sequência de Fibonacci
def fibonacci(n):
    #sequencia = []
    a, b = 0, 1
    for _ in range(n):
     #   sequencia.append(a)
        a, b = b, a + b
        print (a, end=" ")
    return a #sequencia

# Entrada do usuário
num_termos = int(input("Quantos termos da sequência de Fibonacci você deseja ver? "))

# Cálculo e saída
resultado = fibonacci(num_termos)
print("Sequência de Fibonacci:")
print(resultado)
