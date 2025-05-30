def mostrar_info(**dados):
    for chave, valor in dados.items():
        print (f"{chave.capitalize()}: {valor}")

mostrar_info(nome="Sandra", idade=30, cidade="Ceará")