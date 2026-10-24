historico = []

while True:
    valor_compra = float(input("Digite o valor da compra (0 para encerrar): ").replace(",", "."))

    if valor_compra == 0:
        break

    if valor_compra < 0:
        print("Valor invalido.(Input negativo)")
        continue

    idade = int(input("Idade do cliente: "))

    while idade < 0:
        print("Valor invalido.(Input negativo)")
        idade = int(input("idade do cliente: "))

    quantidade_itens = int(input("Quantidade de itens: "))
    while quantidade_itens < 0:
        print("Valor invalido.(Input negativo)")
        quantidade_itens = int(input("Digite a quantidade de itens: "))

    cupom = input("Digite o cupom de fidelidade (ou Enter para nenhum): ").strip().upper()

    valor_com_desconto = valor_compra

    if idade >= 65:
        valor_com_desconto = valor_com_desconto * 0.80

    if valor_com_desconto > 100:
        valor_com_desconto = valor_com_desconto * 0.90

    if quantidade_itens > 3:
        valor_com_desconto = valor_com_desconto * 0.95

    if cupom == "FIDELIDADE10":
        valor_com_desconto = valor_com_desconto * 0.90

    valor_final = round(valor_com_desconto, 2)
    desconto_concedido = round(valor_compra - valor_final, 2)

    historico.append({
        "original": valor_compra,
        "idade": idade,
        "quantidade": quantidade_itens,
        "cupom": cupom,
        "desconto": desconto_concedido,
        "final": valor_final
    })

    print(f"Valor final: R$ {valor_final:.2f}")

print("\nResumo Geral")

quantidade_compras = len(historico)
total_bruto = 0
total_descontos = 0
total_final = 0

for compra in historico:
    total_bruto += compra["original"]
    total_descontos += compra["desconto"]
    total_final += compra["final"]

print(f"Quantidade de compras: {quantidade_compras}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")

with open("resumo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Resumo Geral\n")
    arquivo.write(f"Quantidade de compras: {quantidade_compras}\n")
    arquivo.write(f"Total bruto: R$ {total_bruto:.2f}\n")
    arquivo.write(f"Total de descontos: R$ {total_descontos:.2f}\n")
    arquivo.write(f"Total final: R$ {total_final:.2f}\n\n")
    arquivo.write("Histórico\n")

    for indice, compra in enumerate(historico, start=1):
        arquivo.write(f"Compra {indice}: valor original R$ {compra['original']:.2f}; ")
        arquivo.write(f"idade {compra['idade']}; itens {compra['quantidade']}; ")
        arquivo.write(f"cupom '{compra['cupom']}'; desconto R$ {compra['desconto']:.2f}; ")
        arquivo.write(f"valor final R$ {compra['final']:.2f}\n")

print("Resumo salvo no arquivo resumo.txt")