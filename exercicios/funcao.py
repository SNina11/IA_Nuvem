# Função que executa a operação recebida com dois números
def executar_operacao(operacao, a, b=0):
    resultado = operacao(a, b)
    return resultado

# Operações
def soma(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: divisão por zero"
    return x / y

def quadrado(x, _):
    return x * x  # ou x ** 2

# Exemplos de uso
print("Soma: ", executar_operacao(soma, 8, 4))          # 12
print("Subtração: ", executar_operacao(subtrair, 8, 4)) # 4
print("Multiplicação: ", executar_operacao(multiplicar, 8, 4)) # 32
print("Divisão: ", executar_operacao(dividir, 8, 4))    # 2.0
print("Quadrado: ", executar_operacao(quadrado, 8))     # 64
