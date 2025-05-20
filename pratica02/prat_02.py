""" 1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""
valor_reais = 100
taxa_dolar = 5.20
taxa_euro = 6.15
print(f"valor_dolar: {valor_reais / taxa_dolar:.2f}")
print(f"valor_euro: {valor_reais / taxa_euro:.2f}")

"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""
produto = "Camiseta"
preco_original = 50
porcentagem_desconto = 20  # sem o símbolo %

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"Produto: {produto}")
print(f"Preço original: R${preco_original:.2f}")
print(f"Desconto: R${valor_desconto:.2f}")
print(f"Preço final: R${preco_final:.2f}")
"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""
nota_1 = 7.5
nota_2 = 8.0
nota_3 = 6.5
media = (nota_1 + nota_2 + nota_3) / 3
print(f"Media Final: {media:.2f}")
"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais
"""
distancia = 300
combustivel_gasto = 25
consumo_medio = distancia/combustivel_gasto
print(f"Consumo Medio: {consumo_medio:.2f}")