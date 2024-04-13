prestacoes = int(input("Informe o número total de pestações do consórcio: "))
prestacoes_pagas = int(input("Informe o número de pestações já pagas: "))
valor_prestacao = int(input("Informe o valor da prestação: "))

valor_pago = prestacoes_pagas * valor_prestacao
saldo_devedor = (prestacoes - prestacoes_pagas) * valor_prestacao

print("O total já pago é R$", valor_pago)
print("O saldo devedor é R$", saldo_devedor)
